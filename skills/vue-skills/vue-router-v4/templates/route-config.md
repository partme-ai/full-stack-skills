# Route Configuration Templates | 路由配置模板

## Basic Route

```javascript
{
  path: '/home',
  name: 'Home',
  component: Home
}
```

## Route with Params

```javascript
{
  path: '/user/:id',
  name: 'User',
  component: User
}
```

## Nested Route

```javascript
{
  path: '/user/:id',
  component: UserLayout,
  children: [
    {
      path: 'profile',
      component: UserProfile
    },
    {
      path: 'posts',
      component: UserPosts
    }
  ]
}
```

## Route with Meta

```javascript
{
  path: '/dashboard',
  name: 'Dashboard',
  component: Dashboard,
  meta: {
    requiresAuth: true,
    title: 'Dashboard'
  }
}
```

## Route with Guard

```javascript
{
  path: '/admin',
  component: Admin,
  beforeEnter: (to, from, next) => {
    if (isAdmin()) {
      next()
    } else {
      next('/login')
    }
  }
}
```

## Route with Redirect

```javascript
{
  path: '/home',
  redirect: '/'
}
```

## Route with Alias

```javascript
{
  path: '/',
  component: Home,
  alias: '/home'
}
```

## Lazy Loaded Route

```javascript
{
  path: '/about',
  name: 'About',
  component: () => import('../views/About.vue')
}
```
