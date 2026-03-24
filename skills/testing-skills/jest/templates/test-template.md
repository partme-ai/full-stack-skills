# Test Template | 测试模板

## Basic Test Template

```javascript
// math.test.js
const { sum, subtract } = require('./math');

describe('Math operations', () => {
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
  });

  test('subtracts 2 - 1 to equal 1', () => {
    expect(subtract(2, 1)).toBe(1);
  });
});
```

## Async Test Template

```javascript
// api.test.js
const { fetchData } = require('./api');

describe('API calls', () => {
  test('fetches data successfully', async () => {
    const data = await fetchData();
    expect(data).toBeDefined();
    expect(data).toHaveProperty('id');
  });

  test('handles errors', async () => {
    await expect(fetchData('invalid')).rejects.toThrow();
  });
});
```

## Mock Test Template

```javascript
// service.test.js
const { processData } = require('./service');
const { fetchData } = require('./api');

jest.mock('./api');

describe('Service', () => {
  test('processes data correctly', async () => {
    fetchData.mockResolvedValue({ id: 1, name: 'John' });
    
    const result = await processData(1);
    
    expect(fetchData).toHaveBeenCalledWith(1);
    expect(result).toEqual({ id: 1, name: 'John', processed: true });
  });
});
```
