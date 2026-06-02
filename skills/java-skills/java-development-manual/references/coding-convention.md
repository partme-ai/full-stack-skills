# 编程规约

## 目录
- [一、命名风格](#一命名风格)
- [二、常量定义](#二常量定义)
- [三、代码格式](#三代码格式)
- [四、OOP规约](#四oop规约)
- [五、日期时间](#五日期时间)
- [六、集合处理](#六集合处理)
- [七、并发处理](#七并发处理)
- [八、控制语句](#八控制语句)
- [九、注释规约](#九注释规约)
- [十、前后端规约](#十前后端规约)

---

## 一、命名风格

### 【强制】规约

1. **禁止特殊字符开头/结尾**：代码命名均不能以下划线或美元符号开始/结束
   - 反例：`_name` / `__name` / `$name` / `name_` / `name$` / `name__`

2. **禁止拼音混合命名**：严禁使用拼音与英文混合，更不允许直接使用中文
   - 正例：`ali` / `alibaba` / `taobao` / `hangzhou`（国际通用名称可视同英文）
   - 反例：`DaZhePromotion` / `getPingfenByName()` / `String fw` / `int 某变量 = 3`

3. **禁止歧视性词语**：代码和注释中避免使用种族歧视性词语
   - 正例：`blockList` / `allowList` / `secondary`
   - 反例：`blackList` / `whiteList` / `slave`

4. **类名使用UpperCamelCase**：例外情况：DO/BO/DTO/VO/AO/PO/UID等
   - 正例：`ForceCode` / `UserDO` / `HtmlDTO` / `XmlService`
   - 反例：`forcecode` / `UserDo` / `HTMLDto` / `XMLService`

5. **方法名、参数名、成员变量使用lowerCamelCase**
   - 正例：`localValue` / `getHttpMessage()` / `inputUserId`

6. **常量全大写，下划线分隔**
   - 正例：`MAX_STOCK_COUNT` / `CACHE_EXPIRED_TIME`
   - 反例：`MAX_COUNT` / `EXPIRED_TIME`

7. **特殊类命名**：
   - 抽象类：`Abstract`或`Base`开头
   - 异常类：`Exception`结尾
   - 测试类：被测试类名开始，`Test`结尾

8. **数组声明**：类型与中括号紧挨
   - 正例：`int[] arrayDemo`
   - 反例：`String args[]`

9. **POJO布尔变量不加is前缀**：避免框架解析序列化错误
   - 说明：数据库字段用`is_xxx`，需要在`<resultMap>`设置映射

10. **包名全小写，单数形式**：点分隔符间仅一个自然语义单词
    - 正例：`com.alibaba.ei.kunlun.aap.util`、类名`MessageUtils`

11. **避免子父类成员变量同名**

12. **杜绝不规范缩写**
    - 反例：`AbsClass` / `condi` / `Fu`

13. **接口方法不加修饰符**：保持简洁，加上Javadoc注释

14. **Service/DAO实现类用Impl后缀**
    - 正例：`CacheServiceImpl`实现`CacheService`

15. **枚举类带Enum后缀，成员全大写**
    - 正例：`ProcessStatusEnum.SUCCESS` / `ProcessStatusEnum.UNKNOWN_REASON`

### 【推荐】规约

- 使用完整单词组合表达（自解释）
- 类型名词放词尾：`startTime` / `workQueue` / `nameList`
- 设计模式体现在命名中：`OrderFactory` / `LoginProxy` / `ResourceObserver`

### 各层命名规约

| 层级 | 方法前缀 | 示例 |
|------|---------|------|
| 获取单个对象 | get | `getUserById` |
| 获取多个对象 | list | `listUsers` |
| 获取统计值 | count | `countUsers` |
| 插入 | save/insert | `saveUser` |
| 删除 | remove/delete | `deleteUser` |
| 修改 | update | `updateUser` |

**领域模型命名**：
- 数据对象：`xxxDO`（xxx为表名）
- 数据传输对象：`xxxDTO`
- 展示对象：`xxxVO`
- 禁止命名成`xxxPOJO`

---

## 二、常量定义

### 【强制】规约

1. **禁止魔法值**：不允许未经预先定义的常量直接出现
   ```java
   // 反例
   String key = "Id#taobao_" + tradeId;
   cache.put(key, value);
   ```

2. **Long类型使用大写L**
   ```java
   // 正例
   Long a = 2L;
   // 反例（容易混淆为数字21）
   Long a = 2l;
   ```

### 【推荐】规约

- 按功能归类常量：`CacheConsts` / `SystemConfigConsts`
- 常量复用层次：跨应用→应用内→子工程→包内→类内
- 固定范围变化用enum定义：
  ```java
  public enum SeasonEnum {
      SPRING(1), SUMMER(2), AUTUMN(3), WINTER(4);
      private int seq;
      SeasonEnum(int seq) { this.seq = seq; }
      public int getSeq() { return seq; }
  }
  ```

---

## 三、代码格式

### 【强制】规约

1. **大括号规则**：
   - 空代码块：`{}`
   - 非空：左大括号前不换行，后换行；右大括号前换行

2. **空格规则**：
   - 小括号内外不加空格
   - `if/for/while/switch/do`与括号间加空格
   - 运算符左右加空格

3. **缩进**：4个空格，禁止Tab字符

4. **注释格式**：双斜线与内容间仅一个空格
   ```java
   // 这是正确的注释格式
   ```

5. **单行字符限制**：不超过120字符
   - 换行缩进4空格
   - 运算符与下文一起换行
   - 点符号与下文一起换行
   - 逗号后换行

6. **参数逗号后加空格**：
   ```java
   method(args1, args2, args3);
   ```

7. **IDE编码设置**：UTF-8，换行符使用Unix格式

### 【推荐】规约

- 单个方法总行数不超过80行
- 不同逻辑/业务代码间插入空行

---

## 四、OOP规约

### 【强制】规约

1. **静态成员通过类名访问**，不通过对象引用

2. **覆写方法必须加@Override注解**

3. **可变参数放最后**，同类型同含义才使用

4. **接口过时加@Deprecated注解**

5. **禁止使用过时类/方法**

6. **equals避免NPE**：用常量调用
   ```java
   // 正例
   "test".equals(object);
   // 推荐
   Objects.equals(a, b);
   ```

7. **整型包装类比较用equals**：Integer缓存范围-128~127

8. **货币金额用整型存储**：最小货币单位

9. **浮点数比较**：
   ```java
   // 方式1：误差范围
   float diff = 1e-6F;
   if (Math.abs(a - b) < diff) { ... }

   // 方式2：BigDecimal
   BigDecimal a = new BigDecimal("1.0");
   if (x.compareTo(y) == 0) { ... }
   ```

10. **BigDecimal比较用compareTo()**，不用equals()

11. **DO类属性类型匹配数据库字段类型**

12. **BigDecimal构造用String或valueOf**：
    ```java
    // 正例
    new BigDecimal("0.1");
    BigDecimal.valueOf(0.1);
    // 反例
    new BigDecimal(0.1F);  // 精度损失
    ```

13. **POJO属性用包装类型**，局部变量用基本类型

14. **POJO不设属性默认值**

15. **serialVersionUID不要随意修改**

16. **构造方法禁止业务逻辑**，放init方法

17. **POJO必须写toString()**，继承时加`super.toString()`

18. **禁止同时存在isXxx()和getXxx()**

### 【推荐】规约

- String的split结果做边界检查
- 重载方法放一起
- 方法顺序：公有>私有>getter/setter
- setter/getter不加业务逻辑
- 循环内字符串连接用StringBuilder
- 慎用Object.clone()
- 访问控制从严

---

## 五、日期时间

### 【强制】规约

1. **年份用小写y**：
   ```java
   // 正例
   new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
   // 说明：YYYY是week in which year
   ```

2. **区分大小写**：
   - 大写M：月份
   - 小写m：分钟
   - 大写H：24小时制
   - 小写h：12小时制

3. **获取毫秒数**：
   ```java
   // 正例
   System.currentTimeMillis();
   // 反例
   new Date().getTime();
   ```

4. **禁止使用**：`java.sql.Date` / `java.sql.Time` / `java.sql.Timestamp`

5. **禁止写死一年365天**：
   ```java
   // 正例
   int daysOfThisYear = LocalDate.now().lengthOfYear();
   ```

### 【推荐】规约

- 避免闰年2月问题
- 月份使用枚举：`Calendar.JANUARY`

---

## 六、集合处理

### 【强制】规约

1. **覆写equals必须覆写hashCode**

2. **判空用isEmpty()**，不用size()==0

3. **toMap()必须指定mergeFunction**：
   ```java
   // 正例
   Collectors.toMap(Pair::getKey, Pair::getValue, (v1, v2) -> v2)
   ```

4. **toMap()注意value为null抛NPE**

5. **subList结果不可强转ArrayList**

6. **keySet()/values()/entrySet()返回对象不可添加元素**

7. **Collections.emptyList()不可修改**

8. **subList场景注意父集合修改导致ConcurrentModificationException**

9. **集合转数组用toArray(T[])**：
   ```java
   String[] array = list.toArray(new String[0]);
   ```

10. **addAll()要做NPE判断**

11. **Arrays.asList()不可修改**

12. **foreach循环里禁止remove/add**，用Iterator

13. **Comparator必须满足三个条件**

### 【推荐】规约

- 泛型定义使用diamond语法：`new HashMap<>(16)`
- 集合初始化指定大小：`(需要存储元素数 / 0.75) + 1`
- 使用entrySet遍历Map，或JDK8的forEach

**Map对null的支持**：

| 集合类 | Key为null | Value为null |
|--------|----------|-------------|
| HashMap | 允许 | 允许 |
| ConcurrentHashMap | 不允许 | 不允许 |
| Hashtable | 不允许 | 不允许 |
| TreeMap | 不允许 | 允许 |

---

## 七、并发处理

### 【强制】规约

1. **单例对象保证线程安全**

2. **线程池指定有意义名称**

3. **线程资源必须通过线程池提供**

4. **禁止Executors创建线程池**，用ThreadPoolExecutor
   - FixedThreadPool/SingleThreadPool：队列长度Integer.MAX_VALUE，可能OOM
   - CachedThreadPool：线程数Integer.MAX_VALUE，可能OOM

5. **SimpleDateFormat线程不安全**：
   ```java
   // 正例：ThreadLocal
   private static final ThreadLocal<DateFormat> df = ThreadLocal.withInitial(
       () -> new SimpleDateFormat("yyyy-MM-dd")
   );
   // JDK8推荐：DateTimeFormatter
   ```

6. **ThreadLocal必须回收**：
   ```java
   try {
       threadLocal.set(value);
       // ...
   } finally {
       threadLocal.remove();
   }
   ```

7. **同步调用考量锁性能**：能无锁不锁，能块锁不全方法锁

8. **多资源加锁保持一致顺序**

9. **锁的正确使用**：
   ```java
   Lock lock = new XxxLock();
   lock.lock();
   try {
       doSomething();
   } finally {
       lock.unlock();
   }
   ```

10. **tryLock必须判断是否持有锁**

11. **并发修改同一记录需加锁**：乐观锁version或悲观锁

12. **多线程定时任务用ScheduledExecutorService**，不用Timer

### 【推荐】规约

- 资金相关用悲观锁：一锁、二判、三更新、四释放
- CountDownLatch异步转同步，确保countDown执行
- Random多线程性能问题用ThreadLocalRandom
- 双重检查锁用volatile
- LongAdder比AtomicLong性能更好

---

## 八、控制语句

### 【强制】规约

1. **switch每个case必须终止**（break/return/continue），必须有default

2. **switch String参数必须先null判断**

3. **if/else/for/while/do必须用大括号**

4. **三目运算符注意自动拆箱NPE**

5. **高并发避免用"等于"判断作中断条件**

### 【推荐】规约

- 超过10行的方法，return/throw后加空行
- 异常分支用卫语句：
  ```java
  public void process(Man man) {
      if (man.isUgly()) return;
      if (man.isPoor()) return;
      // 正常逻辑
  }
  ```
- if-else不超过3层，超过用策略/状态模式
- 复杂逻辑提取为布尔变量
- 不在条件表达式中插入赋值语句
- 循环体优化：对象定义、数据库连接等移到循环外
- 避免取反逻辑

---

## 九、注释规约

### 【强制】规约

1. **类、属性、方法用Javadoc格式**`/** */`

2. **抽象方法必须Javadoc注释**：说明功能、参数、返回值、异常

3. **类必须添加创建者和日期**

4. **方法内单行用//，多行用/* */**

5. **枚举字段必须有注释**

### 【推荐】规约

- 英文不好就用中文注释
- 代码修改同步更新注释
- 删除未使用的字段、方法、参数

### 【参考】规约

- 谨慎注释代码，无用则删除
- 特殊标记注明人和时间：TODO / FIXME

---

## 十、前后端规约

### 【强制】规约

1. **API明确要素**：协议(HTTPS)、域名、路径、请求方法、请求内容、状态码、响应体

2. **空列表返回空数组[]或空集合{}**

3. **服务端错误返回**：HTTP状态码 + errorCode + errorMessage + 用户提示

4. **JSON的key用lowerCamelCase**

5. **超大整数用String返回**，禁止Long（JS精度问题）

6. **URL参数不超过2048字节**

7. **body内容控制长度**

8. **翻页边界处理**：小于1返回第一页，大于总数返回最后一页

9. **内部重定向用forward**

### 【推荐】规约

- 响应设置缓存：`Cache-Control: s-maxage=秒数`
- 使用JSON格式而非XML
- 时间格式统一：`yyyy-MM-dd HH:mm:ss`，GMT时区
