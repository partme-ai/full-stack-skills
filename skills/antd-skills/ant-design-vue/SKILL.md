---
name: ant-design-vue
description: Provides comprehensive guidance for Ant Design Vue (AntDV) component library for Vue 3. Covers installation, usage, API reference, templates, and all component categories. Use when building enterprise-class UI with Vue 3 and Ant Design.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- "Ant Design Vue", "AntDV", "Ant Design of Vue"
- Building Vue 3 applications with Ant Design
- Using UI components like Button, Table, Form, Modal, Menu in a Vue context
- "Ant Design Vue 4.x", "AntDV 4"
- Requests to "implement a [component] with Ant Design Vue"
- Requests for Ant Design Vue API or configuration

## How to use this skill

This skill is organized to match the Ant Design Vue official documentation structure.

### 1. Identify the User's Need

- **Getting Started/Setup** → `examples/getting-started/installation.md` or `templates/project-setup.md`
- **Component Usage** → See Component Categories below
- **API Reference** → `api/components.md` or `api/config-provider.md`
- **Theme/i18n** → `examples/advanced/`
- **Templates** → `templates/component-template.md`

### 2. Component Categories (One-to-One Mapping)

**通用 (General)**
- **Contains**: Button, Icon, Typography
- **File**: `examples/components/general.md`

**布局 (Layout)**
- **Contains**: Divider, Grid, Layout, Space
- **File**: `examples/components/layout.md`

**导航 (Navigation)**
- **Contains**: Anchor, Breadcrumb, Dropdown, Menu, Pagination, Steps
- **File**: `examples/components/navigation.md`

**数据录入 (Data Entry)**
- **Contains**: AutoComplete, Cascader, Checkbox, DatePicker, Form, Input, InputNumber, Mentions, Radio, Rate, Select, Slider, Switch, TimePicker, Transfer, TreeSelect, Upload
- **File**: `examples/components/data-entry.md`

**数据展示 (Data Display)**
- **Contains**: Avatar, Badge, Calendar, Card, Carousel, Collapse, Descriptions, Empty, Image, List, Popover, QRCode, Segmented, Statistic, Table, Tabs, Tag, Timeline, Tooltip, Tour, Tree
- **File**: `examples/components/data-display.md`

**反馈 (Feedback)**
- **Contains**: Alert, Drawer, Message, Modal, Notification, Popconfirm, Progress, Result, Skeleton, Spin, Watermark
- **File**: `examples/components/feedback.md`

**其他 (Other)**
- **Contains**: Affix, App, BackTop, ConfigProvider, FloatButton
- **File**: `examples/components/other.md`

### 3. API & Advanced Topics

- **Components API**: `api/components.md` (Props, Events for common components)
- **ConfigProvider API**: `api/config-provider.md` (Global config, Theme)
- **Theme Customization**: `examples/advanced/theme-customization.md` (Design Token)
- **Internationalization**: `examples/advanced/internationalization.md`

### 4. Templates

- **Component Templates**: `templates/component-template.md` (Basic, Form, Modal patterns)
- **Project Setup**: `templates/project-setup.md` (Vite, Main.ts, App.vue setup)
