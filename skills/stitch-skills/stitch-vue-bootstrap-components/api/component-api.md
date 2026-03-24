# Bootstrap Vue Component API (Stitch conversion reference)

Aligned with [full-stack-skills/bootstrap-vue3](https://github.com/partme-ai/full-stack-skills/tree/main/skills/bootstrap-vue3) and official docs. Use for precise Stitch HTML → Vue SFC mapping.

## Common conventions

- Components: kebab-case `<b-button>`, `<b-container>` or PascalCase `<BButton>`, `<BContainer>` (per project registration).
- Common props: variant, size, disabled, class.

## Button

| Use | Syntax | Notes |
|-----|--------|-------|
| Variant | `<b-button variant="primary">` | primary, success, danger, warning, info, light, dark |
| Size | `size="sm" \| default \| lg"` | sm / default / lg |
| Disabled | `disabled` | boolean |
| Type | `type="button" \| submit \| reset"` | use submit for form submit |
| Click | `@click="handler"` | event |
| Group | `<b-button-group>` wrapping multiple `<b-button>` | button group |

Do not use `<button class="btn btn-primary">`; use `<b-button>` only.

## Grid

| Use | Syntax | Notes |
|-----|--------|-------|
| Container | `<b-container>` or `<b-container fluid>` | fluid = full width |
| Row | `<b-row>` | children are `<b-col>` |
| Col | `<b-col cols="12" md="6" lg="4">` | cols required; md/lg/xl/xxl responsive |
| Offset | `<b-col offset="4">` | column offset |
| Align | `<b-row align-v="center" align-h="center">` | vertical / horizontal align |

Responsive first: define mobile `cols="12"` then override with `md="6"`, `lg="4"` etc.

## Form

| Use | Syntax | Notes |
|-----|--------|-------|
| Input | `<b-form-input v-model="val" type="email" placeholder="..." />` | type: text, email, password, number |
| Label+input | `<b-form-group label="Email" label-for="email">` + `<b-form-input id="email" />` | pair for accessibility |
| Select | `<b-form-select v-model="sel" :options="options">` | options: [{ value, text }, ...] |
| Checkbox | `<b-form-checkbox v-model="checked">` | multi: `<b-form-checkbox-group>` |
| Submit/Reset | `<b-button type="submit">` / `type="reset"` | inside `<b-form @submit.prevent="onSubmit">` |

Events: @submit, @reset; form fields use v-model.

## Table

| Use | Syntax | Notes |
|-----|--------|-------|
| Table | `<b-table :items="items" :fields="fields" striped hover>` | items = data array, fields = column defs |
| Fields | `fields: [{ key: 'name', label: 'Name' }, { key: 'age', label: 'Age' }]` | or omit label, key used as header |
| Row select | `selectable`, `select-mode="multi"`, `v-model:selected="selected"` | row selection |
| Sort | `sortable` | column sortable |

Do not hand-write `<thead>`/`<tbody>`; use items + fields.

## Card

| Use | Syntax | Notes |
|-----|--------|-------|
| Basic | `<b-card title="Title">` | title optional |
| Image | `<b-card img-src="..." img-top>` | image on top |
| Body | `<b-card-text>` or default slot | body content |
| Footer button | `<b-button variant="primary">` inside `<b-card>` | inside card |

## Modal

| Use | Syntax | Notes |
|-----|--------|-------|
| Show | `<b-modal v-model="visible" title="Title" @ok="onOk" @cancel="onCancel">` | v-model controls visibility |
| Size | `size="sm" \| lg \| xl"` | modal width |
| Methods | `ref.show()` / `ref.hide()` | via ref |

## References

- [references/contract.md](../references/contract.md) — design tokens and mapping rules
- [references/official.md](../references/official.md) — official docs
