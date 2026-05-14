import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime

DSL_STREAM_API_URL = "https://smart.processon.com/v1/chat/completion"
DSL_STREAM_MODEL = "deepseek-v3-2-251201"
DSL_STREAM_UID = "567890"
DSL_EDIT_URL = "https://smart.processon.com/editor"
IMAGE_RENDER_API_URL = "https://smart.processon.com/v1/api/generate/img"


def normalize_title(title):
    if not title:
        return "processon-diagram"
    normalized = title.strip("，。；：、 ,.-_")
    if not normalized:
        return "processon-diagram"
    return normalized[:20]


def slugify_filename(title):
    if not title:
        return "processon-diagram"
    slug = re.sub(r"[^\u4e00-\u9fffA-Za-z0-9_-]+", "-", title).strip("-_")
    if not slug:
        slug = "processon-diagram"
    return slug[:40]


def save_image_content(title, content_items, output_dir=None):
    if not output_dir:
        output_dir = os.path.join(os.getcwd(), "outputs", "processon")

    saved_paths = []
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    image_index = 1
    title = normalize_title(title)
    filename_slug = slugify_filename(title)

    for item in content_items:
        if not isinstance(item, dict):
            continue
        if item.get("type") != "image":
            continue
        if item.get("mimeType") != "image/png":
            continue

        image_data = item.get("data", "")
        if not image_data:
            continue

        if image_index == 1:
            filename = f"{filename_slug}-{timestamp}.png"
        else:
            filename = f"{filename_slug}-{timestamp}-{image_index}.png"
        file_path = os.path.abspath(os.path.join(output_dir, filename))
        with open(file_path, "wb") as f:
            f.write(base64.b64decode(image_data))
        saved_paths.append(file_path)
        image_index += 1

    return {
        "title": title,
        "filename_slug": filename_slug,
        "saved_paths": saved_paths,
    }


def normalize_bearer(api_key):
    if not api_key:
        return None
    api_key = api_key.strip()
    if not api_key:
        return None
    if api_key.lower().startswith("bearer "):
        return api_key
    return f"Bearer {api_key}"


def build_headers(api_key):
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "*/*",
        "User-Agent": "ProcessOn-Architect-Skill/3.0",
    }
    bearer = normalize_bearer(api_key)
    if bearer:
        headers["Authorization"] = bearer
    return headers


def build_stream_payload(prompt):
    return {
        "model": DSL_STREAM_MODEL,
        "prompt": prompt,
        "uid": DSL_STREAM_UID,
        "source": "skill",
        "cancelPursueNode": True,
    }


def build_image_payload(dsl, diagram_type):
    payload = {
        "prompt": dsl,
        "source": "skill",
    }
    if diagram_type:
        payload["diagramType"] = diagram_type
    return payload


def normalize_content_items(content_items):
    normalized = []
    for item in content_items:
        if not isinstance(item, dict):
            continue
        normalized_item = dict(item)
        if "data" in normalized_item and "text" not in normalized_item and normalized_item.get("type") == "text":
            normalized_item["text"] = normalized_item["data"]
        normalized.append(normalized_item)
    return normalized


def extract_content_items(result):
    if isinstance(result, list):
        return result
    if not isinstance(result, dict):
        return None
    if isinstance(result.get("content"), list):
        return result["content"]
    if isinstance(result.get("data"), dict) and isinstance(result["data"].get("content"), list):
        return result["data"]["content"]
    return None


def extract_remote_image_urls(content_items):
    urls = []
    for item in content_items:
        if not isinstance(item, dict):
            continue
        if item.get("type") != "image_url":
            continue
        url = item.get("url")
        if isinstance(url, str) and url.strip():
            urls.append(url.strip())
    return urls


def build_final_image_payload(result, diagram_title):
    content = extract_content_items(result)
    if content is None:
        raise ValueError("Invalid image response: missing 'content' array")

    normalized_content = normalize_content_items(content)
    remote_image_urls = extract_remote_image_urls(normalized_content)
    save_result = save_image_content(diagram_title, normalized_content)
    saved_paths = save_result["saved_paths"]

    output_content = []
    for item in normalized_content:
        if not isinstance(item, dict):
            continue
        if item.get("type") in ("image", "image_url"):
            output_content.append(item)
    if remote_image_urls:
        output_content.append({
            "type": "text",
            "text": "\n".join(["图片链接："] + remote_image_urls),
        })
    if saved_paths:
        output_content.append({
            "type": "text",
            "text": "\n".join(["图片已保存："] + saved_paths),
        })

    output_payload = {"content": output_content}
    if isinstance(result, dict) and isinstance(result.get("data"), dict):
        output_payload["data"] = dict(result["data"])
    if remote_image_urls:
        output_payload.setdefault("data", {})
        output_payload["data"]["remoteImageUrls"] = remote_image_urls
    if saved_paths:
        output_payload.setdefault("data", {})
        output_payload["data"].update({
            "imageTitle": save_result["title"],
            "savedImagePaths": saved_paths,
            "primarySavedImagePath": saved_paths[0],
            "preferredDisplay": "inline",
            "showInlineIfPossible": True,
        })
    return output_payload


def build_image_failure_payload(message):
    return {
        "content": [
            {
                "type": "text",
                "text": "\n".join([
                    "DSL 已生成，但图片生成失败。",
                    f"你可以打开编辑链接，粘贴 DSL 继续渲染和导出图片：{DSL_EDIT_URL}",
                    f"失败原因：{message}",
                ]),
            }
        ],
        "data": {"errorCode": "IMAGE_RENDER_FAILED"},
    }


def generate_diagram(prompt, title=None, stream_style=None, output_mode=None, auto_render=True):
    output_mode = (output_mode or os.environ.get("PROCESSON_OUTPUT_MODE", "text")).strip().lower()
    stream_style = (stream_style or os.environ.get("PROCESSON_STREAM_STYLE", "host")).strip().lower()
    dsl_event_buffer = ""

    def is_json_output():
        return output_mode == "json"

    def is_event_stream_output():
        return output_mode in ("eventstream", "event-stream", "events", "jsonl", "ndjson")

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(write_through=True)
        except Exception:
            pass

    def write_stdout(text):
        if text is None:
            return
        if not isinstance(text, str):
            text = str(text)
        sys.stdout.write(text)
        sys.stdout.flush()

    def mcp_print(payload):
        if is_json_output():
            print(json.dumps(payload, ensure_ascii=False), flush=True)
            return
        if is_event_stream_output():
            for event in payload_to_events(payload):
                print(json.dumps(event, ensure_ascii=False), flush=True)
            return
        text = payload_to_text(payload)
        if text:
            write_stdout(text)
            if not text.endswith("\n"):
                write_stdout("\n")

    def mcp_print_text(text, data=None):
        if is_json_output() or is_event_stream_output():
            payload = {"event": "commentary", "text": text}
            if data:
                payload.update(data)
            print(json.dumps(payload, ensure_ascii=False), flush=True)
            return
        write_stdout(text)

    def payload_to_text(payload):
        if not isinstance(payload, dict):
            return json.dumps(payload, ensure_ascii=False)

        content = payload.get("content")
        parts = []
        if isinstance(content, list):
            for item in content:
                if not isinstance(item, dict):
                    continue
                item_type = item.get("type")
                if item_type == "text":
                    text = item.get("text")
                    if text is None:
                        text = item.get("data")
                    if isinstance(text, str) and text:
                        parts.append(text)
                elif item_type == "image_url":
                    url = item.get("url")
                    if isinstance(url, str) and url.strip():
                        parts.append(url.strip())

        if parts:
            return "\n\n".join(parts)

        data = payload.get("data")
        if isinstance(data, dict):
            extra_parts = []
            remote_urls = data.get("remoteImageUrls") or []
            saved_paths = data.get("savedImagePaths") or []
            if remote_urls:
                extra_parts.append("\n".join(["图片链接："] + remote_urls))
            if saved_paths:
                extra_parts.append("\n".join(["图片已保存："] + saved_paths))
            if extra_parts:
                return "\n\n".join(extra_parts)

        return json.dumps(payload, ensure_ascii=False)

    def payload_to_events(payload):
        events = []
        if not isinstance(payload, dict):
            return [{"event": "message", "text": json.dumps(payload, ensure_ascii=False)}]

        content = payload.get("content")
        if isinstance(content, list):
            for item in content:
                if not isinstance(item, dict):
                    continue
                item_type = item.get("type")
                if item_type == "text":
                    text = item.get("text")
                    if text is None:
                        text = item.get("data")
                    if isinstance(text, str) and text:
                        events.append({"event": "message", "text": text, "data": {"contentType": "text"}})
                elif item_type == "image_url":
                    url = item.get("url")
                    if isinstance(url, str) and url.strip():
                        events.append({"event": "image_url", "text": url.strip(), "data": {"contentType": "image_url"}})
                elif item_type == "image":
                    events.append({"event": "image", "data": item})

        data = payload.get("data")
        if isinstance(data, dict):
            for url in data.get("remoteImageUrls") or []:
                if isinstance(url, str) and url.strip():
                    events.append({"event": "image_url", "text": url.strip(), "data": {"contentType": "image_url"}})
            for path in data.get("savedImagePaths") or []:
                if isinstance(path, str) and path.strip():
                    events.append({"event": "saved_image_path", "text": path.strip(), "data": {"contentType": "saved_image_path"}})

        if not events:
            events.append({"event": "message", "text": json.dumps(payload, ensure_ascii=False)})
        return events

    def emit_event(event_type, text=None, data=None):
        payload = {"event": event_type}
        if text is not None:
            payload["text"] = text
        if data is not None:
            payload["data"] = data
        print(json.dumps(payload, ensure_ascii=False), flush=True)

    def flush_dsl_event_buffer(force=False):
        nonlocal dsl_event_buffer
        if not is_event_stream_output():
            return
        if not dsl_event_buffer:
            return
        if force or len(dsl_event_buffer) > 20 or "\n" in dsl_event_buffer:
            emit_event("dsl_line", text=dsl_event_buffer)
            dsl_event_buffer = ""

    def build_credential_metadata():
        macos_command = 'export PROCESSON_API_KEY="<your-processon-api-key>"'
        windows_powershell_command = '$env:PROCESSON_API_KEY="<your-processon-api-key>"'
        windows_cmd_command = 'set PROCESSON_API_KEY=<your-processon-api-key>'
        return {
            "credential": {
                "name": "PROCESSON_API_KEY",
                "label": "ProcessOn API Key",
                "kind": "secret",
                "required": True,
                "envVar": "PROCESSON_API_KEY",
                "placeholder": "<your-processon-api-key>",
                "description": "用于 ProcessOn API 的鉴权密钥。",
            },
            "actions": [
                {
                    "type": "request_credential",
                    "credential": "PROCESSON_API_KEY",
                    "label": "配置 ProcessOn API Key",
                    "mode": "secret",
                },
                {
                    "type": "show_config_example",
                    "target": "processon-api",
                    "label": "查看配置示例",
                },
                {
                    "type": "copy_command",
                    "label": "复制 macOS/Linux 配置命令",
                    "command": macos_command,
                    "platform": ["macos", "linux"],
                },
                {
                    "type": "copy_command",
                    "label": "复制 Windows PowerShell 配置命令",
                    "command": windows_powershell_command,
                    "platform": ["windows"],
                    "shell": "powershell",
                },
                {
                    "type": "copy_command",
                    "label": "复制 Windows CMD 配置命令",
                    "command": windows_cmd_command,
                    "platform": ["windows"],
                    "shell": "cmd",
                },
                {
                    "type": "retry",
                    "label": "配置完成后重试",
                },
            ],
            "suggestedCommands": {
                "macos_linux": macos_command,
                "windows_powershell": windows_powershell_command,
                "windows_cmd": windows_cmd_command,
                "verify": "echo $PROCESSON_API_KEY",
                "retryPrompt": "继续生成流程图",
            },
            "interactive": {
                "canRequestCredential": True,
                "preferredAction": "request_credential",
            },
        }

    def build_missing_api_key_payload():
        hint = "\n".join([
            "当前还没有检测到可用的 ProcessOn API Key，所以暂时无法直接生成流程图。",
            "API Key/Token 获取地址：https://smart.processon.com/user",
            "macOS/Linux:",
            '  export PROCESSON_API_KEY="<your-processon-api-key>"',
        ])
        payload = {
            "content": [{"type": "text", "text": hint}],
            "data": {"errorCode": "MISSING_API_KEY"},
        }
        payload["data"].update(build_credential_metadata())
        return payload

    def build_invalid_api_key_payload(http_message):
        hint = "\n".join([
            "检测到 PROCESSON_API_KEY，但鉴权失败。当前配置的 API Key 可能无效、已过期，或不适用于当前接口。",
            "如需重新获取 Token，请访问：https://smart.processon.com/user",
            "",
            f"失败原因：{http_message}",
            "",
            "请检查：",
            "1. PROCESSON_API_KEY 是否填写正确",
            "2. 该 Key 是否具备 smart.processon.com 接口访问权限",
            "3. 是否误填了其他系统的 token",
        ])
        payload = {
            "content": [{"type": "text", "text": hint}],
            "data": {"errorCode": "INVALID_API_KEY"},
        }
        payload["data"].update(build_credential_metadata())
        return payload

    def extract_complete_json(buffer):
        depth = 0
        in_string = False
        escape = False
        start_index = -1

        for index, char in enumerate(buffer):
            if in_string:
                if escape:
                    escape = False
                elif char == "\\":
                    escape = True
                elif char == '"':
                    in_string = False
                continue

            if char == '"':
                in_string = True
                continue

            if char == "{":
                if depth == 0:
                    start_index = index
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0 and start_index != -1:
                    return buffer[start_index:index + 1], buffer[index + 1:]

        return None

    def parse_json_response(response):
        status_code = getattr(response, "status", "unknown")
        content_type = response.headers.get("Content-Type", "unknown")
        response_data = response.read().decode("utf-8")
        if not response_data.strip():
            raise ValueError(
                f"Empty response body from ProcessOn API "
                f"(status={status_code}, content_type={content_type})"
            )
        try:
            return json.loads(response_data)
        except json.JSONDecodeError as exc:
            snippet = response_data[:500]
            raise ValueError(
                f"Invalid JSON response from ProcessOn API "
                f"(status={status_code}, content_type={content_type}, body_prefix={snippet!r})"
            ) from exc

    def open_json_request(url, headers, payload, timeout=180):
        json_payload = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        request = urllib.request.Request(url, data=json_payload, headers=headers, method="POST")
        return urllib.request.urlopen(request, timeout=timeout)

    def use_markdown_stream():
        return stream_style in ("markdown", "md", "codefence", "code_fence", "fenced")

    def guess_dsl_code_fence(dsl_text):
        if not isinstance(dsl_text, str):
            return ""
        stripped = dsl_text.strip()
        if not stripped:
            return ""
        first_line = ""
        for line in stripped.splitlines():
            normalized = line.strip()
            if normalized:
                first_line = normalized.lower()
                break
        if first_line.startswith((
            "graph ",
            "flowchart ",
            "sequencediagram",
            "classdiagram",
            "statediagram",
            "statediagram-v2",
            "erdiagram",
            "journey",
            "gantt",
            "mindmap",
            "timeline",
            "gitgraph",
            "pie",
            "quadrantchart",
            "requirementdiagram",
            "xychart",
            "block-beta",
        )):
            return "mermaid"
        if stripped.startswith("{") or stripped.startswith("["):
            return "json"
        return "text"

    def build_first_stage_display_text(dsl_text):
        fence = guess_dsl_code_fence(dsl_text)
        lines = [
            "第一阶段已完成，DSL 已生成。",
            "",
            "编辑链接：",
            DSL_EDIT_URL,
            "",
            "DSL 原文如下（你可以复制上方 DSL 数据到此链接进行渲染和二次编辑）：",
            f"```{fence}",
            dsl_text,
            "```",
        ]
        return "\n".join(lines)

    def emit_dsl_stream_prefix():
        if use_markdown_stream():
            mcp_print_text(
                "创建图结果：\n```text\n",
                data={"event": "dsl_start", "streamStyle": "markdown"},
            )
            return
        mcp_print_text(
            "创建图结果（实时输出）：\n",
            data={"event": "dsl_start", "streamStyle": "host"},
        )

    def emit_dsl_stream_suffix():
        flush_dsl_event_buffer(force=True)
        if use_markdown_stream():
            mcp_print_text("\n```\n", data={"event": "dsl_complete", "streamStyle": "markdown"})
            return
        mcp_print_text("\n\nDSL 输出结束。\n", data={"event": "dsl_complete", "streamStyle": "host"})

    def emit_edit_link():
        mcp_print_text(
            "\n".join([
                "编辑链接：",
                DSL_EDIT_URL,
                "",
                "你可以复制上方 DSL 数据到此链接进行渲染和二次编辑。",
            ]) + "\n",
            data={"event": "edit_link", "url": DSL_EDIT_URL},
        )

    def stream_dsl_from_chat_completion(prompt_text, headers):
        payload = build_stream_payload(prompt_text)
        ai_content_arr = ["", "", ""]
        step_number = 0
        diagram_type = ""
        dsl_started = False
        event_name = None
        event_data_lines = []

        with open_json_request(DSL_STREAM_API_URL, headers, payload, timeout=300) as response:
            for raw_line in response:
                line = raw_line.decode("utf-8", errors="replace")
                stripped = line.strip("\r\n")

                if not stripped:
                    if event_data_lines:
                        event_data = "\n".join(event_data_lines)
                        event_name, step_number, diagram_type, dsl_started = handle_stream_message(
                            event_name,
                            event_data,
                            ai_content_arr,
                            step_number,
                            diagram_type,
                            dsl_started,
                        )
                        if event_name == "DONE":
                            break
                    event_name = None
                    event_data_lines = []
                    continue

                if stripped.startswith(":"):
                    continue
                if stripped.startswith("event:"):
                    event_name = stripped.split(":", 1)[1].strip()
                if stripped.startswith("data:"):
                    event_data_lines.append(stripped.split(":", 1)[1].lstrip())

            if event_data_lines:
                event_name, step_number, diagram_type, dsl_started = handle_stream_message(
                    event_name,
                    "\n".join(event_data_lines),
                    ai_content_arr,
                    step_number,
                    diagram_type,
                    dsl_started,
                )

        dsl = ai_content_arr[2].rstrip()
        if not dsl:
            raise ValueError("DSL generation failed: empty DSL result from stream")
        return dsl, diagram_type

    def handle_stream_message(current_event_name, raw_data, ai_content_arr, step_number, diagram_type, dsl_started):
        nonlocal dsl_event_buffer
        try:
            parsed = json.loads(raw_data)
            data = parsed["a"]
        except Exception:
            return current_event_name, step_number, diagram_type, dsl_started

        if data == "语义分析结果：":
            step_number = 1
            ai_content_arr[1] = ""
            mcp_print_text("语义分析结果：\n", data={"event": "analysis_start"})
            return current_event_name, step_number, diagram_type, dsl_started
        if data == "创建图结果：":
            step_number = 2
            ai_content_arr[2] = ""
            dsl_started = True
            emit_dsl_stream_prefix()
            return current_event_name, step_number, diagram_type, dsl_started
        if data == "追问结果：":
            if dsl_started:
                emit_dsl_stream_suffix()
                emit_edit_link()
            return current_event_name, 3, diagram_type, False
        if data == "[DONE]":
            if dsl_started:
                emit_dsl_stream_suffix()
                emit_edit_link()
            return "DONE", 3, diagram_type, False

        if step_number == 1:
            ai_content_arr[1] += data
            extracted = extract_complete_json(ai_content_arr[1])
            while extracted:
                json_str, rest = extracted
                ai_content_arr[1] = rest
                parsed_json = json.loads(json_str)
                if parsed_json.get("type") == "analysis" and parsed_json.get("content"):
                    analysis_text = parsed_json["content"]
                    if output_mode != "json" and not analysis_text.endswith("\n"):
                        analysis_text += "\n"
                    mcp_print_text(analysis_text, data={"event": "analysis_chunk"})
                    if is_event_stream_output():
                        emit_event("analysis_complete", text=analysis_text.strip())
                if parsed_json.get("type") == "route":
                    diagram_type = parsed_json.get("diagramType") or diagram_type
                    if is_event_stream_output() and diagram_type:
                        emit_event("route", text=diagram_type, data={"diagramType": diagram_type})
                extracted = extract_complete_json(ai_content_arr[1])
        elif step_number == 2:
            ai_content_arr[2] += data
            mcp_print_text(data, data={"event": "dsl_chunk"})
            if is_event_stream_output():
                dsl_event_buffer += data
                flush_dsl_event_buffer()

        return current_event_name, step_number, diagram_type, dsl_started

    api_key = os.environ.get("PROCESSON_API_KEY", "")

    try:
        if not api_key.strip():
            mcp_print(build_missing_api_key_payload())
            sys.exit(1)

        headers = build_headers(api_key)
        dsl, diagram_type = stream_dsl_from_chat_completion(prompt, headers)
        
        # End of first stage
        display_text = build_first_stage_display_text(dsl)
        result_data = {
            "dsl": dsl,
            "diagramType": diagram_type,
            "editUrl": DSL_EDIT_URL,
            "title": title,
            "displayText": display_text,
            "displayImmediately": True,
        }
        
        if is_event_stream_output():
            emit_event("dsl_ready", text=display_text, data=result_data)
        elif is_json_output():
            mcp_print({
                "content": [{"type": "text", "text": display_text}],
                "data": result_data,
            })
        else:
            # For plain text mode, we already printed fragments.
            # But we might want to ensure the final block is clear.
            pass

        if auto_render:
            if is_event_stream_output():
                emit_event("image_render_start", text="正在渲染图片")
            
            try:
                render_payload = build_image_payload(dsl, diagram_type)
                with open_json_request(IMAGE_RENDER_API_URL, headers, render_payload, timeout=180) as response:
                    image_result = parse_json_response(response)
                    final_payload = build_final_image_payload(image_result, title)
                    if is_event_stream_output():
                        emit_event("image_render_succeeded", text="图片渲染成功")
                    mcp_print(final_payload)
            except Exception as e:
                msg = str(e)
                if is_event_stream_output():
                    emit_event("image_render_failed", text=msg)
                mcp_print(build_image_failure_payload(msg))

        return dsl, diagram_type

    except urllib.error.HTTPError as exc:
        try:
            body = exc.read().decode("utf-8")
            msg = f"HTTP {exc.code} {exc.reason}: {body}"
        except Exception:
            msg = f"HTTP {exc.code} {exc.reason}"
        current_api_key = os.environ.get("PROCESSON_API_KEY", "").strip()
        if exc.code in (401, 403) and not current_api_key:
            missing_payload = build_missing_api_key_payload()
            missing_payload["content"][0]["text"] = f"{msg}\n\n{missing_payload['content'][0]['text']}"
            mcp_print(missing_payload)
            sys.exit(1)
        if exc.code in (401, 403) and current_api_key:
            mcp_print(build_invalid_api_key_payload(msg))
            sys.exit(1)
        mcp_print_text(msg)
        sys.exit(1)
    except urllib.error.URLError as exc:
        mcp_print_text(f"Connection Error: {exc.reason}")
        sys.exit(1)
    except Exception as exc:
        mcp_print_text(str(exc))
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ProcessOn AI Diagram Generator")
    parser.add_argument("prompt", type=str, help="The optimized prompt for the diagram")
    parser.add_argument("--title", type=str, default="processon-diagram", help="Short title for the saved image filename")
    parser.add_argument(
        "--stream-style",
        type=str,
        choices=["host", "markdown"],
        default=None,
        help="Streaming presentation style.",
    )
    parser.add_argument(
        "--output-mode",
        type=str,
        choices=["text", "json", "eventstream", "jsonl", "ndjson"],
        default=None,
        help="Output mode.",
    )
    parser.add_argument(
        "--no-render",
        action="store_false",
        dest="auto_render",
        help="Disable automatic image rendering.",
    )
    parser.set_defaults(auto_render=True)

    args = parser.parse_args()

    generate_diagram(
        args.prompt,
        args.title,
        stream_style=args.stream_style,
        output_mode=args.output_mode,
        auto_render=args.auto_render,
    )
