package ${package.Domain}.model.valueobject

import java.io.Serializable
<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.ApiModel
import io.swagger.annotations.ApiModelProperty
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.media.Schema
</#if>
</#if>

/**
 * <p>${valueObjectName}值对象</p>
 * 
 * <p>${valueObjectDescription}，值对象是不可变的，通过值相等性进行比较。
 * 值对象没有唯一标识，通过其属性值来标识。</p>
 * 
 * <p>值对象特性：
 * <ul>
 *   <li>不可变性：值对象创建后不可修改</li>
 *   <li>值相等性：通过属性值比较相等性，而非引用</li>
 *   <li>无唯一标识：值对象没有ID，通过属性值标识</li>
 *   <li>自包含：值对象包含完整的业务含义</li>
 * </ul>
 * </p>
 * 
 * @author ${author}
 * @since ${date}
 */
<#if swagger>
<#if swaggerVersion == "swagger2">
@ApiModel(value = "${valueObjectName}值对象", description = "${valueObjectDescription}")
<#elseif swaggerVersion == "openapi3">
@Schema(description = "${valueObjectDescription}")
</#if>
</#if>
data class ${valueObjectName} private constructor(
## ----------  BEGIN 值对象字段  ----------
<#list valueObjectFields as field>
<#if field.comment?? && field.comment != "">
    /**
     * <p>${field.comment}</p>
     * 
     * <p>${field.comment}，${field.type}类型</p>
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
    val ${field.propertyName}: ${field.propertyType}<#if field.propertyType == "String">?</#if><#if field_has_next>,</#if>

</#list>
## ----------  END 值对象字段  ----------
) : Serializable {

    companion object {
        private const val serialVersionUID: Long = 1L

        /**
         * <p>创建${valueObjectName}值对象</p>
         * 
         * <p>创建新的${valueObjectName}值对象实例。值对象创建后不可修改。</p>
         * 
<#list valueObjectFields as field>
         * @param ${field.propertyName} ${field.comment}
</#list>
         * @return ${valueObjectName}值对象实例
         */
        fun create(<#list valueObjectFields as field>${field.propertyName}: ${field.propertyType}<#if field.propertyType == "String">?</#if><#if field_has_next>, </#if></#list>): ${valueObjectName} {
            // TODO: 实现值对象构造逻辑，包括参数验证
            return ${valueObjectName}(
<#list valueObjectFields as field>
                ${field.propertyName}<#if field_has_next>,</#if>
</#list>
            )
        }
    }
}
