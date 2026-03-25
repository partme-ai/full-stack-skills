---
name: react-hooks
description: "Provides comprehensive guidance for React Hooks including useState, useEffect, useContext, useReducer, useMemo, useCallback, custom hooks, and hook patterns. Use when the user asks about React Hooks, needs to use hooks in functional components, create custom hooks, or optimize hook performance."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Use built-in React hooks (useState, useEffect, useContext, useRef, useMemo, useCallback)
- Create custom hooks for reusable stateful logic
- Manage complex state with useReducer
- Optimize component performance with memoization hooks
- Handle side effects (data fetching, subscriptions, timers) with useEffect
- Understand and follow the Rules of Hooks

## How to use this skill

### Workflow

1. **Identify which hook** best fits the user's requirement
2. **Apply the Rules of Hooks**: only call hooks at the top level; only call hooks from React functions
3. **Generate hook code** with proper dependency arrays and cleanup functions
4. **Verify** there are no stale closures or missing dependencies

### 1. useState and useEffect

```tsx
import { useState, useEffect } from 'react';

function useUserData(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);

    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        if (!cancelled) {
          setUser(data);
          setLoading(false);
        }
      })
      .catch(err => {
        if (!cancelled) {
          setError(err);
          setLoading(false);
        }
      });

    return () => { cancelled = true; }; // Cleanup on unmount or userId change
  }, [userId]);

  return { user, loading, error };
}
```

### 2. useReducer for Complex State

```tsx
import { useReducer } from 'react';

type State = { count: number; step: number };
type Action = { type: 'increment' } | { type: 'decrement' } | { type: 'setStep'; payload: number };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment': return { ...state, count: state.count + state.step };
    case 'decrement': return { ...state, count: state.count - state.step };
    case 'setStep':   return { ...state, step: action.payload };
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0, step: 1 });
  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </div>
  );
}
```

### 3. useMemo and useCallback

```tsx
import { useMemo, useCallback } from 'react';

function FilteredList({ items, filter }: { items: Item[]; filter: string }) {
  // Memoize expensive computation
  const filtered = useMemo(
    () => items.filter(item => item.name.includes(filter)),
    [items, filter]
  );

  // Memoize callback to prevent child re-renders
  const handleSelect = useCallback((id: string) => {
    console.log('Selected:', id);
  }, []);

  return <ItemList items={filtered} onSelect={handleSelect} />;
}
```

### 4. Custom Hook Pattern

```tsx
import { useState, useCallback } from 'react';

function useToggle(initialValue = false): [boolean, () => void] {
  const [value, setValue] = useState(initialValue);
  const toggle = useCallback(() => setValue(prev => !prev), []);
  return [value, toggle];
}

// Usage
function Modal() {
  const [isOpen, toggleOpen] = useToggle(false);
  return <>{isOpen && <div>Modal Content</div>}<button onClick={toggleOpen}>Toggle</button></>;
}
```

## Best Practices

- Always include all dependencies in the useEffect dependency array (use ESLint plugin `react-hooks/exhaustive-deps`)
- Clean up subscriptions, timers, and listeners in the useEffect return function
- Name custom hooks with the `use` prefix (e.g., `useAuth`, `useFetch`)
- Never call hooks inside conditions, loops, or nested functions
- Use `useCallback` and `useMemo` only when there is a measurable performance benefit
- Prefer `useReducer` over multiple `useState` calls when state transitions are complex

## Resources

- Hooks reference: https://react.dev/reference/react
- Rules of Hooks: https://react.dev/reference/rules/rules-of-hooks

## Keywords

React Hooks, useState, useEffect, useContext, useReducer, useMemo, useCallback, useRef, custom hooks, Rules of Hooks, dependency array, cleanup, memoization
