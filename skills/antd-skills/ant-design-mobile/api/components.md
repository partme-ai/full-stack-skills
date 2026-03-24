# Components API | 组件 API

## API Reference

Complete Ant Design Mobile component APIs and props reference.

### Common Props

Most components share common props:

- `className`: Additional CSS class
- `style`: Inline style object
- `disabled`: Disabled state
- `loading`: Loading state

### General Components

#### Button API

**Props:**
- `color`: Button color (primary, success, warning, danger, default)
- `size`: Button size (large, middle, small, mini)
- `fill`: Button fill style (solid, outline, none)
- `block`: Full-width button
- `loading`: Loading state
- `disabled`: Disabled state
- `onClick`: Click handler

#### Icon API

**Props:**
- `fontSize`: Icon size
- `color`: Icon color
- Children: Icon component from `antd-mobile-icons`

#### Badge API

**Props:**
- `content`: Badge content (number or string)
- `dot`: Show as dot
- `color`: Badge color
- `position`: Badge position (top-right, bottom-right, etc.)
- `max`: Maximum number to display

#### Tag API

**Props:**
- `color`: Tag color (default, primary, success, warning, danger)
- `size`: Tag size (small, middle, large)
- `round`: Rounded corners
- `closable`: Show close button
- `onClose`: Close handler
- `icon`: Tag icon

#### Avatar API

**Props:**
- `src`: Image URL
- `size`: Avatar size (small, middle, large)
- `shape`: Avatar shape (circle, square, rounded)
- `style`: Custom styles

#### Divider API

**Props:**
- `direction`: Divider direction (horizontal, vertical)
- `contentPosition`: Text position (left, center, right)
- Children: Divider text

#### Space API

**Props:**
- `direction`: Space direction (horizontal, vertical)
- `size`: Space size (small, middle, large)
- `wrap`: Wrap items

#### SafeArea API

**Props:**
- `position`: Safe area position (top, bottom, left, right)

### Data Entry Components

#### Input API

**Props:**
- `value`: Input value
- `defaultValue`: Default value
- `placeholder`: Placeholder text
- `type`: Input type (text, number, password, tel, etc.)
- `clearable`: Show clear button
- `prefix`: Prefix element
- `suffix`: Suffix element
- `error`: Error message
- `onChange`: Change handler (receives value)

#### Form API

**Props:**
- `form`: Form instance from Form.useForm()
- `onFinish`: Submit handler
- `onFinishFailed`: Failed submit handler
- `initialValues`: Initial form values

**Form.Item Props:**
- `name`: Field name
- `label`: Field label
- `rules`: Validation rules
- `required`: Required field
- `help`: Help text
- `error`: Error message

#### Textarea API

**Props:**
- `value`: Textarea value
- `defaultValue`: Default value
- `placeholder`: Placeholder text
- `maxLength`: Maximum length
- `showCount`: Show character count
- `autoSize`: Auto resize (object with minRows, maxRows)
- `onChange`: Change handler

#### Switch API

**Props:**
- `checked`: Switch state
- `defaultChecked`: Default state
- `disabled`: Disabled state
- `color`: Switch color
- `loading`: Loading state
- `onChange`: Change handler

#### Checkbox API

**Props:**
- `checked`: Checkbox state
- `defaultChecked`: Default state
- `disabled`: Disabled state
- `shape`: Checkbox shape (square, round)
- `onChange`: Change handler

**Checkbox.Group Props:**
- `value`: Selected values array
- `defaultValue`: Default selected values
- `onChange`: Change handler

#### Radio API

**Props:**
- `checked`: Radio state
- `defaultChecked`: Default state
- `disabled`: Disabled state
- `shape`: Radio shape (square, round)
- `onChange`: Change handler

**Radio.Group Props:**
- `value`: Selected value
- `defaultValue`: Default selected value
- `onChange`: Change handler

#### Stepper API

**Props:**
- `value`: Stepper value
- `defaultValue`: Default value
- `min`: Minimum value
- `max`: Maximum value
- `step`: Step increment
- `disabled`: Disabled state
- `formatter`: Value formatter function
- `onChange`: Change handler

#### Rate API

**Props:**
- `value`: Rate value
- `defaultValue`: Default value
- `count`: Star count
- `allowHalf`: Allow half star
- `readonly`: Readonly mode
- `character`: Custom character
- `onChange`: Change handler

#### Slider API

**Props:**
- `value`: Slider value
- `defaultValue`: Default value
- `min`: Minimum value
- `max`: Maximum value
- `step`: Step increment
- `marks`: Marks object
- `range`: Range mode
- `onChange`: Change handler

#### Uploader API

**Props:**
- `value`: File list
- `defaultValue`: Default file list
- `multiple`: Multiple files
- `maxCount`: Maximum file count
- `preview`: Show preview
- `upload`: Custom upload function
- `onChange`: Change handler

### Data Display Components

#### List API

**Props:**
- `mode`: List mode (default, card)
- `header`: List header
- `footer`: List footer

**List.Item Props:**
- `title`: Item title
- `description`: Item description
- `prefix`: Prefix element
- `extra`: Extra element
- `arrow`: Show arrow
- `onClick`: Click handler

#### Card API

**Props:**
- `title`: Card title
- `extra`: Extra content in header
- `bodyStyle`: Body styles
- `cover`: Card cover image
- `bordered`: Show border

#### Grid API

**Props:**
- `columns`: Column count
- `gap`: Gap between items

**Grid.Item Props:**
- `onClick`: Click handler

#### Image API

**Props:**
- `src`: Image URL
- `alt`: Alt text
- `width`: Image width
- `height`: Image height
- `lazy`: Lazy load
- `placeholder`: Loading placeholder
- `fallback`: Error fallback
- `preview`: Enable preview
- `fit`: Image fit mode (contain, cover, fill)

#### ImageViewer API

**Props:**
- `image`: Image URL or array of URLs
- `visible`: Visibility
- `defaultIndex`: Initial index
- `onIndexChange`: Index change handler
- `onClose`: Close handler
- `renderFooter`: Custom footer renderer

### Navigation Components

#### Tabs API

**Props:**
- `activeKey`: Active tab key
- `defaultActiveKey`: Default active key
- `onChange`: Tab change handler

**Tabs.Tab Props:**
- `key`: Tab key
- `title`: Tab title
- `disabled`: Disabled state

#### NavBar API

**Props:**
- `onBack`: Back button handler
- `left`: Left content
- `right`: Right content
- `style`: Custom styles
- Children: NavBar title

#### TabBar API

**Props:**
- `activeKey`: Active tab key
- `onChange`: Tab change handler

**TabBar.Item Props:**
- `key`: Tab key
- `icon`: Tab icon
- `title`: Tab title
- `badge`: Tab badge

#### IndexBar API

**Props:**
- `sticky`: Sticky header

**IndexBar.Panel Props:**
- `index`: Index value
- `title`: Section title

#### SideBar API

**Props:**
- `activeKey`: Active item key
- `onChange`: Item change handler

**SideBar.Item Props:**
- `key`: Item key
- `title`: Item title
- `badge`: Item badge

### Feedback Components

#### Modal API

**Props:**
- `visible`: Visibility
- `title`: Modal title
- `content`: Modal content
- `closeOnAction`: Close on action
- `actions`: Action buttons
- `onClose`: Close handler
- `onAction`: Action handler

**Static Methods:**
- `Modal.alert(options)`: Show alert
- `Modal.confirm(options)`: Show confirm
- `Modal.show(options)`: Show custom modal

#### Dialog API

Same as Modal API.

#### Toast API

**Static Methods:**
- `Toast.show(content | options)`: Show toast
- `Toast.clear()`: Clear toast

**Options:**
- `icon`: Toast icon (success, fail, loading)
- `content`: Toast content
- `duration`: Display duration (0 for infinite)

#### ActionSheet API

**Static Methods:**
- `ActionSheet.show(options)`: Show action sheet

**Options:**
- `actions`: Action options array
- `cancelText`: Cancel text
- `onAction`: Action handler

#### Popup API

**Props:**
- `visible`: Visibility
- `position`: Popup position (top, bottom, left, right, center)
- `mask`: Show mask
- `maskStyle`: Mask styles
- `showCloseButton`: Show close button
- `title`: Popup title
- `onMaskClick`: Mask click handler
- `onClose`: Close handler

#### Loading API

**Props:**
- `visible`: Visibility
- `mask`: Show mask
- `fullScreen`: Full screen loading
- Children: Loading text

#### ErrorBlock API

**Props:**
- `status`: Error status (default, network, busy, empty)
- `title`: Error title
- `description`: Error description
- `actions`: Action buttons

#### Empty API

**Props:**
- `title`: Empty title
- `description`: Empty description
- `image`: Custom image
- `actions`: Action buttons

#### NoticeBar API

**Props:**
- `content`: Notice content
- `icon`: Notice icon
- `closeable`: Show close button
- `onClose`: Close handler
- `extra`: Extra content
- `onExtraClick`: Extra click handler
- `wrap`: Text wrapping
- `color`: Notice color (default, alert)

#### Mask API

**Props:**
- `visible`: Visibility
- `opacity`: Mask opacity
- `disableBodyScroll`: Disable body scroll
- `onMaskClick`: Mask click handler

### Selector Components

#### Picker API

**Props:**
- `visible`: Visibility
- `value`: Selected value
- `defaultValue`: Default value
- `columns`: Picker columns
- `onConfirm`: Confirm handler
- `onCancel`: Cancel handler
- `onClose`: Close handler

#### DatePicker API

**Props:**
- `visible`: Visibility
- `value`: Selected date
- `defaultValue`: Default date
- `precision`: Date precision (year, month, day, hour, minute, second)
- `min`: Minimum date
- `max`: Maximum date
- `onConfirm`: Confirm handler
- `onCancel`: Cancel handler
- `onClose`: Close handler

#### Cascader API

**Props:**
- `visible`: Visibility
- `value`: Selected value array
- `defaultValue`: Default value array
- `options`: Cascader options
- `onConfirm`: Confirm handler
- `onCancel`: Cancel handler
- `onClose`: Close handler

#### SearchBar API

**Props:**
- `value`: Search value
- `defaultValue`: Default value
- `placeholder`: Placeholder text
- `showCancelButton`: Show cancel button
- `clearable`: Show clear button
- `onChange`: Change handler
- `onSearch`: Search handler
- `onCancel`: Cancel handler

### Other Components

#### Swiper API

**Props:**
- `autoplay`: Autoplay
- `loop`: Loop mode
- `indicator`: Custom indicator function
- `onIndexChange`: Index change handler

**Swiper.Item Props:**
- Children: Swiper item content

#### PullToRefresh API

**Props:**
- `onRefresh`: Refresh handler
- `canReleaseText`: Can release text
- `releaseText`: Release text
- `refreshingText`: Refreshing text
- `completeText`: Complete text

#### InfiniteScroll API

**Props:**
- `hasMore`: Has more data
- `loadMore`: Load more handler
- `threshold`: Load threshold

#### VirtualInput API

**Props:**
- `value`: Input value
- `defaultValue`: Default value
- `type`: Keyboard type (number, password, etc.)
- `placeholder`: Placeholder text
- `confirmText`: Confirm button text
- `onChange`: Change handler
- `onConfirm`: Confirm handler

### Key Points

- All components support `className` and `style` props
- Most form components support `value`, `defaultValue`, and `onChange`
- Modal-like components use `visible` prop for visibility control
- All components are optimized for mobile display
- Refer to individual component examples for detailed usage
