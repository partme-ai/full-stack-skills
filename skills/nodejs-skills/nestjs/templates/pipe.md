# Pipe Template | 管道模板

```ts
import { PipeTransform, Injectable, BadRequestException } from '@nestjs/common'

// ParseIdPipe: 将字符串 id 转为数字
@Injectable()
export class ParseIdPipe implements PipeTransform {
  // transform(): 管道转换逻辑
  transform(value: string) {
    const parsed = Number(value)
    if (Number.isNaN(parsed)) {
      throw new BadRequestException('Invalid id')
    }
    return parsed
  }
}
```
