# Guard Template | 守卫模板

```ts
import { CanActivate, ExecutionContext, Injectable } from '@nestjs/common'

// AuthGuard: 示例权限守卫
@Injectable()
export class AuthGuard implements CanActivate {
  // canActivate(): 访问控制逻辑
  canActivate(context: ExecutionContext) {
    const request = context.switchToHttp().getRequest()
    return Boolean(request.user)
  }
}
```
