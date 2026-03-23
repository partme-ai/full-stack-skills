# Form | 表单

**官方文档**: https://bootstrap-vue.org


## Instructions

This example demonstrates how to use Form components in Bootstrap Vue 3.0.

### Key Concepts

- Form component setup
- Form validation
- Form inputs
- Form submission
- Form layout

### Example: Basic Form

```vue
<template>
  <BForm @submit.prevent="onSubmit">
    <BFormGroup label="Username" label-for="username">
      <BFormInput
        id="username"
        v-model="form.username"
        required
      />
    </BFormGroup>
    <BFormGroup label="Email" label-for="email">
      <BFormInput
        id="email"
        v-model="form.email"
        type="email"
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
  username: '',
  email: ''
})

const onSubmit = () => {
  console.log('Form submitted:', form.value)
}
</script>
```

### Example: Form with Validation

```vue
<template>
  <BForm @submit.prevent="onSubmit">
    <BFormGroup
      label="Email"
      label-for="email"
      :invalid-feedback="emailFeedback"
      :state="emailState"
    >
      <BFormInput
        id="email"
        v-model="form.email"
        type="email"
        :state="emailState"
        required
      />
    </BFormGroup>
    <BFormGroup
      label="Password"
      label-for="password"
      :invalid-feedback="passwordFeedback"
      :state="passwordState"
    >
      <BFormInput
        id="password"
        v-model="form.password"
        type="password"
        :state="passwordState"
        required
      />
    </BFormGroup>
    <BButton type="submit" variant="primary">Submit</BButton>
  </BForm>
</template>

<script setup>
import { ref, computed } from 'vue'
import { BForm, BFormGroup, BFormInput, BButton } from 'bootstrap-vue-next'

const form = ref({
  email: '',
  password: ''
})

const emailState = computed(() => {
  return form.value.email.length > 0 && form.value.email.includes('@')
})

const emailFeedback = computed(() => {
  return emailState.value ? '' : 'Please enter a valid email'
})

const passwordState = computed(() => {
  return form.value.password.length >= 6
})

const passwordFeedback = computed(() => {
  return passwordState.value ? '' : 'Password must be at least 6 characters'
})

const onSubmit = () => {
  if (emailState.value && passwordState.value) {
    console.log('Form submitted:', form.value)
  }
}
</script>
```

### Example: Form with Select

```vue
<template>
  <BForm>
    <BFormGroup label="Select" label-for="select">
      <BFormSelect
        id="select"
        v-model="selected"
        :options="options"
      />
    </BFormGroup>
  </BForm>
</template>

<script setup>
import { ref } from 'vue'
import { BForm, BFormGroup, BFormSelect } from 'bootstrap-vue-next'

const selected = ref(null)
const options = [
  { value: null, text: 'Please select' },
  { value: 'a', text: 'Option A' },
  { value: 'b', text: 'Option B' }
]
</script>
```

### Key Points

- Use `BForm` component to wrap form fields
- Use `BFormGroup` for form field groups
- Use `BFormInput`, `BFormSelect`, etc. for inputs
- Use `v-model` for two-way binding
- Use `:state` prop for validation state
- Use `:invalid-feedback` for error messages
- Use `@submit.prevent` for form submission
