---
name: react
description: "Provides comprehensive guidance for React development including components, JSX, props, state, hooks, context, performance optimization, and best practices. Use when the user asks about React, needs to create React components, implement hooks, manage component state, or build React applications."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build user interfaces with React components and JSX
- Manage component state and lifecycle with hooks
- Create reusable, composable React components
- Use Context API or state management libraries (Redux, Zustand)
- Set up React projects with Vite or Create React App
- Implement routing with React Router
- Optimize rendering performance (React.memo, useMemo, lazy loading)

## How to use this skill

### Workflow

1. **Identify the request area** (component creation, state management, routing, performance, etc.)
2. **Apply React best practices** following the official documentation patterns
3. **Generate JSX/TSX code** using functional components and hooks
4. **Verify** the component tree renders correctly and state flows are clean

### 1. Functional Component

```tsx
import { useState } from 'react';

interface UserCardProps {
  name: string;
  email: string;
  onSelect: (name: string) => void;
}

export function UserCard({ name, email, onSelect }: UserCardProps) {
  return (
    <div className="user-card" onClick={() => onSelect(name)}>
      <h3>{name}</h3>
      <p>{email}</p>
    </div>
  );
}
```

### 2. State and Effects

```tsx
import { useState, useEffect } from 'react';

export function UserList() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/users')
      .then(res => res.json())
      .then(data => {
        setUsers(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### 3. Custom Hook

```tsx
import { useState, useCallback } from 'react';

function useToggle(initial = false): [boolean, () => void] {
  const [value, setValue] = useState(initial);
  const toggle = useCallback(() => setValue(v => !v), []);
  return [value, toggle];
}
```

### 4. Context Pattern

```tsx
import { createContext, useContext, useState, ReactNode } from 'react';

const ThemeContext = createContext<{ dark: boolean; toggle: () => void } | null>(null);

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [dark, setDark] = useState(false);
  const toggle = () => setDark(d => !d);
  return <ThemeContext.Provider value={{ dark, toggle }}>{children}</ThemeContext.Provider>;
}

export function useTheme() {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error('useTheme must be used within ThemeProvider');
  return ctx;
}
```

## Best Practices

- Keep components small and focused on a single responsibility
- Lift state up to the nearest common ancestor; use Context for deeply shared state
- Always provide a stable `key` prop when rendering lists
- Clean up side effects in `useEffect` return functions (subscriptions, timers)
- Avoid creating new objects/functions inline in JSX to prevent unnecessary re-renders
- Use `React.lazy` and `Suspense` for code-splitting large routes

## Resources

- Official documentation: https://react.dev/
- React hooks reference: https://react.dev/reference/react
- Create React App: https://create-react-app.dev/

## Keywords

react, React Hooks, JSX, TSX, components, state, props, useEffect, useState, Context API, functional components, performance, memo, lazy loading
