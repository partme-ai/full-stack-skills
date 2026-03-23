# Layout Components (布局)

## Divider (分割线)
A divider line separates different content.

```vue
<a-divider />
<a-divider>With Text</a-divider>
<a-divider type="vertical" />
```

## Grid (栅格)
24 Grids System.

```vue
<a-row>
  <a-col :span="12">col-12</a-col>
  <a-col :span="12">col-12</a-col>
</a-row>
<a-row :gutter="16">
  <a-col :span="8">col-8</a-col>
  <a-col :span="8">col-8</a-col>
  <a-col :span="8">col-8</a-col>
</a-row>
```

## Layout (布局)
Handling the overall layout of a page.

```vue
<a-layout>
  <a-layout-header>Header</a-layout-header>
  <a-layout-content>Content</a-layout-content>
  <a-layout-footer>Footer</a-layout-footer>
</a-layout>
```

## Space (间距)
Set components spacing.

```vue
<a-space>
  <a-button>Button</a-button>
  <a-button>Button</a-button>
</a-space>
```
