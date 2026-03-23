package ${package.DTO};

<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.media.Schema;
</#if>
</#if>
<#if entityLombokModel>
import lombok.Data;
</#if>
<#if validation>
import javax.validation.constraints.*;
</#if>
import java.io.Serializable;
import java.time.LocalDateTime;

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
@Data
</#if>
public class ${entity}${dtoType}DTO implements Serializable {

<#if serialVersionUID>
    private static final long serialVersionUID = 1L;
</#if>
## ----------  BEGIN DTO 字段  ----------
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
    private ${field.propertyType} ${field.propertyName};
</#list>
## ----------  END DTO 字段  ----------
}
