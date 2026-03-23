# Middleware Template | 中间件模板

```ts
import { Injectable, NestMiddleware } from '@nestjs/common'
import { Request, Response, NextFunction } from 'express'

// LoggerMiddleware: 记录请求日志
@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  // use(): 中间件执行逻辑
  use(req: Request, res: Response, next: NextFunction) {
    console.log(req.method, req.originalUrl)
    next()
  }
}
```
