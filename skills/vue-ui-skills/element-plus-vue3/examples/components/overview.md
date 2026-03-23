# Components Overview

**官方文档**: https://element-plus.org/en-US/component/overview.html


## Instructions

This example provides an overview of Element Plus components.

### Key Concepts

- Component categories
- Component list
- Component usage
- Component features

### Example: Component Categories

**Basic Components (基础组件)**:
- Button, Link, Icon

**Form Components (表单组件)**:
- Input, Textarea, Select, Switch, Checkbox, Radio, DatePicker, TimePicker, Upload, Rate, ColorPicker, Transfer, Form

**Data Display (数据展示)**:
- Table, Tag, Progress, Tree, Pagination, Badge, Avatar, Skeleton, Empty, Descriptions, Result, Statistic

**Navigation (导航)**:
- NavMenu, Tabs, Breadcrumb, PageHeader, Affix, Backtop

**Feedback (反馈)**:
- Alert, Loading, Message, MessageBox, Notification, Popover, Tooltip, Popconfirm, Drawer, Dialog

**Layout (布局)**:
- Row, Col, Container, Aside, Main, Header, Footer

**Others (其他)**:
- Divider, Calendar, Image, Timeline, Card, Carousel, Collapse, InfiniteScroll

### Example: Component Registration

```javascript
// Full import
import ElementPlus from 'element-plus'
app.use(ElementPlus)

// On-demand import
import { ElButton, ElInput } from 'element-plus'
app.component(ElButton.name, ElButton)
app.component(ElInput.name, ElInput)
```

### Key Points

- 60+ components available
- Organized by category
- Support full import and on-demand import
- TypeScript support
- Consistent API design
