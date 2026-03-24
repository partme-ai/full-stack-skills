---
name: redux
description: Provides comprehensive guidance for Redux state management including stores, actions, reducers, middleware, selectors, and Redux Toolkit. Use when the user asks about Redux, needs to manage global state, implement Redux patterns, or work with Redux middleware.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 Redux 管理 React 应用全局状态（store、reducer、action、dispatch）
- 使用 Redux Toolkit（createSlice、configureStore）或经典写法

## How to use this skill

1. **核心**：store、reducer、action、dispatch； useSelector、useDispatch。
2. **Toolkit**：createSlice、configureStore、createAsyncThunk；DevTools 与中间件。
3. **参考**：https://react-redux.js.org/ 、https://redux-toolkit.js.org/

## Best Practices

- 状态扁平、按域切 reducer；action 与 reducer 纯函数。
- 异步用 thunk 或 RTK Query；避免在 reducer 中请求。

## Keywords

redux, Redux Toolkit, store, 状态管理, React
