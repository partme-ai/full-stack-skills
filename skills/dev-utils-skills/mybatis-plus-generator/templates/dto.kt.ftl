package ${package.DTO}

<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.ApiModel
import io.swagger.annotations.ApiModelProperty
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.media.Schema
</#if>
</#if>
<#if validation>
import javax.validation.constraints.*
</#if>
import java.io.Serializable
import java.time.LocalDateTime

/**
 * <p>${table.comment}${dtoType}DTO</p>
 * 
 * <p>用于${dtoPurpose}的数据传输对象。
 * 本DTO包含${table.comment}的${dtoFields}字段，用于${dtoUsage}场景。</p>
 * 
 * @author ${author}
 * @since ${date}
 */
<#if swagger>
<#if swaggerVersion == "swagger2">
@ApiModel(value = "${table.comment}${dtoType}DTO", description = "${table.comment}${dtoType}数据传输对象")
<#elseif swaggerVersion == "openapi3">
@Schema(description = "${table.comment}${dtoType}数据传输对象")
</#if>
</#if>
<#if entityLombokModel>
data class ${entity}${dtoType}DTO(
<#else>
class ${entity}${dtoType}DTO : Serializable {
</#if>

<#if serialVersionUID>
    companion object {
        private const val serialVersionUID: Long = 1L
    }
</#if>
## ----------  BEGIN DTO 字段  ----------
<#if entityLombokModel>
<#list dtoFields as field>
<#if field.comment?? && field.comment != "">
    /**
     * <p>${field.comment}</p>
     * 
     * <p>${field.comment}，${field.type}类型<#if field.propertyType == "String">，长度限制为 ${field.length} 个字符</#if></p>
     */
<#else>
    /**
     * <p>${field.propertyName}</p>
     */
</#if>
<#if swagger>
<#if swaggerVersion == "swagger2">
    @ApiModelProperty(value = "${field.comment}"<#if field.required?? && field.required>, required = true</#if>)
<#elseif swaggerVersion == "openapi3">
    @Schema(description = "${field.comment}"<#if field.required?? && field.required>, required = true</#if>)
</#if>
</#if>
<#if validation>
<#if field.required?? && field.required>
    @get:NotNull(message = "${field.comment}不能为空")
<#if field.propertyType == "String">
    @get:NotBlank(message = "${field.comment}不能为空")
</#if>
</#if>
<#if field.propertyType == "String" && field.length??>
    @get:Size(max = ${field.length}, message = "${field.comment}长度不能超过${field.length}个字符")
</#if>
</#if>
    var ${field.propertyName}: ${field.propertyType}<#if field.propertyType == "String">?</#if><#if field.required?? && field.required><#else> = null</#if><#if field_has_next>,</#if>

</#list>
) : Serializable
<#else>
<#list dtoFields as field>
<#if field.comment?? && field.comment != "">
    /**
     * <p>${field.comment}</p>
     * 
     * <p>${field.comment}，${field.type}类型<#if field.propertyType == "String">，长度限制为 ${field.length} 个字符</#if></p>
     */
<#else>
    /**
     * <p>${field.propertyName}</p>
     */
</#if>
<#if swagger>
<#if swaggerVersion == "swagger2">
    @ApiModelProperty(value = "${field.comment}"<#if field.required?? && field.required>, required = true</#if>)
<#elseif swaggerVersion == "openapi3">
    @Schema(description = "${field.comment}"<#if field.required?? && field.required>, required = true</#if>)
</#if>
</#if>
<#if validation>
<#if field.required?? && field.required>
    @NotNull(message = "${field.comment}不能为空")
<#if field.propertyType == "String">
    @NotBlank(message = "${field.comment}不能为空")
</#if>
</#if>
<#if field.propertyType == "String" && field.length??>
    @Size(max = ${field.length}, message = "${field.comment}长度不能超过${field.length}个字符")
</#if>
</#if>
    var ${field.propertyName}: ${field.propertyType}<#if field.propertyType == "String">?</#if> = <#if field.required?? && field.required><#if field.propertyType == "String">null<#elseif field.propertyType == "Long" || field.propertyType == "Integer" || field.propertyType == "Int">0<#elseif field.propertyType == "Boolean">false<#else>null</#if><#else>null</#if>

</#list>
</#if>
## ----------  END DTO 字段  ----------
<#if !entityLombokModel>
}
</#if>
