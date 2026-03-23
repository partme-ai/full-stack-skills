# Controller Template | 控制器模板

## Basic Controller Template

```typescript
import { Controller, Get, Post, Put, Delete, Body, Param, Query, UseGuards } from '@nestjs/common';
import { ServiceName } from './service-name.service';
import { CreateDto } from './dto/create-dto.dto';
import { UpdateDto } from './dto/update-dto.dto';
import { AuthGuard } from '../auth/guards/auth.guard';

@Controller('resource-name')
@UseGuards(AuthGuard)
export class ResourceNameController {
  constructor(private readonly serviceName: ServiceName) {}

  @Get()
  findAll(@Query('limit') limit?: number) {
    return this.serviceName.findAll(limit);
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.serviceName.findOne(id);
  }

  @Post()
  create(@Body() createDto: CreateDto) {
    return this.serviceName.create(createDto);
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() updateDto: UpdateDto) {
    return this.serviceName.update(id, updateDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.serviceName.remove(id);
  }
}
```

## Controller with Pagination

```typescript
import { Controller, Get, Query } from '@nestjs/common';
import { ServiceName } from './service-name.service';

@Controller('resource-name')
export class ResourceNameController {
  constructor(private readonly serviceName: ServiceName) {}

  @Get()
  findAll(
    @Query('page') page: number = 1,
    @Query('limit') limit: number = 10,
  ) {
    return this.serviceName.findAll(page, limit);
  }
}
```
