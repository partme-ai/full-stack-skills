# CRUD API | CRUD API

## API Reference

Avue CRUD component API reference.

### Component Props

**Data:**
- `option`: CRUD configuration object (required)
- `data`: Table data array (required)
- `page`: Pagination object
- `loading`: Loading state

**Display:**
- `height`: Table height
- `maxHeight`: Maximum table height
- `stripe`: Stripe style
- `border`: Show border

### Component Events

**CRUD Operations:**
- `@row-save`: Emitted when row is saved (row, done)
- `@row-update`: Emitted when row is updated (row, index, done)
- `@row-del`: Emitted when row is deleted (row, index)

**Data Loading:**
- `@on-load`: Emitted when data should be loaded (page)
- `@refresh-change`: Emitted when refresh button is clicked

**Search:**
- `@search-change`: Emitted when search changes (params, done)
- `@search-reset`: Emitted when search is reset

**Selection:**
- `@selection-change`: Emitted when selection changes (selection)

**Export:**
- `@excel`: Emitted when export button is clicked

**Other:**
- `@current-change`: Emitted when current row changes
- `@size-change`: Emitted when page size changes
- `@current-page-change`: Emitted when current page changes

### Option Configuration

**Table Display:**
- `border`: Show border (boolean)
- `index`: Show index (boolean)
- `indexLabel`: Index label (string)
- `stripe`: Stripe style (boolean)
- `size`: Table size (string: medium/small/mini)
- `height`: Table height (string/number)
- `maxHeight`: Maximum height (string/number)

**Buttons:**
- `addBtn`: Show add button (boolean)
- `editBtn`: Show edit button (boolean)
- `delBtn`: Show delete button (boolean)
- `viewBtn`: Show view button (boolean)
- `searchBtn`: Show search button (boolean)
- `refreshBtn`: Show refresh button (boolean)
- `columnBtn`: Show column button (boolean)
- `excelBtn`: Show excel button (boolean)
- `printBtn`: Show print button (boolean)

**Pagination:**
- `page`: Enable pagination (boolean)
- `pageSize`: Default page size (number)
- `pageSizes`: Page size options (array)

**Search:**
- `searchMenuSpan`: Search form span (number)
- `searchSize`: Search form size (string)
- `searchIcon`: Show search icon (boolean)

**Form:**
- `dialogType`: Dialog type (string: drawer/dialog)
- `dialogWidth`: Dialog width (string)
- `dialogHeight`: Dialog height (string)
- `formOption`: Form configuration object

**Column:**
- `column`: Column configuration array (required)

### Key Points

- option object contains all configuration
- column array defines table columns
- Handle events for CRUD operations
- Use page object for pagination
- Use data array for table data
- All configuration is data-driven
