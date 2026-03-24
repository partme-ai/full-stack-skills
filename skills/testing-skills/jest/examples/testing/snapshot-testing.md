# Snapshot Testing | 快照测试

**官方文档**: https://jestjs.io/docs/snapshot-testing


## Instructions

This example demonstrates how to use snapshot testing in Jest.

### Key Concepts

- Creating snapshots
- Updating snapshots
- Inline snapshots
- Property matchers
- Snapshot serializers

### Example: Basic Snapshot

```javascript
// Link.react.js
import React from 'react';

const Link = ({ page, children }) => {
  return <a href={page}>{children}</a>;
};

export default Link;
```

```javascript
// Link.test.js
import React from 'react';
import renderer from 'react-test-renderer';
import Link from '../Link.react';

test('Link renders correctly', () => {
  const tree = renderer
    .create(<Link page="http://www.facebook.com">Facebook</Link>)
    .toJSON();
  expect(tree).toMatchSnapshot();
});
```

### Example: Updating Snapshots

```bash
# Update all snapshots
jest --updateSnapshot

# Or use -u flag
jest -u
```

### Example: Inline Snapshots

```javascript
test('inline snapshot', () => {
  expect({ name: 'John', age: 30 }).toMatchInlineSnapshot(`
    Object {
      "age": 30,
      "name": "John",
    }
  `);
});
```

### Example: Property Matchers

```javascript
test('property matchers', () => {
  const user = {
    createdAt: new Date(),
    id: Math.floor(Math.random() * 20),
    name: 'John',
  };

  expect(user).toMatchSnapshot({
    createdAt: expect.any(Date),
    id: expect.any(Number),
  });
});
```

### Example: Snapshot Serializers

```javascript
// Custom serializer
expect.addSnapshotSerializer({
  test: (val) => val && val.hasOwnProperty('name'),
  print: (val, serialize) => `Name: ${val.name}`,
});
```

### Key Points

- Snapshots capture component/object output
- Use `toMatchSnapshot()` for snapshots
- Use `toMatchInlineSnapshot()` for inline snapshots
- Update snapshots with `--updateSnapshot` flag
- Use property matchers for dynamic values
- Review snapshot changes before committing
- Snapshots should be committed to version control
