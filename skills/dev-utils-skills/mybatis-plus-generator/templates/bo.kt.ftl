package ${package.BO}

<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.ApiModel
import io.swagger.annotations.ApiModelProperty
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.media.Schema
</#if>
</#if>
import java.io.Serializable

/**
 * <p>${table.comment}业务对象</p>
 * 
 * <p>封装${table.comment}的业务逻辑对象，包含业务规则和业务方法。
 * 本BO用于业务层处理，包含业务逻辑和业务规则验证。</p>
 * 
 * @author ${author}
 * @since ${date}
 */
<#if swagger>
<#if swaggerVersion == "swagger2">
@ApiModel(value = "${table.comment}BO", description = "${table.comment}业务对象")
<#elseif swaggerVersion == "openapi3">
@Schema(description = "${table.comment}业务对象")
</#if>
</#if>
<#if entityLombokModel>
data class ${entity}BO(
<#else>
class ${entity}BO : Serializable {
</#if>

<#if serialVersionUID>
    companion object {
        private const val serialVersionUID: Long = 1L
    }
</#if>
## ----------  BEGIN BO 字段  ----------
<#if entityLombokModel>
<#list boFields as field>
<#if field.comment?? && field.comment != "">
    /**
     * <p>${field.comment}</p>
     * 
     * <p>${field.comment}，用于业务逻辑处理</p>
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
    var ${field.propertyName}: ${field.propertyType}<#if field.propertyType == "String">?</#if> = null<#if field_has_next>,</#if>

</#list>
) : Serializable
<#else>
<#list boFields as field>
<#if field.comment?? && field.comment != "">
    /**
     * <p>${field.comment}</p>
     * 
     * <p>${field.comment}，用于业务逻辑处理</p>
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
    var ${field.propertyName}: ${field.propertyType}<#if field.propertyType == "String">?</#if> = null

</#list>
</#if>
## ----------  END BO 字段  ----------
<#if !entityLombokModel>
}
</#if>
