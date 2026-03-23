# Columns API

## API Reference

Avue-form columns configuration API.

### Common Column Properties

**label**
- Type: `String`
- Required: `true`
- Description: Field label

**prop**
- Type: `String`
- Required: `true`
- Description: Field property name

**type**
- Type: `String`
- Required: `true`
- Description: Field type (input, select, date, etc.)

**span**
- Type: `Number`
- Default: `24`
- Description: Column span (1-24)

**offset**
- Type: `Number`
- Default: `0`
- Description: Column offset

**order**
- Type: `Number`
- Default: `0`
- Description: Column order

**display**
- Type: `Boolean`
- Default: `true`
- Description: Display column

**disabled**
- Type: `Boolean`
- Default: `false`
- Description: Disable field

**readonly**
- Type: `Boolean`
- Default: `false`
- Description: Readonly field

**rules**
- Type: `Array`
- Description: Validation rules

### Column Types

**input** - Text input
**textarea** - Textarea
**select** - Select dropdown
**date** - Date picker
**time** - Time picker
**datetime** - DateTime picker
**switch** - Switch toggle
**radio** - Radio button
**checkbox** - Checkbox
**number** - Number input
**rate** - Rate component
**upload** - File upload
**tree** - Tree selector
**map** - Map selector
**color** - Color picker
**icon** - Icon selector

### Type-Specific Properties

Each column type has specific properties. See column type examples for details.

**See also:** `examples/components/columns.md` for detailed examples
