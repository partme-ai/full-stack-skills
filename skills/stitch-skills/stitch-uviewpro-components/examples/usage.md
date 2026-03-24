# stitch-uviewpro-components Usage

## When to use

- User has a Stitch screen and wants **uni-app + Vue 3 + uView Pro** pages/components that match the design.
- You need to download Stitch HTML reliably (use `scripts/fetch-stitch.sh` when web_fetch fails on GCS URLs).

## Steps

1. **Discover components**: Read [references/component-index.md](../references/component-index.md) so you use the right u-* (u-modal, u-popup, u-action-sheet, u-empty, u-avatar, u-picker, u-tabbar, etc.) instead of raw HTML.
2. Get projectId and screenId (e.g. via stitch-mcp-list-projects, stitch-mcp-list-screens).
3. Call Stitch MCP get_screen; get `htmlCode.downloadUrl`.
4. Run `bash scripts/fetch-stitch.sh "<url>" temp/source.html`.
5. Parse HTML; map to uView Pro (u-*) per references/contract.md and component-index.md; create pages using resources/page-template.vue and data/mockData.js.
6. Register pages in pages.json; verify against resources/architecture-checklist.md; run in HBuilderX or CLI.

## Example user prompt

> "Convert the Stitch login screen to a uni-app + uView Pro project."

---

## Example 1: Login page (u-form + u-input + u-button)

```vue
<template>
  <view class="page">
    <u-navbar title="Login" :autoBack="true"></u-navbar>
    <view class="content">
      <u-form :model="form" ref="uForm">
        <u-form-item label="Phone" prop="phone" borderBottom>
          <u-input v-model="form.phone" placeholder="Please input phone" border="none" type="number" maxlength="11" />
        </u-form-item>
        <u-form-item label="Code" prop="code" borderBottom>
          <u-input v-model="form.code" placeholder="Please input code" border="none" />
          <u-code :seconds="60" @end="codeEnd" @start="codeStart" ref="uCode"></u-code>
        </u-form-item>
      </u-form>
      <u-button type="primary" @click="submit" :loading="loading">Login</u-button>
    </view>
    <u-toast ref="uToast"></u-toast>
  </view>
</template>
<script setup lang="ts">
import { ref, reactive } from 'vue'
const uForm = ref(), uToast = ref(), uCode = ref()
const loading = ref(false)
const form = reactive({ phone: '', code: '' })
function submit() {
  uForm.value.validate().then(() => {
    loading.value = true
    // uni.$u.http.post('/login', form).then(...)
    uni.$u.toast('Login success')
    loading.value = false
  }).catch(() => uni.$u.toast('Please fill in'))
}
function codeStart() {}, function codeEnd() {}
</script>
<style lang="scss" scoped>
.page { padding: 32rpx; }
.content { margin-top: 48rpx; }
</style>
```

---

## Example 2: List with swipe + action sheet (u-swipe-action, u-action-sheet, u-empty)

```vue
<template>
  <view class="page">
    <u-navbar title="List" :autoBack="true"></u-navbar>
    <u-empty v-if="list.length === 0" text="No data" mode="data"></u-empty>
    <view v-else class="list">
      <u-swipe-action v-for="(item, i) in list" :key="item.id">
        <u-swipe-action-item :options="options" @click="onSwipeClick($event, item)">
          <u-cell :title="item.title" :value="item.desc" isLink @click="goDetail(item)" />
        </u-swipe-action-item>
      </u-swipe-action>
    </view>
    <u-action-sheet :list="actionList" v-model="showSheet" @click="onActionClick"></u-action-sheet>
    <u-toast ref="uToast"></u-toast>
  </view>
</template>
<script setup lang="ts">
import { ref } from 'vue'
const list = ref([{ id: 1, title: 'Title', desc: 'Description' }])
const showSheet = ref(false)
const options = [{ text: 'Delete', style: { backgroundColor: '#f56c6c' } }]
const actionList = ref([{ text: 'Edit' }, { text: 'Delete' }])
function onSwipeClick(e, item) { if (e.text === 'Delete') { /* delete item */ } }
function onActionClick(e) { uni.$u.toast(e.text) }
function goDetail(item) { uni.$u.route('/pages/detail/detail?id=' + item.id) }
</script>
```

Use **u-empty** when list is empty; **u-swipe-action** for list item actions; **u-action-sheet** for bottom menu; **u-cell** for row. Do not use raw div/button for these.

---

## Example 3: Tabs + Picker + Radio + form-item label (official API)

**Tab switcher must use u-tabs** (never custom `<view class="tab-item">`). Use **:current** and **@change(index)** for tabs; **v-model** and **mode="selector"** + **:range** (1D array) for picker; **value** + **label** for radio; **#label** / **#suffix** for slots (never `slot="label"` or `slot="suffix"`).

```vue
<template>
  <view class="page">
    <u-navbar title="Create" :autoBack="true"></u-navbar>
    <u-tabs
      :list="tabsList"
      :current="currentTab"
      @change="currentTab = $event"
      active-color="#2979ff"
      inactive-color="#606266"
    />
    <u-form :model="form" ref="uForm">
      <u-form-item prop="category" borderBottom>
        <template #label>
          <text>Category</text>
          <text class="sub">(required)</text>
        </template>
        <u-input
          v-model="form.category"
          type="select"
          :select-open="showPicker"
          placeholder="Select"
          border="none"
          @click="showPicker = true"
        />
      </u-form-item>
      <u-form-item label="Type" prop="type" borderBottom>
        <u-radio-group v-model="form.type" active-color="#2979ff">
          <u-radio label="Option A" value="a"></u-radio>
          <u-radio label="Option B" value="b"></u-radio>
        </u-radio-group>
      </u-form-item>
    </u-form>
    <u-picker
      v-model="showPicker"
      mode="selector"
      :range="categoryOptions"
      @confirm="onPickerConfirm"
    />
  </view>
</template>
<script setup lang="ts">
import { ref, reactive } from 'vue'
const currentTab = ref(0)
const tabsList = ref([{ name: 'Tab1' }, { name: 'Tab2' }])
const form = reactive({ category: '', type: 'a' })
const showPicker = ref(false)
const categoryOptions = ref(['Cat1', 'Cat2', 'Cat3'])
function onPickerConfirm(e: number[] | { value?: number[] }) {
  const idx = Array.isArray(e) ? e[0] : e?.value?.[0] ?? 0
  form.category = categoryOptions.value[idx]
  showPicker.value = false
}
</script>
<style lang="scss" scoped>
.sub { font-size: 24rpx; color: #909399; margin-left: 8rpx; }
</style>
```

Do **not** use: custom view/div for tabs (always u-tabs); `lineColor`, `activeStyle`, `itemStyle` on u-tabs; `:show` or `:columns` on u-picker; `name`, `customStyle`, or `placement` on u-radio; **`slot="label"`** or **`slot="suffix"`** (use **#label**, **#suffix** in Vue 3).
