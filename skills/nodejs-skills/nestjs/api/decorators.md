# Decorators API | 装饰器 API

## API Reference

All NestJS decorators and their usage.

### Module Decorators

#### @Module()

Defines a module.

**Properties:**
- `imports`: Array of modules to import
- `controllers`: Array of controllers
- `providers`: Array of providers
- `exports`: Array of providers to export

**Example:**
```typescript
@Module({
  imports: [OtherModule],
  controllers: [CatsController],
  providers: [CatsService],
  exports: [CatsService],
})
export class CatsModule {}
```

### Controller Decorators

#### @Controller()

Defines a controller with optional route prefix.

**Parameters:**
- `prefix`: Route prefix (optional)

**Example:**
```typescript
@Controller('cats')
export class CatsController {}
```

#### @Get(), @Post(), @Put(), @Delete(), @Patch()

HTTP method decorators.

**Parameters:**
- `path`: Route path (optional)

**Example:**
```typescript
@Get()
@Get('profile')
@Post('create')
```

### Parameter Decorators

#### @Param()

Extract route parameter.

**Parameters:**
- `property`: Parameter name (optional)

**Example:**
```typescript
@Get(':id')
findOne(@Param('id') id: string) {}
```

#### @Query()

Extract query parameter.

**Parameters:**
- `property`: Query parameter name (optional)

**Example:**
```typescript
@Get()
findAll(@Query('limit') limit: number) {}
```

#### @Body()

Extract request body.

**Parameters:**
- `property`: Body property name (optional)

**Example:**
```typescript
@Post()
create(@Body() createDto: CreateDto) {}
```

#### @Headers()

Extract request header.

**Parameters:**
- `property`: Header name (optional)

**Example:**
```typescript
@Get()
findAll(@Headers('authorization') auth: string) {}
```

#### @Req(), @Request()

Extract request object.

**Example:**
```typescript
@Get()
findAll(@Req() request: Request) {}
```

#### @Res(), @Response()

Extract response object.

**Example:**
```typescript
@Get()
findAll(@Res() response: Response) {}
```

### Provider Decorators

#### @Injectable()

Marks a class as a provider.

**Example:**
```typescript
@Injectable()
export class CatsService {}
```

#### @Inject()

Injects a custom provider.

**Parameters:**
- `token`: Injection token

**Example:**
```typescript
constructor(@Inject('CONFIG') private config: any) {}
```

#### @Optional()

Marks a dependency as optional.

**Example:**
```typescript
constructor(@Optional() @Inject('CONFIG') private config: any) {}
```

### Guard Decorators

#### @UseGuards()

Applies guards to controller or route.

**Parameters:**
- `...guards`: Guard classes or instances

**Example:**
```typescript
@UseGuards(AuthGuard)
@Controller('cats')
export class CatsController {}
```

### Interceptor Decorators

#### @UseInterceptors()

Applies interceptors to controller or route.

**Parameters:**
- `...interceptors`: Interceptor classes or instances

**Example:**
```typescript
@UseInterceptors(LoggingInterceptor)
@Controller('cats')
export class CatsController {}
```

### Pipe Decorators

#### @UsePipes()

Applies pipes to controller or route.

**Parameters:**
- `...pipes`: Pipe classes or instances

**Example:**
```typescript
@UsePipes(ValidationPipe)
@Post()
create(@Body() createDto: CreateDto) {}
```

### Exception Filter Decorators

#### @UseFilters()

Applies exception filters to controller or route.

**Parameters:**
- `...filters`: Exception filter classes or instances

**Example:**
```typescript
@UseFilters(HttpExceptionFilter)
@Controller('cats')
export class CatsController {}
```

### HTTP Code Decorators

#### @HttpCode()

Sets HTTP status code.

**Parameters:**
- `statusCode`: HTTP status code

**Example:**
```typescript
@Post()
@HttpCode(201)
create() {}
```

#### @Header()

Sets response header.

**Parameters:**
- `name`: Header name
- `value`: Header value

**Example:**
```typescript
@Get()
@Header('Cache-Control', 'no-cache')
findAll() {}
```

#### @Redirect()

Redirects to a URL.

**Parameters:**
- `url`: Redirect URL
- `statusCode`: HTTP status code (default: 302)

**Example:**
```typescript
@Get()
@Redirect('https://nestjs.com', 301)
redirect() {}
```

### Key Points

- Decorators provide metadata for NestJS
- Use decorators to configure controllers, providers, and routes
- Parameter decorators extract values from requests
- Method decorators define HTTP methods and routes
- Class decorators define modules, controllers, and providers
