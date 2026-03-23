# Examples

## PENCIL_PLAN example

Step 1: open_document(filePathOrTemplate: 'new')
Step 2: set_variables(variables: { ucharts-color-1: '#1890ff', ... }, replace: false)
Step 3: batch_design(operations: "root=I(document, { type: 'frame', layout: 'vertical', name: 'Charts Overview' }) ...")
Step 4: get_screenshot(nodeId: <root-id>)
