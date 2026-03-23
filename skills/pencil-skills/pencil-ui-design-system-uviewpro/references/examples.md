# Examples

## PENCIL_PLAN example

Step 1: open_document(filePathOrTemplate: 'new')
Step 2: get_editor_state(include_schema: false)
Step 3: set_variables(variables: { u-type-primary: '#2979ff', ... }, replace: false)
Step 4: batch_design(operations: "root=I(document, { type: 'frame', layout: 'vertical', name: 'Components Overview' }) ...")
Step 5: get_screenshot(nodeId: <root-id>)
