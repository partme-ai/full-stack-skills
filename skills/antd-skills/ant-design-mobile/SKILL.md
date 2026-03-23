---
name: ant-design-mobile
description: Provides comprehensive guidance for Ant Design Mobile component library including mobile components, themes, and platform adaptations. Use when the user asks about Ant Design Mobile, needs to build mobile applications, or implement mobile UI components.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build React mobile applications with Ant Design Mobile components
- Use mobile UI components (Button, Input, Form, List, Card, Modal, etc.)
- Create mobile-friendly interfaces
- Customize Ant Design Mobile theme
- Implement mobile-specific features (pull-to-refresh, infinite scroll, etc.)
- Use Ant Design Mobile with React Native or web
- Handle mobile gestures and interactions
- Implement mobile navigation patterns
- Use mobile form components
- Create mobile data display components

## How to use this skill

This skill is organized to match the Ant Design Mobile official documentation structure (https://ant-design-mobile.antgroup.com/zh/guide/quick-start, https://ant-design-mobile.antgroup.com/zh/components/button). When working with Ant Design Mobile:

1. **Install and setup** Ant Design Mobile:
   - Load `examples/getting-started/installation.md` for installation instructions
   - Load `examples/getting-started/basic-usage.md` for basic usage examples

2. **Choose the component** based on the user's requirements:
   - Button/按钮 → `examples/components/button.md`
   - Input/输入框 → `examples/components/input.md`
   - Form/表单 → `examples/components/form.md`
   - List/列表 → `examples/components/list.md`
   - Card/卡片 → `examples/components/card.md`
   - Modal/对话框 → `examples/components/modal.md`
   - Picker/选择器 → `examples/components/picker.md`
   - DatePicker/日期选择器 → `examples/components/date-picker.md`
   - Tabs/标签页 → `examples/components/tabs.md`
   - PullToRefresh/下拉刷新 → `examples/components/pull-to-refresh.md`
   - InfiniteScroll/无限滚动 → `examples/components/infinite-scroll.md`
   - And many more components...

3. **Load the appropriate example file** from the `examples/` directory:
   - `examples/getting-started/installation.md` - Installation and setup
   - `examples/getting-started/basic-usage.md` - Basic usage examples
   - `examples/components/button.md` - Button component
   - `examples/components/input.md` - Input component
   - `examples/components/form.md` - Form component
   - `examples/components/list.md` - List component
   - `examples/components/card.md` - Card component
   - `examples/components/modal.md` - Modal component
   - `examples/components/picker.md` - Picker component
   - `examples/components/date-picker.md` - DatePicker component
   - `examples/components/tabs.md` - Tabs component
   - `examples/components/pull-to-refresh.md` - PullToRefresh component
   - `examples/components/infinite-scroll.md` - InfiniteScroll component
   - `examples/components/icon.md` - Icon component
   - `examples/components/badge.md` - Badge component
   - `examples/components/tag.md` - Tag component
   - `examples/components/avatar.md` - Avatar component
   - `examples/components/image.md` - Image component
   - `examples/components/image-viewer.md` - ImageViewer component
   - `examples/components/nav-bar.md` - NavBar component
   - `examples/components/tab-bar.md` - TabBar component
   - `examples/components/index-bar.md` - IndexBar component
   - `examples/components/side-bar.md` - SideBar component
   - `examples/components/dialog.md` - Dialog component
   - `examples/components/toast.md` - Toast component
   - `examples/components/action-sheet.md` - ActionSheet component
   - `examples/components/popup.md` - Popup component
   - `examples/components/loading.md` - Loading component
   - `examples/components/error-block.md` - ErrorBlock component
   - `examples/components/empty.md` - Empty component
   - `examples/components/notice-bar.md` - NoticeBar component
   - `examples/components/mask.md` - Mask component
   - `examples/components/textarea.md` - Textarea component
   - `examples/components/switch.md` - Switch component
   - `examples/components/checkbox.md` - Checkbox component
   - `examples/components/radio.md` - Radio component
   - `examples/components/stepper.md` - Stepper component
   - `examples/components/rate.md` - Rate component
   - `examples/components/slider.md` - Slider component
   - `examples/components/uploader.md` - Uploader component
   - `examples/components/grid.md` - Grid component
   - `examples/components/swiper.md` - Swiper component
   - `examples/components/cascader.md` - Cascader component
   - `examples/components/search-bar.md` - SearchBar component
   - `examples/components/virtual-input.md` - VirtualInput component
   - `examples/components/divider.md` - Divider component
   - `examples/components/space.md` - Space component
   - `examples/components/safe-area.md` - SafeArea component
   - `examples/advanced/theme-customization.md` - Theme customization
   - `examples/advanced/internationalization.md` - Internationalization

4. **Follow the specific instructions** in that example file for syntax, structure, and best practices

5. **Reference the API documentation** when needed:
   - `api/components.md` - Component API reference
   - `api/config-provider.md` - ConfigProvider API

6. **Use templates** for quick start:
   - `templates/project-setup.md` - Project setup templates
   - `templates/component-template.md` - Component usage templates


### Doc mapping (one-to-one with official documentation)

**Guide (指南)**:
- See guide files in `examples/guide/` or `examples/getting-started/` → https://ant-design-mobile.antgroup.com/zh/guide/quick-start

**Components (组件)**:
- See component files in `examples/components/` → https://ant-design-mobile.antgroup.com/zh/components/button

## Examples and Templates

This skill includes detailed examples organized to match the official documentation structure. All examples are in the `examples/` directory (see mapping above).

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the mapping above
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference templates in `templates/` directory for common scaffolding
- Adapt templates to your specific needs and coding style

## API Reference

- **Components API**: `api/components.md` - All component props and APIs
- **ConfigProvider API**: `api/config-provider.md` - ConfigProvider component API and global configuration

## Best Practices

1. **Import styles**: Import Ant Design Mobile CSS in your entry file
2. **Use ConfigProvider**: Wrap your app with ConfigProvider for global configuration
3. **Mobile-first**: Design for mobile devices first
4. **Touch interactions**: Consider touch gestures and interactions
5. **Performance**: Optimize for mobile performance
6. **Responsive design**: Test on different screen sizes
7. **Accessibility**: Follow mobile accessibility guidelines
8. **Theme customization**: Use design tokens for consistent theming
9. **Internationalization**: Use ConfigProvider with locale for i18n
10. **Component composition**: Compose components for complex UIs

## Resources

- **Official Website**: https://ant-design-mobile.antgroup.com/
- **Getting Started**: https://ant-design-mobile.antgroup.com/zh/guide/quick-start
- **Components**: https://ant-design-mobile.antgroup.com/zh/components/button
- **GitHub Repository**: https://github.com/ant-design/ant-design-mobile

## Keywords

Ant Design Mobile, antd-mobile, mobile UI, React mobile, mobile components, Button, Input, Form, List, Card, Modal, Picker, DatePicker, Tabs, PullToRefresh, InfiniteScroll, Swiper, Toast, Dialog, ActionSheet, Popup, Loading, NavBar, TabBar, Icon, Badge, Tag, Avatar, Image, ImageViewer, Switch, Checkbox, Radio, Stepper, Rate, Slider, Uploader, Grid, Cascader, SearchBar, VirtualInput, Divider, Space, SafeArea, ErrorBlock, Empty, NoticeBar, Mask, mobile app, 移动端, 组件库, 按钮, 输入框, 表单, 列表, 卡片, 对话框, 选择器, 日期选择器, 标签页, 下拉刷新, 无限滚动
