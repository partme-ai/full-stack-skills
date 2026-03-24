package ${package.Repository}

import ${package.Entity}.${entity}
import java.util.List
import java.util.Optional

/**
 * <p>${table.comment}仓储接口</p>
 * 
 * <p>定义${table.comment}聚合的仓储接口，遵循领域驱动设计（DDD）原则。
 * 仓储接口位于领域层，定义${table.comment}聚合的持久化契约，不依赖具体的技术实现。</p>
 * 
 * <p>主要职责：
 * <ul>
 *   <li>保存${table.comment}聚合</li>
 *   <li>根据ID查找${table.comment}聚合</li>
 *   <li>删除${table.comment}聚合</li>
 *   <li>查询${table.comment}聚合列表</li>
 *   <li>批量保存${table.comment}聚合</li>
 *   <li>批量删除${table.comment}聚合</li>
 *   <li>判断${table.comment}聚合是否存在</li>
 *   <li>统计${table.comment}聚合数量</li>
<#if customMethods??>
<#list customMethods as method>
 *   <li>${method.description}</li>
</#list>
</#if>
 * </ul>
 * </p>
 * 
 * <p>注意：仓储接口是领域层的核心接口，实现类应放在基础设施层（infrastructure/persistence/repository/）。</p>
 * 
 * @author ${author}
 * @since ${date}
 */
interface ${entity}Repository {

    /**
     * <p>保存${table.comment}聚合</p>
     * 
     * <p>保存或更新${table.comment}聚合根。如果聚合根已存在则更新，否则创建新聚合根。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)} ${table.comment}聚合根对象
     * @return ${table.comment}聚合根对象
     */
    fun save(${entity?substring(0,1)?lower_case}${entity?substring(1)}: ${entity}): ${entity}

    /**
     * <p>根据ID查找${table.comment}聚合</p>
     * 
     * <p>根据聚合根ID查找对应的${table.comment}聚合。如果不存在则返回 null。</p>
     * 
     * @param id ${table.comment}聚合根ID
     * @return ${table.comment}聚合根对象，如果不存在则返回 null
     */
    fun findById(id: Long): ${entity}?

    /**
     * <p>删除${table.comment}聚合</p>
     * 
     * <p>根据聚合根ID删除${table.comment}聚合。删除操作会级联删除聚合内的所有实体。</p>
     * 
     * @param id ${table.comment}聚合根ID
     */
    fun deleteById(id: Long)

    /**
     * <p>查询所有${table.comment}聚合</p>
     * 
     * <p>查询所有${table.comment}聚合根列表。注意：对于大数据量场景，应使用分页查询。</p>
     * 
     * @return ${table.comment}聚合根列表
     */
    fun findAll(): List<${entity}>

    /**
     * <p>批量保存${table.comment}聚合</p>
     * 
     * <p>批量保存或更新${table.comment}聚合根列表。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)}List ${table.comment}聚合根列表
     * @return 保存后的${table.comment}聚合根列表
     */
    fun saveAll(${entity?substring(0,1)?lower_case}${entity?substring(1)}List: List<${entity}>): List<${entity}>

    /**
     * <p>批量删除${table.comment}聚合</p>
     * 
     * <p>根据聚合根ID列表批量删除${table.comment}聚合。</p>
     * 
     * @param ids ${table.comment}聚合根ID列表
     */
    fun deleteAllByIds(ids: List<Long>)

    /**
     * <p>判断${table.comment}聚合是否存在</p>
     * 
     * <p>根据聚合根ID判断${table.comment}聚合是否存在。</p>
     * 
     * @param id ${table.comment}聚合根ID
     * @return Boolean 是否存在
     */
    fun existsById(id: Long): Boolean

    /**
     * <p>统计${table.comment}聚合数量</p>
     * 
     * <p>统计${table.comment}聚合根的总数量。</p>
     * 
     * @return Long ${table.comment}聚合根数量
     */
    fun count(): Long
<#if customMethods??>

## ----------  BEGIN 自定义方法  ----------
<#list customMethods as method>
    /**
     * <p>${method.description}</p>
     * 
     * <p>${method.detailDescription}</p>
     * 
<#list method.parameters as param>
     * @param ${param.name} ${param.type} ${param.description}
</#list>
     * @return ${method.returnType} ${method.returnDescription}
<#if method.exceptions??>
<#list method.exceptions as exception>
     * @exception ${exception.type} ${exception.description}
</#list>
</#if>
     */
    fun ${method.name}(<#list method.parameters as param>${param.name}: ${param.type}<#if param_has_next>, </#if></#list>): ${method.returnType}
</#list>
## ----------  END 自定义方法  ----------
</#if>
}
