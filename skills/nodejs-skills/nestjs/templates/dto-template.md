# DTO Template | DTO 模板

## Basic DTO Template

```typescript
import { IsString, IsInt, Min, Max, IsOptional, IsEmail, IsBoolean } from 'class-validator';

export class CreateResourceDto {
  @IsString()
  name: string;

  @IsInt()
  @Min(0)
  @Max(100)
  age: number;

  @IsEmail()
  @IsOptional()
  email?: string;

  @IsBoolean()
  @IsOptional()
  isActive?: boolean;
}
```

## Update DTO Template

```typescript
import { IsString, IsInt, Min, Max, IsOptional } from 'class-validator';

export class UpdateResourceDto {
  @IsString()
  @IsOptional()
  name?: string;

  @IsInt()
  @Min(0)
  @Max(100)
  @IsOptional()
  age?: number;
}
```

## DTO with Nested Objects

```typescript
import { IsString, ValidateNested, IsObject } from 'class-validator';
import { Type } from 'class-transformer';

class AddressDto {
  @IsString()
  street: string;

  @IsString()
  city: string;
}

export class CreateUserDto {
  @IsString()
  name: string;

  @ValidateNested()
  @Type(() => AddressDto)
  @IsObject()
  address: AddressDto;
}
```

## DTO with Arrays

```typescript
import { IsArray, IsString, ArrayMinSize } from 'class-validator';

export class CreateResourceDto {
  @IsString()
  name: string;

  @IsArray()
  @IsString({ each: true })
  @ArrayMinSize(1)
  tags: string[];
}
```
