# Installation | 安装

**官方文档**: https://jestjs.io/docs/getting-started


## Instructions

This example demonstrates how to install Jest and set it up in a project.

### Key Concepts

- Installing Jest
- Creating Jest configuration
- Writing first test
- Running tests
- Package.json scripts

### Example: Installation

```bash
# Using npm
npm install --save-dev jest

# Using yarn
yarn add --dev jest

# Using pnpm
pnpm add -D jest
```

### Example: Basic Configuration

```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'node',
  testMatch: ['**/__tests__/**/*.js', '**/?(*.)+(spec|test).js'],
  collectCoverageFrom: [
    '**/*.js',
    '!**/node_modules/**',
    '!**/coverage/**'
  ]
};
```

### Example: Package.json Scripts

```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

### Example: First Test

```javascript
// sum.js
function sum(a, b) {
  return a + b;
}
module.exports = sum;
```

```javascript
// sum.test.js
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

### Example: Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run tests with coverage
npm test -- --coverage
```

### Example: TypeScript Configuration

```typescript
// jest.config.ts
import type { Config } from 'jest';

const config: Config = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts'],
};

export default config;
```

### Key Points

- Install Jest as a dev dependency
- Create jest.config.js for configuration
- Write tests in files ending with .test.js or .spec.js
- Use npm test or jest command to run tests
- Configure test environment (node, jsdom, etc.)
- Set up test match patterns
- Add scripts to package.json for convenience
