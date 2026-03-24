# Exception Filter Template | 异常过滤器模板

```ts
import { ExceptionFilter, Catch, ArgumentsHost, HttpException } from '@nestjs/common'

// HttpExceptionFilter: 处理 HTTP 异常
@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  // catch(): 捕获异常并返回响应
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp()
    const response = ctx.getResponse()
    response.status(exception.getStatus()).json({
      message: exception.message
    })
  }
}
```
