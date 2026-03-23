

设计管理
✅ get_editor_state() - 获取编辑器状态

Get the currently active canvas editor, the current user selection and other essential design information
to get started on a design task.
Parameters:
include _ schema: Set this flag to true if you want the .pen file schema to be included. lf you areaware of the .pen file schema already, set this to false

✅ open_document() - 打开/创建文档

If there is no active editor, pass "'new" to open new document or if user requests to open a specificpen file, pass the file path to open it.
Parameters:
filePathOrTemplate: File path to an existing .pen file, OR 'new' for a new document. No othertemplate names are valid.

✅ batch_design() - 批量设计操作

Retrieve nodes by searching for matching patterns and by node ids in batches.
IMPORTANT: Combine multiple search patterns and node lD searches into one call.
lMPORTANT: When you want to perform multiple searches and node id reads after another.
combine them into one call.
lf neither patterns nor nodelds is specified, returns the top-level children of the document.When using design system components, AVOlD reading each component one-by-one. Instead listall of the available components in a single tool call.
To list components of a design system, search for reusable nodes inside the design systems frameUse this tool in the beginning to list components of a design system or design kit to understand its
available components.
This tool will return the searched nodes and its direct children. Use searchDepth to define howmany levels to search in.
Be careful using readDepth > 3, because it can return large amounts of data overflowing thecontext. Prefer using low numbers.
Path geometry is abbreviated by default; set includePathGeometry=true for full geometry dataSet resolveVariables=true to see computed values instead of variable references

Traversing large documents:
1. Start by reading top-level nodes, or nodes you already know the IDs of to understand overalstructure
2. Decide if the nodes you have already read are sufficient for your task3. lf you need more data and you see ".." for children, make new read calls with those specific childIDs

Example
To search for the reusable components in the desian system: { "filePath": "desians/forms.pen"

✅ batch_get() - 批量获取节点

Execute multiple insert/copy/updatemove/delete/image operations in a single call.
Usage
*Keep each batch_design call to maximum 25 operations for optimal performance.For larger designs, split work into multiple batch design calls by logical sections (eg., screen structure first, then sidebar content, thenmain content).
Avoid creating large operation objects like an insert with multiple descendants. Prefer breaking it down into many separate operations
instead.
lf one of the operations fails, all previously executed operations in that block will be rolled back..lmportant: always create new binding names for every operation list, DO NOT reuse binding names across operation listsA list of potential issues will be returned in the response message. Try to fix them in the next batch _design cal.
Working with Component Instances
When you insert a component instance and want to modify its descendants:
1.Update properties →Use U() with the instance path:
card=I(body, {type:"ref", ref:"CardComp"})U(card+"/titleText",{content: "New Title"})
2.Replace a descendant entirely → R() with the instance path:
card=I(body,{type:"ref",ref:"CardComp"})newTitle=R(card+"/headerSlot", {type:"text", content: "Custom Title"})
3. Add new children → Use l() on regular frames or document root:
   {type:"frame",layout:"vertical"})container=I(bodyitem=I(container,"'text""'New item'"})黌蹚灄叫蚍蹈鑥恼設駙勲肃俄pe :content:

✅ snapshot_layout() - 布局快照

Check the current layout structure of an .pen file
Be careful with omitting the maxDepth parameter, as large maxDepth values can result in a lot ofdata.
lf you're only interested in overlapping elements, clipped elements, etc. then use the problemsOnlyparameter.
Example:
. maxDepth=0 means only the top level nodes layout will be returned. Useful for finding space for anew frame on the canvas.
Parameters:
filePath: An optional file path to access a .pen file.
, maxDepth: Limit how deep to descend in the node tree. lf omitted, the search is limited to thenode and its direct children. When maxDepth is reached, omitted children are replaced with "..."Unlimited depth can result in a lot of data, prefer specifying a maxDepth.parentld: Only return the layout rectangles in this node's subtree. lf omitted returns the layout ofthe whole document.
problemsOnly: Only return nodes that have some kind of problem with their layout, e.g. they areclipped by their parents.lf omitted,the value is false


✅ get_screenshot() - 获取截图

This tool returns a screenshot of a node in a .pen file.
Usage:
IMPORTANT: Always analyze the returned screenshot image to make sure that the generated resultlooks correct, satisfies the design requirements and doesn't contain any visual errors, glitches ormisalignment.
IMPORTANT: Think carefully after you received a screenshot to detect any possible design issuesor inconsistencies in the generated design.
Use this tool to get a screenshot image representation of specific nodes, frames or other elementsbased on their IDs. This is useful to verify and compare the generated layout with the originaldesign.
You can also use this tool to check elements and design system components, to verify their layoutand look.
Parameters:
filePath: An optional file path to access a .pen filenodeld: The lD of the node to get a screenshot of

风格与指南
✅ get_guidelines() - 获取设计指南

This tool returns the design guidelines and rules for working with .pen files.
Usage:
lMPORTANT: Follow the guidelines and design rules to solve your design tasks.Call this tool multiple times with different topics to retrieve the relevant guidelines based on whatyou will work on next.
This tool provides essential information about the .pen file schema, components, layout.
止ositioning,typography,and other design rules.
Available topics:
design-system: Guidelines for composing screens and dashboards using design systemcomponents. Use this when building SaaS apps, dashboards, or screens with existing reusablecomponents.
code: Coding guidelines to generate code from .pen files. Use this tool when your task involvesgenerating code or implementations from .pen files. Guidelines to work with tables in .pen files. Use this when asked to insert, update or movetables or dashboards.
tailwind: Tailwind v4 specific implementation guidelines. Use when implementing designs withTailwind CSS.
landing-page: Guidelines for designing high-conversion landing page websites from scratch. Usethis when asked to design landing pages, websites, or promotional web pages.
Parameters:
topic: A topic to return the design guidelines for. You can only pick a single one at a time.

✅ get_style_guide_tags() - 获取风格标签

This tool returns a style guide for design inspiration based on a set of tags.
Usage:
USE for any design task that benefits from creative direction or visual inspirationUSE when creating landing pages, marketing sites, dashboards, or app screensUSE when the user asks for a specific aesthetic, style, or mood
USE when designing from scratch, on a blank canvas, or exploring new directionsUSE when remixing, restyling, or creating variationsConsider SKlPPiNG only when the task is purely compositional (e.g. "add a button here") with an
existing design systemTry to include mobile, website, or webapp tag if possibleONLY use tags received from the earlier "get style guide tags" call.. lf a style guide lD is explicitly provided, just pass the ID to this tool to use it to retrieve a specificstyle guide by lD instead of searching by tags.
Parameters:
id: Optional style guide ID to retrieve a specific style guide by lD instead of searching by tagstags: Optional: Specify 5-10 tags best fitting for the current design task based on the available setof tags returned by "get style guide tags"

✅ get_style_guide() - 获取风格指南


This tool returns all the available style guide tags available.
Usage:
USE for any design task that benefits from creative direction or visual inspirationUSE when creating landing pages, marketing sites, dashboards, or app screens
USE when the user asks for a specific aesthetic, style, or mood
USE when designing from scratch or on a blank canvas
USE when remixing, restyling, or exploring variations.Consider SKlPPlNG only when the task is purely compositional (e.g. "add a button here") with an
existing design system
Call this tool first, then use the tags or style guide lD in "get style _ guide".
No parameters

变量管理
✅ get_variables() - 获取设计变量

Get the variables and themes defined in this .pen file.
Use the result of this tool to create global CSS rules to use in a codebase..When generating code from a design, use this tool to get the global styling rules associated withthe design.
Parameters:
filePath: An optional file path to access a .pen file.

✅ set_variables() - 设置设计变量


Update the variables and themes defined in this .pen file
lf a variable is using theming, theme axes and values that aren't yet present in the document will beautomatically registered.
IMPORTANT: variable names are arbitrary strings. They don't have to begin with a dollar sign!
Parameters:
filePath: An optional file path to access a .pen file.
replace: By default, the variables are merged into the document's existing variable definitions. lfyou want to completely replace the document's existing variable definitions, pass true for thisflag.
variables: Follow the variable definition in the .pen file schema. lf you are not familiar with the .penfile schema, you can retrieve it by getting the general guidelines.

画布操作
✅ find_empty_space_on_canvas() - 查找空白区域

Find empty space in a .pen file for a given direction and desired sizeIf nodeld is provided, finds space around that specific node. lf nodeld is omitted, finds space aroundthe entire canvas content.
Parameters:
direction: The direction to search for empty space relative to the node
filePath: An optional file path to access a .pen file.
height: The height of the required empty spacenodeld: Optional starting point node lD to find space around. lf omitted, the empty space will be
found around the canvas content.
padding: The minimum padding distance from other element
width: The width of the required empty space

✅ search_all_unique_properties() - 搜索属性

Recursively search for all unique properties on the entire node tree on provided parent ids
Parameters:
filePath: An optional file path to access a .pen file.
parents:IDs of all parent nodes to search
properties:List of properties to search for

✅ replace_all_matching_properties() - 批量替换属性

Recursively replace all matching properties on the entire node tree on provided parent ids.
Parameters:
filePath: An optional file path to access a .pen file.
parents:lDs of all parent nodes to search
properties: List of replacements for each property.