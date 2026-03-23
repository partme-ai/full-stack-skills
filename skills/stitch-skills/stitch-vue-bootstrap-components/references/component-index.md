# Bootstrap Vue Component Index (with official doc links)

**Use framework components when available; do not replace with generic div/span + custom class.** Use **b-card** for cards, **b-alert** for tips/notices. When generating pages **prefer b-\* components from this table**; avoid raw `<button class="btn">` or `<div class="card">` when a Bootstrap Vue component exists. Official docs: https://bootstrap-vue.org/docs

Each component links to its official doc (Doc column). Base: https://bootstrap-vue.org/docs/components/

| Component | Tag | Doc |
|-----------|-----|-----|
| Button | `<b-button variant="primary">` | [button](https://bootstrap-vue.org/docs/components/button) |
| Button Group | `<b-button-group>` | [button-group](https://bootstrap-vue.org/docs/components/button-group) |
| Container | `<b-container>`, `<b-container fluid>` | [layout](https://bootstrap-vue.org/docs/components/layout) |
| Row / Col | `<b-row>`, `<b-col cols="12" md="6">` | [layout](https://bootstrap-vue.org/docs/components/layout) |
| Form | `<b-form @submit.prevent="onSubmit">` | [form](https://bootstrap-vue.org/docs/components/form) |
| Form Group | `<b-form-group label="..." label-for="...">` | [form-group](https://bootstrap-vue.org/docs/components/form-group) |
| Form Input | `<b-form-input v-model="val" type="text">` | [form-input](https://bootstrap-vue.org/docs/components/form-input) |
| Form Select | `<b-form-select v-model="sel" :options="options">` | [form-select](https://bootstrap-vue.org/docs/components/form-select) |
| Form Checkbox | `<b-form-checkbox v-model="checked">` | [form-checkbox](https://bootstrap-vue.org/docs/components/form-checkbox) |
| Table | `<b-table :items="items" :fields="fields">` | [table](https://bootstrap-vue.org/docs/components/table) |
| Card | `<b-card title="..." sub-title="...">` | [card](https://bootstrap-vue.org/docs/components/card) |
| Alert | `<b-alert show variant="info">` | [alert](https://bootstrap-vue.org/docs/components/alert) |
| Modal | `<b-modal v-model="show" title="...">` | [modal](https://bootstrap-vue.org/docs/components/modal) |
| Nav | `<b-nav>`, `<b-nav-item>` | [nav](https://bootstrap-vue.org/docs/components/nav) |
| Tabs | `<b-tabs>`, `<b-tab title="...">` | [tabs](https://bootstrap-vue.org/docs/components/tabs) |
| Badge | `<b-badge variant="primary">` | [badge](https://bootstrap-vue.org/docs/components/badge) |
| Spinner | `<b-spinner>` | [spinner](https://bootstrap-vue.org/docs/components/spinner) |
| Icons | Bootstrap Icons (e.g. icon pack) | [icons](https://bootstrap-vue.org/docs/icons) |

## Design element → Component mapping (MUST use these)

| What you see in design | Use component | Do not use |
|------------------------|---------------|------------|
| Card / section block | **b-card** (title, sub-title, b-card-text) | div.card + custom header/title |
| Tips / notice text | **b-alert** (variant="info"|warning|success) | div + .tips-text / .alert custom class |
| Form label + hint | **b-form-group** label + description | raw label + span.hint |
| Button, Table, Form, etc. | b-button, b-table, b-form-* | raw button, table, input |

Vue 3 support: https://bootstrap-vue.org/vue3. Consult this table and [contract.md](contract.md) when mapping Stitch HTML to Bootstrap Vue components.
