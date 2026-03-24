# Form Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Form component in Ant Design Mini.

### Key Concepts

- Form structure
- Form validation
- Form submission
- Form fields

### Example: Basic Form

```xml
<ant-form onFinish="handleSubmit">
  <ant-form-item label="Name" name="name">
    <ant-input value="{{form.name}}" onInput="handleNameInput" />
  </ant-form-item>
  <ant-form-item label="Email" name="email">
    <ant-input value="{{form.email}}" onInput="handleEmailInput" />
  </ant-form-item>
  <ant-form-item>
    <ant-button type="primary" formType="submit">Submit</ant-button>
  </ant-form-item>
</ant-form>
```

```javascript
// page.js
Page({
  data: {
    form: {
      name: '',
      email: ''
    }
  },
  handleNameInput(e) {
    this.setData({
      'form.name': e.detail.value
    })
  },
  handleEmailInput(e) {
    this.setData({
      'form.email': e.detail.value
    })
  },
  handleSubmit(e) {
    console.log('Form data:', this.data.form)
  }
})
```

### Example: Form Validation

```xml
<ant-form 
  onFinish="handleSubmit"
  onFinishFailed="handleFailed"
>
  <ant-form-item 
    label="Name" 
    name="name"
    rules="{{[{required: true, message: 'Name is required'}]}}"
  >
    <ant-input value="{{form.name}}" onInput="handleNameInput" />
  </ant-form-item>
</ant-form>
```

### Key Points

- Use ant-form for form container
- Use ant-form-item for form fields
- Configure validation rules
- Handle form submission
- Use formType="submit" on button
