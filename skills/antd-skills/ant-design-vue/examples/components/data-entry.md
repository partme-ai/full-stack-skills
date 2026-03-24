# Data Entry Components (数据录入)

## Form (表单)
High performance Form component with data scope management.

```vue
<template>
  <a-form :model="formState" @finish="onFinish">
    <a-form-item
      label="Username"
      name="username"
      :rules="[{ required: true, message: 'Please input your username!' }]"
    >
      <a-input v-model:value="formState.username" />
    </a-form-item>
    <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
      <a-button type="primary" html-type="submit">Submit</a-button>
    </a-form-item>
  </a-form>
</template>
<script setup lang="ts">
import { reactive } from 'vue';
const formState = reactive({ username: '' });
const onFinish = values => { console.log('Success:', values); };
</script>
```

## Input (输入框)
A basic widget for getting the user input.

```vue
<a-input v-model:value="value" placeholder="Basic usage" />
<a-textarea v-model:value="value" :rows="4" />
<a-input-password v-model:value="value" />
```

## Select (选择器)
Select component to select value from options.

```vue
<a-select
  v-model:value="value"
  style="width: 120px"
  :options="[{ value: 'jack', label: 'Jack' }, { value: 'lucy', label: 'Lucy' }]"
/>
```

## DatePicker (日期选择框)
To select or input a date.

```vue
<a-date-picker v-model:value="value" />
<a-range-picker v-model:value="value" />
```

## AutoComplete (自动完成)
Input with auto-complete function.

```vue
<a-auto-complete
  v-model:value="value"
  :options="options"
  placeholder="input here"
  @search="handleSearch"
/>
```

## Cascader (级联选择)
Cascade selection box.

```vue
<a-cascader v-model:value="value" :options="options" placeholder="Please select" />
```

## Checkbox (多选框)
Checkbox.

```vue
<a-checkbox v-model:checked="checked">Checkbox</a-checkbox>
<a-checkbox-group v-model:value="value" :options="plainOptions" />
```

## InputNumber (数字输入框)
Enter a number within certain range.

```vue
<a-input-number v-model:value="value" :min="1" :max="10" />
```

## Mentions (提及)
Mention component.

```vue
<a-mentions v-model:value="value" :options="options" prefix="#" />
```

## Radio (单选框)
Radio.

```vue
<a-radio-group v-model:value="value">
  <a-radio value="a">Hangzhou</a-radio>
  <a-radio value="b">Shanghai</a-radio>
</a-radio-group>
```

## Rate (评分)
Rate component.

```vue
<a-rate v-model:value="value" />
```

## Slider (滑动输入条)
A Slider component for displaying current value and intervals in range.

```vue
<a-slider v-model:value="value" />
<a-slider v-model:value="rangeValue" range />
```

## Switch (开关)
Switching Selector.

```vue
<a-switch v-model:checked="checked" />
```

## TimePicker (时间选择框)
To select or input a time.

```vue
<a-time-picker v-model:value="value" />
```

## Transfer (穿梭框)
Double column transfer choice box.

```vue
<a-transfer
  v-model:targetKeys="targetKeys"
  :dataSource="dataSource"
  :render="item => item.title"
/>
```

## TreeSelect (树选择)
Tree selection control.

```vue
<a-tree-select
  v-model:value="value"
  show-search
  style="width: 100%"
  :dropdown-style="{ maxHeight: '400px', overflow: 'auto' }"
  placeholder="Please select"
  allow-clear
  tree-default-expand-all
  :tree-data="treeData"
/>
```

## Upload (上传)
Upload file control.

```vue
<a-upload
  v-model:file-list="fileList"
  name="file"
  action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
  @change="handleChange"
>
  <a-button>
    <upload-outlined />
    Click to Upload
  </a-button>
</a-upload>
```
