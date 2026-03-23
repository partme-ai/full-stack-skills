package ${package.Entity};

import com.baomidou.mybatisplus.annotation.*;
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
import lombok.EqualsAndHashCode;
</#if>
import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * <p>${table.comment}实体类</p>
 * 
 * <p>对应数据库中的 ${table.name} 表，用于存储${table.comment}。
 * 本实体类使用 MyBatis-Plus 注解进行 ORM 映射，支持自动建表和字段映射。</p>
 * 
 * <p>主要字段：
 * <ul>
<#list table.fields as field>
 *   <li>${field.propertyName}: ${field.comment}</li>
</#list>
 * </ul>
 * </p>
 * 
 * @author ${author}
 * @since ${date}
 */
<#if entityLombokModel>
@Data
<#if superEntityClass??>
@EqualsAndHashCode(callSuper = true)
<#else>
@EqualsAndHashCode(callSuper = false)
</#if>
</#if>
<#if table.convert>
@TableName("${schemaName}${table.name}")
</#if>
<#if swagger>
<#if swaggerVersion == "swagger2">
@ApiModel(value = "${entity}对象", description = "${table.comment}")
<#elseif swaggerVersion == "openapi3">
@Schema(description = "${table.comment}")
</#if>
</#if>
<#if superEntityClass??>
public class ${entity} extends ${superEntityClass} {
<#elseif activeRecord>
public class ${entity} extends Model<${entity}> {
<#else>
public class ${entity} implements Serializable {
</#if>

<#if serialVersionUID>
    private static final long serialVersionUID = 1L;
</#if>
## ----------  BEGIN 字段循环遍历  ----------
<#list table.fields as field>
<#if field.keyFlag>
<#assign keyPropertyName=field.propertyName>
</#if>
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
    @ApiModelProperty(value = "${field.comment}")
<#elseif swaggerVersion == "openapi3">
    @Schema(description = "${field.comment}")
</#if>
</#if>
<#if field.keyFlag>
    @TableId(value = "${field.name}", type = IdType.${keyStrategy})
<#elseif field.fill??>
<#if field.convert>
    @TableField(value = "${field.name}", fill = FieldFill.${field.fill})
<#else>
    @TableField(fill = FieldFill.${field.fill})
</#if>
<#elseif field.convert>
    @TableField("${field.name}")
</#if>
<#if field.versionField>
    @Version
</#if>
<#if field.logicDeleteField>
    @TableLogic
</#if>
    private ${field.propertyType} ${field.propertyName};
</#list>
## ----------  END 字段循环遍历  ----------
}
