# Configuration Templates

## Basic Configuration

```javascript
option: {
  labelWidth: 120,
  labelPosition: 'right',
  size: 'medium',
  submitBtn: true,
  emptyBtn: true,
  column: []
}
```

## Layout Configuration

```javascript
option: {
  gutter: 20,
  span: 24,
  column: [
    {
      label: 'Name',
      prop: 'name',
      type: 'input',
      span: 12
    }
  ]
}
```

## Column Configuration

```javascript
column: [
  {
    label: 'Name',
    prop: 'name',
    type: 'input',
    span: 12,
    disabled: false,
    display: true,
    rules: [
      { required: true, message: 'Please input name' }
    ]
  }
]
```

## Validation Configuration

```javascript
column: [
  {
    label: 'Email',
    prop: 'email',
    type: 'input',
    rules: [
      { required: true, message: 'Please input email' },
      { type: 'email', message: 'Please input valid email' }
    ]
  }
]
```
