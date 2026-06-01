# COLA 示例：Customer 客户管理完整实现

> 展示一个相对简单的单实体聚合的 CRUD 操作，适合初学者理解 COLA 四层交互。

## 领域层

```java
// === 聚合根 ===
public class Customer extends AggregateRoot<CustomerId> {
    private CustomerId id;
    private String name;
    private Email email;
    private PhoneNumber phone;
    private CustomerType type;
    private CustomerStatus status;
    private LocalDateTime createdAt;

    public static Customer create(CustomerId id, String name, Email email) {
        Customer customer = new Customer();
        customer.id = id;
        customer.name = name;
        customer.email = email;
        customer.type = CustomerType.NORMAL;
        customer.status = CustomerStatus.ACTIVE;
        customer.createdAt = LocalDateTime.now();
        customer.addDomainEvent(new CustomerCreatedEvent(id, name, email));
        return customer;
    }

    public void changeEmail(Email newEmail) {
        this.email = newEmail;
        addDomainEvent(new CustomerEmailChangedEvent(this.id, this.email));
    }

    public void deactivate() {
        if (this.status == CustomerStatus.INACTIVE) return;
        this.status = CustomerStatus.INACTIVE;
        addDomainEvent(new CustomerDeactivatedEvent(this.id));
    }
}

// === 值对象 ===
public final class Email {
    private final String value;
    private static final Pattern PATTERN = Pattern.compile("^[A-Za-z0-9+_.-]+@(.+)$");

    public Email(String value) {
        if (value == null || !PATTERN.matcher(value).matches()) {
            throw new IllegalArgumentException("Invalid email: " + value);
        }
        this.value = value;
    }
    public String getValue() { return value; }
    // equals/hashCode 省略
}

// === 仓储接口 ===
public interface CustomerRepository {
    Optional<Customer> findById(CustomerId id);
    Customer save(Customer customer);
    void delete(CustomerId id);
    Page<Customer> search(String keyword, Pageable pageable);
}
```

## 应用层

```java
// === 命令对象 ===
public class CustomerCreateCmd {
    @NotBlank private String name;
    @Email @NotBlank private String email;
    // getter/setter
}

public class CustomerUpdateEmailCmd {
    @NotBlank private String customerId;
    @Email @NotBlank private String newEmail;
    // getter/setter
}

// === 命令执行器 ===
@Component
public class CustomerCreateCmdExe implements CommandExecutor<CustomerCreateCmd, CustomerDTO> {
    @Resource private CustomerRepository customerRepository;

    @Override
    @Transactional
    public CustomerDTO execute(CustomerCreateCmd cmd) {
        Customer customer = Customer.create(
            new CustomerId(UUID.randomUUID().toString()),
            cmd.getName(),
            new Email(cmd.getEmail())
        );
        customerRepository.save(customer);
        return CustomerAssembler.toDTO(customer);
    }
}

// === 查询执行器 ===
@Component
public class CustomerSearchQryExe implements QueryExecutor<CustomerSearchQry, PageResult<CustomerDTO>> {
    @Resource private CustomerRepository customerRepository;

    @Override
    public PageResult<CustomerDTO> execute(CustomerSearchQry qry) {
        return customerRepository.search(qry.getKeyword(), qry.toPageable())
            .map(CustomerAssembler::toDTO);
    }
}
```

## 适配层

```java
@RestController
@RequestMapping("/api/v1/customers")
public class CustomerController {
    @Resource private CustomerCreateCmdExe customerCreateCmdExe;
    @Resource private CustomerSearchQryExe customerSearchQryExe;

    @PostMapping
    public Response<CustomerDTO> create(@Valid @RequestBody CustomerCreateRequest request) {
        return Response.success(customerCreateCmdExe.execute(request.toCommand()));
    }

    @GetMapping
    public Response<PageResult<CustomerDTO>> search(
            @RequestParam(required = false) String keyword,
            @RequestParam(defaultValue = "1") int page,
            @RequestParam(defaultValue = "20") int pageSize) {
        CustomerSearchQry qry = new CustomerSearchQry();
        qry.setKeyword(keyword);
        qry.setPage(page);
        qry.setPageSize(pageSize);
        return Response.success(customerSearchQryExe.execute(qry));
    }
}
```

## 基础设施层

```java
// 持久化 PO
@Table(name = "t_customer")
public class CustomerPO {
    @Id private String id;
    private String name;
    private String email;
    private String phone;
    private String type;
    private String status;
    private LocalDateTime createdAt;
}

// Mapper
@Mapper
public interface CustomerMapper {
    @Insert("INSERT INTO t_customer(id, name, email, phone, type, status, created_at) " +
            "VALUES(#{id}, #{name}, #{email}, #{phone}, #{type}, #{status}, #{createdAt})")
    void insert(CustomerPO po);

    @Select("SELECT * FROM t_customer WHERE id = #{id}")
    CustomerPO selectById(String id);

    @Select("<script>SELECT * FROM t_customer " +
            "WHERE 1=1 " +
            "<if test='keyword != null'>AND (name LIKE #{keyword} OR email LIKE #{keyword})</if> " +
            "ORDER BY created_at DESC</script>")
    List<CustomerPO> search(@Param("keyword") String keyword);
}

// 仓储实现
@Repository
public class CustomerRepositoryImpl implements CustomerRepository {
    @Resource private CustomerMapper customerMapper;
    @Resource private CustomerConverter converter;

    @Override
    public Customer save(Customer customer) {
        CustomerPO po = converter.toPO(customer);
        customerMapper.insert(po);
        return converter.toDomain(po);
    }

    @Override
    public Optional<Customer> findById(CustomerId id) {
        return Optional.ofNullable(customerMapper.selectById(id.getValue()))
            .map(converter::toDomain);
    }
}
```

## 数据库 DDL

```sql
CREATE TABLE t_customer (
    id          VARCHAR(64) PRIMARY KEY,
    name        VARCHAR(128) NOT NULL,
    email       VARCHAR(256) NOT NULL UNIQUE,
    phone       VARCHAR(32),
    type        VARCHAR(16) NOT NULL DEFAULT 'NORMAL',
    status      VARCHAR(16) NOT NULL DEFAULT 'ACTIVE',
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_status (status)
);
```
