# Vant (Vue 3) Official References

- **Official**: https://vant-ui.github.io/
- **Guide / Components (en-US)**: https://vant-ui.github.io/vant/#/en-US/home
- **GitHub**: https://github.com/youzan/vant

## Per-component doc links (each component → official doc)

Base URL: `https://vant-ui.github.io/vant/#/en-US/`

| Component | Doc |
|-----------|-----|
| Button | https://vant-ui.github.io/vant/#/en-US/button |
| Cell / Cell Group | https://vant-ui.github.io/vant/#/en-US/cell |
| Icon | https://vant-ui.github.io/vant/#/en-US/icon |
| Image | https://vant-ui.github.io/vant/#/en-US/image |
| Layout (Row, Col) | https://vant-ui.github.io/vant/#/en-US/col |
| Form | https://vant-ui.github.io/vant/#/en-US/form |
| Field | https://vant-ui.github.io/vant/#/en-US/field |
| Search | https://vant-ui.github.io/vant/#/en-US/search |
| Checkbox | https://vant-ui.github.io/vant/#/en-US/checkbox |
| Radio | https://vant-ui.github.io/vant/#/en-US/radio |
| Picker | https://vant-ui.github.io/vant/#/en-US/picker |
| Popup | https://vant-ui.github.io/vant/#/en-US/popup |
| NavBar | https://vant-ui.github.io/vant/#/en-US/nav-bar |
| Tabbar | https://vant-ui.github.io/vant/#/en-US/tabbar |
| Tabs | https://vant-ui.github.io/vant/#/en-US/tab |
| Sidebar | https://vant-ui.github.io/vant/#/en-US/sidebar |
| ActionSheet | https://vant-ui.github.io/vant/#/en-US/action-sheet |
| Empty | https://vant-ui.github.io/vant/#/en-US/empty |
| Dialog | https://vant-ui.github.io/vant/#/en-US/dialog |
| Toast | https://vant-ui.github.io/vant/#/en-US/toast |
| SwipeCell | https://vant-ui.github.io/vant/#/en-US/swipe-cell |
| Card | https://vant-ui.github.io/vant/#/en-US/card |
| SubmitBar | https://vant-ui.github.io/vant/#/en-US/submit-bar |
| ConfigProvider | https://vant-ui.github.io/vant/#/en-US/config-provider |

Full table with tags: [component-index.md](component-index.md).

## Usage in This Skill

1. Map Stitch HTML to Vant 4 components (`van-button`, `van-field`, `van-nav-bar`, `van-tabbar`, `van-cell-group`, etc.) per [references/contract.md](contract.md).
2. Design for mobile-first (375px base); respect safe area; use Vant design tokens (primary #1989fa, page bg #f7f8fa).
3. Prefer `van-*` components over raw HTML for forms, navigation, and lists.
