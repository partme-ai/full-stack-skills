---
name: redux
description: "Provides comprehensive guidance for Redux state management including stores, actions, reducers, middleware, selectors, and Redux Toolkit. Use when the user asks about Redux, needs to manage global state, implement Redux patterns, or work with Redux middleware."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Manage global application state with Redux or Redux Toolkit
- Create slices with `createSlice` and configure the store with `configureStore`
- Handle asynchronous logic with `createAsyncThunk` or RTK Query
- Use `useSelector` and `useDispatch` hooks in React components
- Implement middleware, selectors, and normalized state patterns
- Migrate from classic Redux to Redux Toolkit

## How to use this skill

### Workflow

1. **Identify the state domain** the user needs to manage
2. **Create a slice** using Redux Toolkit's `createSlice`
3. **Configure the store** and provide it to the React app
4. **Connect components** using `useSelector` and `useDispatch`

### 1. Create a Slice

```typescript
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface CounterState {
  value: number;
}

const initialState: CounterState = { value: 0 };

const counterSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    increment(state) { state.value += 1; },
    decrement(state) { state.value -= 1; },
    incrementByAmount(state, action: PayloadAction<number>) {
      state.value += action.payload;
    },
  },
});

export const { increment, decrement, incrementByAmount } = counterSlice.actions;
export default counterSlice.reducer;
```

### 2. Configure the Store

```typescript
import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './counterSlice';

export const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

### 3. Use in Components

```tsx
import { useSelector, useDispatch } from 'react-redux';
import { RootState, AppDispatch } from './store';
import { increment, decrement } from './counterSlice';

export function Counter() {
  const count = useSelector((state: RootState) => state.counter.value);
  const dispatch = useDispatch<AppDispatch>();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch(increment())}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
    </div>
  );
}
```

### 4. Async Thunk

```typescript
import { createAsyncThunk } from '@reduxjs/toolkit';

export const fetchUsers = createAsyncThunk('users/fetch', async () => {
  const response = await fetch('/api/users');
  return response.json();
});
```

## Best Practices

- Keep state flat and normalized; split reducers by domain
- Use Redux Toolkit (`createSlice`, `configureStore`) instead of hand-written boilerplate
- Actions and reducers should be pure functions with no side effects
- Use `createAsyncThunk` or RTK Query for async operations; never fetch in reducers
- Use typed hooks (`useAppSelector`, `useAppDispatch`) for type-safe access
- Only store serializable data in the Redux store

## Resources

- Redux Toolkit: https://redux-toolkit.js.org/
- React Redux: https://react-redux.js.org/
- RTK Query: https://redux-toolkit.js.org/rtk-query/overview

## Keywords

redux, Redux Toolkit, createSlice, configureStore, createAsyncThunk, RTK Query, useSelector, useDispatch, state management, middleware, store, actions, reducers
