# Module Template | 模块模板

```ts
import { Module } from '@nestjs/common'
import { AppController } from './app.controller'
import { AppService } from './app.service'

// AppModule: 应用模块
@Module({
  controllers: [AppController],
  providers: [AppService]
})
export class AppModule {}
```
