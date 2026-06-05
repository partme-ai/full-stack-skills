# Example 02 — 产品目录管理（Product Catalog）

> 展示洋葱架构中多个聚合通过 Application 层协作的模式。

## 业务描述

产品目录管理包含产品（Product）和分类（Category）两个聚合。产品归属某个分类，查询时需跨聚合获取分类名称。

## 模型设计

```
Category (聚合根)                    Product (聚合根)
  └── categoryId (值对象)               └── productId (值对象)
  └── name (值对象)                     └── categoryId (引用，非对象)
  └── parentCategoryId (引用)            └── name (值对象)
  └── products (不持有！)                └── price (值对象)
```

## Domain 层

```java
// core/domain/model/product/Product.java
public class Product extends AggregateRoot<ProductId> {
    private ProductId id;
    private CategoryId categoryId;              // 跨聚合 ID 引用
    private ProductName name;                   // 值对象
    private Money price;                        // 值对象
    private ProductStatus status;
    private LocalDateTime createdAt;

    private Product(ProductId id, CategoryId categoryId, ProductName name, Money price) {
        this.id = id;
        this.categoryId = categoryId;
        this.name = name;
        this.price = price;
        this.status = ProductStatus.ACTIVE;
        this.createdAt = LocalDateTime.now();
    }

    public static Product create(ProductId id, CategoryId categoryId, ProductName name, Money price) {
        if (price.isNegativeOrZero()) throw new DomainException("价格必须大于0");
        Product product = new Product(id, categoryId, name, price);
        product.addDomainEvent(new ProductCreatedEvent(id, categoryId));
        return product;
    }

    public void updatePrice(Money newPrice) {
        if (newPrice.isNegativeOrZero()) throw new DomainException("价格必须大于0");
        this.price = newPrice;
        addDomainEvent(new ProductPriceChangedEvent(this.id, this.price));
    }

    public void deactivate() {
        if (this.status == ProductStatus.INACTIVE) return;
        this.status = ProductStatus.INACTIVE;
        addDomainEvent(new ProductDeactivatedEvent(this.id));
    }

    // getter
    public ProductId getId() { return id; }
    public CategoryId getCategoryId() { return categoryId; }
    public ProductName getName() { return name; }
    public Money getPrice() { return price; }
    public ProductStatus getStatus() { return status; }
}

// core/domain/model/category/Category.java
public class Category extends AggregateRoot<CategoryId> {
    private CategoryId id;
    private CategoryName name;                  // 值对象
    private CategoryId parentCategoryId;        // 父分类 ID 引用
    private int level;
    private boolean active;

    public static Category create(CategoryId id, CategoryName name) {
        Category category = new Category();
        category.id = id;
        category.name = name;
        category.level = 0;
        category.active = true;
        category.addDomainEvent(new CategoryCreatedEvent(id));
        return category;
    }

    public static Category createSubCategory(CategoryId id, CategoryName name, CategoryId parentId) {
        Category category = create(id, name);
        category.parentCategoryId = parentId;
        category.level = 1;
        return category;
    }

    public void rename(CategoryName newName) {
        this.name = newName;
    }

    public CategoryId getId() { return id; }
    public CategoryName getName() { return name; }
    public CategoryId getParentCategoryId() { return parentCategoryId; }
    public int getLevel() { return level; }
}

// core/domain/repository/ProductRepository.java
public interface ProductRepository {
    Optional<Product> findById(ProductId id);
    void save(Product product);
    Page<Product> findByCategoryId(CategoryId categoryId, Pageable pageable);
    Page<Product> findByNameContaining(String keyword, Pageable pageable);
}

// core/domain/repository/CategoryRepository.java
public interface CategoryRepository {
    Optional<Category> findById(CategoryId id);
    void save(Category category);
    List<Category> findAllActive();
}
```

## Application 层（跨聚合编排）

```java
// core/application/service/ProductCatalogService.java
public interface ProductCatalogService {
    ProductDTO createProduct(CreateProductCommand command);
    ProductDTO getProductWithCategory(String productId);
    Page<ProductDTO> searchProducts(String keyword, int page, int size);
    void updateProductPrice(String productId, BigDecimal newPrice);
}

// core/application/service/ProductCatalogServiceImpl.java
public class ProductCatalogServiceImpl implements ProductCatalogService {
    private final ProductRepository productRepository;
    private final CategoryRepository categoryRepository;
    private final ProductDTOAssembler assembler;

    @Override
    @Transactional
    public ProductDTO createProduct(CreateProductCommand command) {
        // 1. 验证分类存在（跨聚合查询）
        Category category = categoryRepository.findById(new CategoryId(command.getCategoryId()))
            .orElseThrow(() -> new CategoryNotFoundException(command.getCategoryId()));

        // 2. 创建产品（Domain 层）
        Product product = Product.create(
            ProductId.generate(),
            category.getId(),
            new ProductName(command.getProductName()),
            Money.of(command.getPrice(), "CNY")
        );

        // 3. 持久化
        productRepository.save(product);

        // 4. 返回 DTO（含分类名称）
        return assembler.toDTOWithCategory(product, category);
    }

    @Override
    @Transactional(readOnly = true)
    public ProductDTO getProductWithCategory(String productId) {
        Product product = productRepository.findById(new ProductId(productId))
            .orElseThrow(() -> new ProductNotFoundException(productId));
        Category category = categoryRepository.findById(product.getCategoryId())
            .orElse(null);
        return assembler.toDTOWithCategory(product, category);
    }
}
```

## Infrastructure 层

```java
// infrastructure/data/repository/ProductRepositoryImpl.java
@Repository
public class ProductRepositoryImpl implements ProductRepository {
    private final JpaProductRepository jpaRepo;
    private final ProductMapper mapper;

    @Override
    public void save(Product product) {
        jpaRepo.save(mapper.toPO(product));
    }

    @Override
    public Optional<Product> findById(ProductId id) {
        return jpaRepo.findById(id.getValue()).map(mapper::toDomain);
    }
}

// infrastructure/data/repository/CategoryRepositoryImpl.java
@Repository
public class CategoryRepositoryImpl implements CategoryRepository {
    private final JpaCategoryRepository jpaRepo;
    private final CategoryMapper mapper;

    @Override
    public void save(Category category) {
        jpaRepo.save(mapper.toPO(category));
    }
}
```

## API 层

```java
// api/controller/ProductController.java
@RestController
@RequestMapping("/api/v1/products")
public class ProductController {
    private final ProductCatalogService catalogService;

    @PostMapping
    public ResponseEntity<ApiResponse<ProductResponse>> createProduct(
            @Valid @RequestBody CreateProductRequest request) {
        ProductDTO dto = catalogService.createProduct(request.toCommand());
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(ApiResponse.success(ProductResponseAssembler.toResponse(dto)));
    }

    @GetMapping("/{productId}")
    public ResponseEntity<ApiResponse<ProductResponse>> getProduct(
            @PathVariable String productId) {
        ProductDTO dto = catalogService.getProductWithCategory(productId);
        return ResponseEntity.ok(ApiResponse.success(ProductResponseAssembler.toResponse(dto)));
    }

    @PutMapping("/{productId}/price")
    public ResponseEntity<ApiResponse<Void>> updatePrice(
            @PathVariable String productId,
            @RequestBody @NotNull BigDecimal newPrice) {
        catalogService.updateProductPrice(productId, newPrice);
        return ResponseEntity.ok(ApiResponse.success(null));
    }
}
```

## 关键设计点

1. **跨聚合 ID 引用**：Product 持有 `CategoryId`（值对象），不持有 `Category` 对象
2. **聚合协作在 Application 层**：`ProductCatalogService` 同时调用两个 Repository，在应用层组合数据
3. **不变的 Domain 层**：Product 和 Category 彼此完全不知道对方存在
4. **DTO 聚合在 Application 层**：`ProductDTOAssembler.toDTOWithCategory()` 组装跨聚合数据
