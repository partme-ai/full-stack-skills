package ${package.VO}

<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.ApiModel
import io.swagger.annotations.ApiModelProperty
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.media.Schema
</#if>
</#if>
import java.io.Serializable
import java.time.LocalDateTime

/**
 * <p>${table.comment}视图对象</p>
 * 
 * <p>用于${table.comment}的视图展示，包含${table.comment}的展示字段。
 * 本VO用于API响应，包含格式化后的数据和展示逻辑。</p>
 * 
 * @author ${author}
 * @since ${date}
 */
<#if swagger>
<#if swaggerVersion == "swagger2">
@ApiModel(value = "${table.comment}VO", description = "${table.comment}视图对象")
<#elseif swaggerVersion == "openapi3">
@Schema(description = "${table.comment}视图对象")
</#if>
</#if>
<#if entityLombokModel>
data class ${entity}VO(
<#else>
class ${entity}VO : Serializable {
</#if>

<#if serialVersionUID>
    companion object {
        private const val serialVersionUID: Long = 1L
    }
</#if>
## ----------  BEGIN VO 字段  ----------
<#if entityLombokModel>
<#list voFields as field>
<#if field.comment?? && field.comment != "">
    /**
     * <p>${field.comment}</p>
     * 
     * <p>${field.comment}，用于视图展示</p>
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
<#list voFields as field>
<#if field.comment?? && field.comment != "">
    /**
     * <p>${field.comment}</p>
     * 
     * <p>${field.comment}，用于视图展示</p>
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
## ----------  END VO 字段  ----------
<#if !entityLombokModel>
}
</#if>
