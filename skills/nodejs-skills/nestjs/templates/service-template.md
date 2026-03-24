# Service Template | 服务模板

## Basic Service Template

```typescript
import { Injectable } from '@nestjs/common';
import { CreateDto } from './dto/create-dto.dto';
import { UpdateDto } from './dto/update-dto.dto';

@Injectable()
export class ResourceNameService {
  private items: any[] = [];

  findAll(): any[] {
    return this.items;
  }

  findOne(id: string): any {
    return this.items.find(item => item.id === id);
  }

  create(createDto: CreateDto): any {
    const item = {
      id: Date.now().toString(),
      ...createDto,
    };
    this.items.push(item);
    return item;
  }

  update(id: string, updateDto: UpdateDto): any {
    const item = this.findOne(id);
    if (item) {
      Object.assign(item, updateDto);
    }
    return item;
  }

  remove(id: string): void {
    const index = this.items.findIndex(item => item.id === id);
    if (index > -1) {
      this.items.splice(index, 1);
    }
  }
}
```

## Service with Repository

```typescript
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { EntityName } from './entities/entity-name.entity';
import { CreateDto } from './dto/create-dto.dto';
import { UpdateDto } from './dto/update-dto.dto';

@Injectable()
export class ResourceNameService {
  constructor(
    @InjectRepository(EntityName)
    private repository: Repository<EntityName>,
  ) {}

  async findAll(): Promise<EntityName[]> {
    return this.repository.find();
  }

  async findOne(id: string): Promise<EntityName> {
    return this.repository.findOne({ where: { id } });
  }

  async create(createDto: CreateDto): Promise<EntityName> {
    const entity = this.repository.create(createDto);
    return this.repository.save(entity);
  }

  async update(id: string, updateDto: UpdateDto): Promise<EntityName> {
    await this.repository.update(id, updateDto);
    return this.findOne(id);
  }

  async remove(id: string): Promise<void> {
    await this.repository.delete(id);
  }
}
```
