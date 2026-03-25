---
name: angular
description: "Provides comprehensive guidance for Angular framework including components, modules, services, dependency injection, routing, forms, and TypeScript integration. Use when the user asks about Angular, needs to create Angular applications, implement Angular components, or work with Angular features."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build single-page applications (SPA) with Angular
- Create Angular components, services, directives, and pipes
- Implement routing, lazy-loading, and navigation guards
- Work with reactive forms or template-driven forms
- Use dependency injection and Angular modules
- Integrate RxJS observables and the async pipe
- Set up Angular CLI projects and generate scaffolding
- Optimize performance with OnPush change detection

## How to use this skill

### Workflow

1. **Identify the request area** from the user's question (component creation, routing, forms, services, etc.)
2. **Apply Angular best practices** following the official style guide
3. **Generate TypeScript code** using Angular conventions and decorators
4. **Verify** the solution compiles and follows the dependency injection pattern

### 1. Project Setup

```bash
# Create a new Angular project
ng new my-app --routing --style=scss

# Generate components and services
ng generate component features/user-list
ng generate service core/services/user
```

### 2. Component Example

```typescript
import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { Observable } from 'rxjs';
import { UserService } from '../../core/services/user.service';
import { User } from '../../core/models/user.model';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserListComponent implements OnInit {
  users$!: Observable<User[]>;

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.users$ = this.userService.getUsers();
  }
}
```

### 3. Service with HttpClient

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class UserService {
  private readonly apiUrl = '/api/users';

  constructor(private http: HttpClient) {}

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrl);
  }

  createUser(user: User): Observable<User> {
    return this.http.post<User>(this.apiUrl, user);
  }
}
```

### 4. Routing with Lazy Loading

```typescript
const routes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  {
    path: 'users',
    loadChildren: () =>
      import('./features/users/users.module').then(m => m.UsersModule)
  }
];
```

## Best Practices

- Use `OnPush` change detection and pure pipes for performance
- Organize code into Core, Shared, and Feature modules
- Prefer constructor injection; register services with `providedIn: 'root'` for singletons
- Unsubscribe from observables to prevent memory leaks (use `takeUntil` or the `async` pipe)
- Use reactive forms for complex validation scenarios
- Lazy-load feature modules to reduce initial bundle size

## Resources

- Official documentation: https://angular.io/docs
- Angular CLI: https://angular.io/cli
- RxJS: https://rxjs.dev/

## Keywords

angular, Angular CLI, components, services, RxJS, dependency injection, routing, reactive forms, TypeScript, SPA, OnPush, lazy loading, modules, directives, pipes
