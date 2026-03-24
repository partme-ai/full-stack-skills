# Modal | 模态框

**官方文档**: https://bootstrap-vue.org


## Instructions

This example demonstrates how to use the Modal component in Bootstrap Vue 3.0.

### Key Concepts

- Basic Modal
- Modal with form
- Modal with programmatic control
- Modal sizes
- Modal events

### Example: Basic Modal

```vue
<template>
  <div>
    <BButton @click="showModal = true">Open Modal</BButton>
    <BModal v-model="showModal" title="Modal Title">
      <p>Modal content goes here</p>
    </BModal>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { BButton, BModal } from 'bootstrap-vue-next'

const showModal = ref(false)
</script>
```

### Example: Modal with Form

```vue
<template>
  <div>
    <BButton @click="showModal = true">Open Modal</BButton>
    <BModal
      v-model="showModal"
      title="Form Modal"
      @ok="handleOk"
    >
      <BForm>
        <BFormGroup label="Name" label-for="name">
          <BFormInput id="name" v-model="form.name" />
        </BFormGroup>
      </BForm>
    </BModal>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { BButton, BModal, BForm, BFormGroup, BFormInput } from 'bootstrap-vue-next'

const showModal = ref(false)
const form = ref({ name: '' })

const handleOk = () => {
  console.log('Form submitted:', form.value)
  showModal.value = false
}
</script>
```

### Example: Modal with Programmatic Control

```vue
<template>
  <div>
    <BButton @click="openModal">Open Modal</BButton>
    <BModal
      ref="modal"
      title="Programmatic Modal"
    >
      <p>Modal content</p>
    </BModal>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { BButton, BModal } from 'bootstrap-vue-next'

const modal = ref(null)

const openModal = () => {
  modal.value.show()
}
</script>
```

### Example: Modal Sizes

```vue
<template>
  <div>
    <BButton @click="showSmall = true">Small Modal</BButton>
    <BButton @click="showLarge = true">Large Modal</BButton>
    <BModal v-model="showSmall" title="Small Modal" size="sm">
      <p>Small modal content</p>
    </BModal>
    <BModal v-model="showLarge" title="Large Modal" size="lg">
      <p>Large modal content</p>
    </BModal>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { BButton, BModal } from 'bootstrap-vue-next'

const showSmall = ref(false)
const showLarge = ref(false)
</script>
```

### Key Points

- Use `BModal` component with `v-model` for visibility
- Use `title` prop for modal title
- Use `@ok` event for OK button handler
- Use `size` prop for modal size (sm, lg, xl)
- Use `ref` and `show()` method for programmatic control
- Modal supports slots for header, footer, etc.
