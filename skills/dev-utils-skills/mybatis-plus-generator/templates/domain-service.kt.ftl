package ${package.Domain}.service

import ${package.Domain}.model.aggregate.${entity?lower_case}.${entity}
import org.springframework.stereotype.Service

/**
 * <p>${table.comment}领域服务</p>
 * 
 * <p>${table.comment}的领域服务，位于领域层，包含不属于任何聚合根的领域逻辑。
 * 领域服务用于处理跨聚合的业务逻辑，或处理不适合放在聚合根中的复杂业务规则。</p>
 * 
 * <p>主要职责：
 * <ul>
 *   <li>处理跨聚合的业务逻辑</li>
 *   <li>实现复杂的业务规则</li>
 *   <li>协调多个聚合根完成业务操作</li>
<#if customMethods??>
<#list customMethods as method>
 *   <li>${method.description}</li>
</#list>
</#if>
 * </ul>
 * </p>
 * 
 * <p>注意：领域服务应是无状态的，不应包含持久化逻辑。持久化操作应通过仓储接口完成。</p>
 * 
 * @author ${author}
 * @since ${date}
 */
@Service
class ${entity}DomainService {

    /**
     * <p>验证${table.comment}业务规则</p>
     * 
     * <p>验证${table.comment}是否符合业务规则。此方法包含复杂的业务规则验证逻辑。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)} ${table.comment}聚合根对象
     * @return Boolean 是否符合业务规则
     */
    fun validateBusinessRules(${entity?substring(0,1)?lower_case}${entity?substring(1)}: ${entity}): Boolean {
        // TODO: 实现业务规则验证逻辑
        // 1. 验证业务不变性
        // 2. 验证业务规则
        // 3. 返回验证结果
        return true
    }

    /**
     * <p>计算${table.comment}相关业务指标</p>
     * 
     * <p>计算${table.comment}相关的业务指标，如统计信息、汇总数据等。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)} ${table.comment}聚合根对象
     * @return Any? 业务指标计算结果
     */
    fun calculateBusinessMetrics(${entity?substring(0,1)?lower_case}${entity?substring(1)}: ${entity}): Any? {
        // TODO: 实现业务指标计算逻辑
        // 1. 计算业务指标
        // 2. 返回计算结果
        return null
    }
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
    fun ${method.name}(<#list method.parameters as param>${param.name}: ${param.type}<#if param_has_next>, </#if></#list>): ${method.returnType} {
        // TODO: 实现 ${method.description} 的领域服务逻辑
        // 1. 业务规则验证
        // 2. 业务逻辑处理
        // 3. 返回处理结果
        return null as ${method.returnType}
    }
</#list>
## ----------  END 自定义方法  ----------
</#if>
}
