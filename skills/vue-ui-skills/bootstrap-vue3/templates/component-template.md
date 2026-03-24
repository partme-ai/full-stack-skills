# Component Template | 组件模板

## Basic Component Usage

```vue
<template>
  <BComponentName
    prop1="value1"
    prop2="value2"
    @event="handleEvent"
  />
</template>

<script setup>
import { BComponentName } from 'bootstrap-vue-next'

const handleEvent = () => {
  console.log('Event handled')
}
</script>
```

## Component with v-model

```vue
<template>
  <BFormInput
    v-model="value"
    placeholder="Enter text"
  />
</template>

<script setup>
import { ref } from 'vue'
import { BFormInput } from 'bootstrap-vue-next'

const value = ref('')
</script>
```

## Component in Form

```vue
<template>
  <BForm @submit.prevent="onSubmit">
    <BFormGroup label="Field" label-for="field">
      <BFormInput
        id="field"
        v-model="form.field"
        required
      />
    </BFormGroup>
    <BButton type="submit" variant="primary">Submit</BButton>
  </BForm>
</template>

<script setup>
import { ref } from 'vue'
import { BForm, BFormGroup, BFormInput, BButton } from 'bootstrap-vue-next'

const form = ref({
  field: ''
})

const onSubmit = () => {
  console.log('Form submitted:', form.value)
}
</script>
```
