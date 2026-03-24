# Manual Mocks | 手动 Mock

**官方文档**: https://jestjs.io/docs/manual-mocks


## Instructions

This example demonstrates how to create manual mocks in Jest.

### Key Concepts

- Creating __mocks__ directory
- Manual module mocks
- Mocking user modules
- Mocking node modules

### Example: Mocking User Module

```javascript
// src/utils.js
export const helper = () => {
  return 'real implementation';
};
```

```javascript
// src/__mocks__/utils.js
export const helper = () => {
  return 'mocked implementation';
};
```

```javascript
// src/utils.test.js
jest.mock('./utils');

import { helper } from './utils';

test('uses manual mock', () => {
  expect(helper()).toBe('mocked implementation');
});
```

### Example: Mocking Node Module

```javascript
// __mocks__/axios.js
export default {
  get: jest.fn(() => Promise.resolve({ data: {} })),
  post: jest.fn(() => Promise.resolve({ data: {} })),
};
```

```javascript
// api.test.js
jest.mock('axios');

import axios from 'axios';
import { fetchData } from './api';

test('fetches data', async () => {
  axios.get.mockResolvedValue({ data: { id: 1 } });
  const data = await fetchData();
  expect(data).toEqual({ id: 1 });
});
```

### Example: Partial Mock

```javascript
// __mocks__/fs.js
const fs = jest.requireActual('fs');

module.exports = {
  ...fs,
  readFileSync: jest.fn(() => 'mocked content'),
};
```

### Key Points

- Create `__mocks__` directory next to module
- Manual mocks are used automatically with `jest.mock()`
- Can mock both user modules and node modules
- Use `jest.requireActual()` for partial mocks
- Manual mocks should match module structure
- Manual mocks are hoisted to top of file
