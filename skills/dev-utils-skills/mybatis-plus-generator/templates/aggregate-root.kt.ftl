package ${package.Domain}.model.aggregate.${entity?lower_case}

import java.io.Serializable
import java.time.LocalDateTime
<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.ApiModel
import io.swagger.annotations.ApiModelProperty
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.media.Schema
</#if>
</#if>

/**
 * <p>${table.comment}聚合根</p>
 * 
 * <p>${table.comment}聚合的根实体，是聚合的入口点，负责维护聚合内的业务不变性。
 * 聚合根封装了${table.comment}的核心业务逻辑和业务规则，确保数据一致性。</p>
 * 
 * <p>主要职责：
 * <ul>
 *   <li>维护聚合内的业务不变性</li>
 *   <li>封装业务逻辑和业务规则</li>
 *   <li>管理聚合内的实体和值对象</li>
 *   <li>发布领域事件</li>
<#list table.fields as field>
<#if field.keyFlag>
 *   <li>${field.comment}：聚合根唯一标识</li>
</#if>
</#list>
 * </ul>
 * </p>
 * 
 * <p>注意：聚合根是领域模型的核心，不应包含持久化相关的注解。持久化实体应放在基础设施层。</p>
 * 
 * @author ${author}
 * @since ${date}
 */
<#if swagger>
<#if swaggerVersion == "swagger2">
@ApiModel(value = "${entity}聚合根", description = "${table.comment}聚合根")
<#elseif swaggerVersion == "openapi3">
@Schema(description = "${table.comment}聚合根")
</#if>
</#if>
class ${entity} : Serializable {

    companion object {
        private const val serialVersionUID: Long = 1L

        /**
         * <p>创建${table.comment}聚合根</p>
         * 
         * <p>创建新的${table.comment}聚合根实例。此方法应包含必要的业务规则验证。</p>
         * 
         * @return ${table.comment}聚合根实例
         */
        fun create(): ${entity} {
            // TODO: 实现创建逻辑，包括业务规则验证
            val ${entity?substring(0,1)?lower_case}${entity?substring(1)} = ${entity}()
            // TODO: 初始化必要字段
            // TODO: 发布领域事件（如 ${entity}CreatedEvent）
            return ${entity?substring(0,1)?lower_case}${entity?substring(1)}
        }
    }

## ----------  BEGIN 聚合根字段  ----------
<#list table.fields as field>
<#if field.keyFlag>
<#assign keyPropertyName=field.propertyName>
</#if>
<#if field.comment?? && field.comment != "">
    /**
     * <p>${field.comment}</p>
     * 
     * <p>${field.comment}，<#if field.keyFlag>聚合根的唯一标识，</#if>用于标识${table.comment}聚合。</p>
     */
<#else>
    /**
     * <p>${field.propertyName}</p>
     */
</#if>
<#if swagger>
<#if swaggerVersion == "swagger2">
    @ApiModelProperty(value = "${field.comment}")
<#elseif swaggerVersion == "openapi3">
    @Schema(description = "${field.comment}")
</#if>
</#if>
    var ${field.propertyName}: ${field.propertyType}<#if field.propertyType == "String">?</#if> = <#if field.keyFlag && keyStrategy == "AUTO">null<#elseif field.propertyType == "String">null<#elseif field.propertyType == "Long" || field.propertyType == "Integer" || field.propertyType == "Int">0<#elseif field.propertyType == "Boolean">false<#elseif field.propertyType == "LocalDateTime">null<#else>null</#if>

</#list>
## ----------  END 聚合根字段  ----------

    /**
     * <p>更新${table.comment}信息</p>
     * 
     * <p>更新${table.comment}聚合根的信息。此方法应包含业务规则验证。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)} ${table.comment}聚合根对象
     */
    fun update(${entity?substring(0,1)?lower_case}${entity?substring(1)}: ${entity}) {
        // TODO: 实现更新逻辑，包括业务规则验证
        // TODO: 验证业务不变性
        // TODO: 更新字段
        // TODO: 发布领域事件（如 ${entity}UpdatedEvent）
    }

    /**
     * <p>删除${table.comment}</p>
     * 
     * <p>标记${table.comment}聚合根为已删除状态。此方法应包含业务规则验证。</p>
     */
    fun delete() {
        // TODO: 实现删除逻辑，包括业务规则验证
        // TODO: 验证是否可以删除（如检查关联关系）
        // TODO: 标记为已删除
        // TODO: 发布领域事件（如 ${entity}DeletedEvent）
    }
}
