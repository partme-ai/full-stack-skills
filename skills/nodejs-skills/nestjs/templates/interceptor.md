# Interceptor Template | 拦截器模板

```ts
import { CallHandler, ExecutionContext, Injectable, NestInterceptor } from '@nestjs/common'
import { Observable } from 'rxjs'
import { map } from 'rxjs/operators'

// TransformInterceptor: 统一响应结构
@Injectable()
export class TransformInterceptor implements NestInterceptor {
  // intercept(): 拦截并转换响应
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    return next.handle().pipe(map(data => ({ data })))
  }
}
```
