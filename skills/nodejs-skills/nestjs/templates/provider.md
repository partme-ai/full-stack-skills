# Provider Template | 提供者模板

```ts
import { Injectable } from '@nestjs/common'

// AppService: 示例服务
@Injectable()
export class AppService {
  // getMessage(): 返回示例消息
  getMessage() {
    return 'hello'
  }
}
```
