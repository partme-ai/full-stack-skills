# Store API

## API Reference

Vuex Store constructor options and instance methods.

### Store Constructor Options

**state**
- Type: `Object | Function`
- Description: Root state object or function returning state

**getters**
- Type: `Object`
- Description: Getter definitions

**mutations**
- Type: `Object`
- Description: Mutation definitions

**actions**
- Type: `Object`
- Description: Action definitions

**modules**
- Type: `Object`
- Description: Module definitions

**plugins**
- Type: `Array<Function>`
- Description: Plugin functions

**strict**
- Type: `Boolean`
- Default: `false`
- Description: Enable strict mode

**devtools**
- Type: `Boolean`
- Default: `true`
- Description: Enable devtools

### Store Instance Properties

**store.state**
- Type: `Object`
- Description: Root state

**store.getters**
- Type: `Object`
- Description: Root getters

### Store Instance Methods

**store.commit(type, payload, options)**
- Commit mutation
- Parameters: `type` - mutation type, `payload` - mutation payload, `options` - options

**store.dispatch(type, payload, options)**
- Dispatch action
- Parameters: `type` - action type, `payload` - action payload, `options` - options

**store.replaceState(state)**
- Replace store state
- Parameters: `state` - new state object

**store.watch(getter, callback, options)**
- Watch getter value
- Parameters: `getter` - getter function, `callback` - callback function, `options` - options

**store.subscribe(callback)**
- Subscribe to mutations
- Parameters: `callback` - callback function

**store.subscribeAction(callback)**
- Subscribe to actions
- Parameters: `callback` - callback function

**store.registerModule(path, module, options)**
- Register dynamic module
- Parameters: `path` - module path, `module` - module object, `options` - options

**store.unregisterModule(path)**
- Unregister dynamic module
- Parameters: `path` - module path

**See also:** `examples/core-concepts/` for detailed usage examples
