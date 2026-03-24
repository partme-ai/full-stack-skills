# Vant 4 Component Index (with official doc links)

**Use framework components when available; do not replace with generic div/span + custom class.** Use **van-cell-group** (inset) for card-like sections, **van-cell** for rows, **van-field** for form hints. When generating pages **prefer van-\* components from this table**; avoid raw `<button>`, `<input>`, or `<div class="card">` when a Vant component exists. Official (en-US): https://vant-ui.github.io/vant/#/en-US/home

Each component links to its official doc (Doc column). Base: https://vant-ui.github.io/vant/#/en-US/

| Component | Tag | Doc |
|-----------|-----|-----|
| Button | `<van-button type="primary" size="large">` | [button](https://vant-ui.github.io/vant/#/en-US/button) |
| Cell | `<van-cell title="Title" value="Value" is-link />` | [cell](https://vant-ui.github.io/vant/#/en-US/cell) |
| Cell Group | `<van-cell-group>`, `<van-cell-group inset>` | [cell](https://vant-ui.github.io/vant/#/en-US/cell) |
| Icon | `<van-icon name="chat-o" />` | [icon](https://vant-ui.github.io/vant/#/en-US/icon) |
| Image | `<van-image width="100" height="100" src="..." radius="4">` | [image](https://vant-ui.github.io/vant/#/en-US/image) |
| Row / Col | `<van-row>`, `<van-col span="12">` | [col](https://vant-ui.github.io/vant/#/en-US/col) |
| Form | `<van-form @submit="onSubmit">` | [form](https://vant-ui.github.io/vant/#/en-US/form) |
| Field | `<van-field v-model="value" label="Label" :rules="[...]">` | [field](https://vant-ui.github.io/vant/#/en-US/field) |
| Search | `<van-search v-model="value" placeholder="Search">` | [search](https://vant-ui.github.io/vant/#/en-US/search) |
| Checkbox | `<van-checkbox v-model="checked">` | [checkbox](https://vant-ui.github.io/vant/#/en-US/checkbox) |
| Radio | `<van-radio-group v-model="val">` + `<van-radio name="1">` | [radio](https://vant-ui.github.io/vant/#/en-US/radio) |
| Picker | `<van-picker :columns="columns" @confirm="onConfirm">` | [picker](https://vant-ui.github.io/vant/#/en-US/picker) |
| Popup | `<van-popup v-model:show="show" position="bottom">` | [popup](https://vant-ui.github.io/vant/#/en-US/popup) |
| NavBar | `<van-nav-bar title="Title" left-arrow left-text="Back">` | [nav-bar](https://vant-ui.github.io/vant/#/en-US/nav-bar) |
| Tabbar | `<van-tabbar v-model="active">` + `<van-tabbar-item>` | [tabbar](https://vant-ui.github.io/vant/#/en-US/tabbar) |
| Tabs | `<van-tabs v-model="active">` + `<van-tab title="...">` | [tab](https://vant-ui.github.io/vant/#/en-US/tab) |
| Sidebar | `<van-sidebar>`, `<van-sidebar-item>` | [sidebar](https://vant-ui.github.io/vant/#/en-US/sidebar) |
| ActionSheet | `<van-action-sheet v-model:show="show" :actions="actions">` | [action-sheet](https://vant-ui.github.io/vant/#/en-US/action-sheet) |
| Empty | `<van-empty description="No Data">` | [empty](https://vant-ui.github.io/vant/#/en-US/empty) |
| Dialog | `showConfirmDialog`, `<van-dialog>` | [dialog](https://vant-ui.github.io/vant/#/en-US/dialog) |
| Toast | `showToast('...')` | [toast](https://vant-ui.github.io/vant/#/en-US/toast) |
| SwipeCell | `<van-swipe-cell>` for list item actions | [swipe-cell](https://vant-ui.github.io/vant/#/en-US/swipe-cell) |
| Card | `<van-card num="2" price="2.00" title="..." thumb="...">` | [card](https://vant-ui.github.io/vant/#/en-US/card) |
| SubmitBar | `<van-submit-bar :price="3050" button-text="Submit" @submit="onSubmit">` | [submit-bar](https://vant-ui.github.io/vant/#/en-US/submit-bar) |
| ConfigProvider | `<van-config-provider>` | [config-provider](https://vant-ui.github.io/vant/#/en-US/config-provider) |

## Design element → Component mapping (MUST use these)

| What you see in design | Use component | Do not use |
|------------------------|---------------|------------|
| Card / section block | **van-cell-group** (inset) + **van-cell** | div.card + custom header/title |
| Form row with label/hint | **van-field** (label, placeholder, rules) | raw input + span.tips |
| Product card | **van-card** (thumb, title, price, desc) | custom product div |
| Button, Tabs, NavBar, etc. | van-button, van-tabs, van-nav-bar, etc. | raw button, div tabs |

Consult this table and [contract.md](contract.md) when mapping Stitch HTML to Vant 4 components.
