# Controller Template | 控制器模板

```ts
import { Controller, Get } from '@nestjs/common'

// AppController: 示例控制器
@Controller('health')
export class AppController {
  // getHealth(): 返回健康状态
  @Get()
  getHealth() {
    return { status: 'ok' }
  }
}
```
