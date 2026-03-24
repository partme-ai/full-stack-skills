# Components API | 组件 API

## API Reference

Avue component APIs and props.

### avue-form API

**Props:**
- `option`: Form configuration object
- `v-model`: Form data binding
- `disabled`: Disable form
- `readonly`: Readonly form

**Events:**
- `@submit`: Form submission
- `@reset`: Form reset
- `@change`: Form change

**Option Properties:**
- `column`: Column configuration array
- `labelWidth`: Label width
- `labelPosition`: Label position
- `menuBtn`: Show menu buttons
- `submitBtn`: Show submit button
- `emptyBtn`: Show empty button

### avue-crud API

**Props:**
- `option`: Table configuration object
- `data`: Table data array
- `page`: Pagination object
- `loading`: Loading state

**Events:**
- `@row-save`: Row save event
- `@row-update`: Row update event
- `@row-del`: Row delete event
- `@on-load`: Load data event
- `@search-change`: Search change event

**Option Properties:**
- `column`: Column configuration array
- `border`: Show border
- `index`: Show index
- `stripe`: Stripe style
- `addBtn`: Show add button
- `editBtn`: Show edit button
- `delBtn`: Show delete button
- `searchBtn`: Show search button
- `refreshBtn`: Show refresh button

### avue-tree API

**Props:**
- `option`: Tree configuration object
- `data`: Tree data array

**Events:**
- `@node-click`: Node click event
- `@check-change`: Check change event

**Option Properties:**
- `props`: Tree props configuration
- `defaultExpandAll`: Expand all by default
- `showCheckbox`: Show checkbox
- `checkStrictly`: Strict check mode

### Column Configuration

**Common Properties:**
- `label`: Column label
- `prop`: Column property
- `type`: Input type
- `rules`: Validation rules
- `disabled`: Disable field
- `readonly`: Readonly field
- `dicData`: Dictionary data
- `span`: Column span

### Key Points

- All components use option object for configuration
- Column array defines form/table fields
- Use type prop for different input types
- Use rules for validation
- Events handle user interactions
- Data-driven configuration approach
