# Route Configuration Templates

## Basic Route

```javascript
{
  path: '/home',
  component: Home
}
```

## Named Route

```javascript
{
  path: '/user/:id',
  name: 'user',
  component: User
}
```

## Route with Children

```javascript
{
  path: '/user/:id',
  component: User,
  children: [
    {
      path: 'profile',
      component: Profile
    },
    {
      path: 'posts',
      component: Posts
    }
  ]
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
  path: '/home',
  component: Home,
  alias: '/'
}
```

## Route with Props

```javascript
{
  path: '/user/:id',
  component: User,
  props: true
}
```

## Route with Meta

```javascript
{
  path: '/admin',
  component: Admin,
  meta: {
    requiresAuth: true,
    requiresAdmin: true
  }
}
```

## Route with BeforeEnter Guard

```javascript
{
  path: '/admin',
  component: Admin,
  beforeEnter: (to, from, next) => {
    if (isAdmin()) {
      next()
    } else {
      next('/')
    }
  }
}
```

## Lazy Loaded Route

```javascript
{
  path: '/about',
  component: () => import('@/views/About.vue')
}
```

## Route with Named Views

```javascript
{
  path: '/',
  components: {
    default: Home,
    header: Header,
    footer: Footer
  }
}
```
