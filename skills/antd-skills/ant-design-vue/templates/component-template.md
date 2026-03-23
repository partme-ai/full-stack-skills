# Component Template | 组件模板

## Basic Component Usage

```vue
<template>
  <a-component-name
    v-model:value="value"
    prop1="value1"
    @change="handleChange"
  />
</template>

<script setup lang="ts">
import { ref } from 'vue';

const value = ref('');
const handleChange = (val) => {
  console.log(val);
};
</script>
```

## Component in Form

```vue
<template>
  <a-form :model="formState" @finish="onFinish">
    <a-form-item
      name="field"
      label="Label"
      :rules="[{ required: true, message: 'Please input!' }]"
    >
      <a-component-name v-model:value="formState.field" />
    </a-form-item>
    <a-form-item>
      <a-button type="primary" html-type="submit">Submit</a-button>
    </a-form-item>
  </a-form>
</template>

<script setup lang="ts">
import { reactive } from 'vue';

interface FormState {
  field: string;
}

const formState = reactive<FormState>({
  field: '',
});

const onFinish = (values: FormState) => {
  console.log('Success:', values);
};
</script>
```

## Modal/Drawer Template

```vue
<template>
  <div>
    <a-button type="primary" @click="showModal">Open</a-button>
    <a-modal
      v-model:open="open"
      title="Title"
      @ok="handleOk"
    >
      <p>Content...</p>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const open = ref<boolean>(false);

const showModal = () => {
  open.value = true;
};

const handleOk = (e: MouseEvent) => {
  console.log(e);
  open.value = false;
};
</script>
```
