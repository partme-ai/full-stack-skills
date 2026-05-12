# Docker Compatibility Notes

This skill relies on the `dreamina` CLI, which requires GLIBC 2.33+.
On systems with older GLIBC (Alibaba Cloud Linux 3, CentOS 7/8, RHEL 8, Debian Bullseye),
the binary must run inside a Docker container with Ubuntu 22.04 or Debian Bookworm.

## Key limitation: login state does not persist across separate `docker run` calls

When running dreamina via Docker, auth tokens are stored ephemerally.
A `login` in one container invocation and a `user_credit` in a second will fail
with "未检测到有效登录态".

**Workaround**: Run login + commands in a single container session:
```bash
docker run --rm --entrypoint sh dreamina-cli -c '
  /root/.local/bin/dreamina login &&
  /root/.local/bin/dreamina user_credit
'
```

## Config files that may be absent

The official docs reference `config.toml`, `credential.json`, `tasks.db` at `~/.dreamina_cli/`,
but these were NOT found after a successful Docker-based login. Do not rely on their existence.

The definitive auth check is `dreamina user_credit` returning your balance.

See the `dreamina-cli` skill's `references/docker-compatibility.md` for full setup details.
