package ${package.Domain}.model.valueobject;

import java.io.Serializable;
<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.media.Schema;
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
public class ${valueObjectName} implements Serializable {

    private static final long serialVersionUID = 1L;

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
    private final ${field.propertyType} ${field.propertyName};
</#list>
## ----------  END 值对象字段  ----------

    /**
     * <p>创建${valueObjectName}值对象</p>
     * 
     * <p>创建新的${valueObjectName}值对象实例。值对象创建后不可修改。</p>
     * 
<#list valueObjectFields as field>
     * @param ${field.propertyName} ${field.comment}
</#list>
     */
    public ${valueObjectName}(<#list valueObjectFields as field>${field.propertyType} ${field.propertyName}<#if field_has_next>, </#if></#list>) {
        // TODO: 实现值对象构造逻辑，包括参数验证
<#list valueObjectFields as field>
        this.${field.propertyName} = ${field.propertyName};
</#list>
    }

## ----------  BEGIN Getter 方法  ----------
<#list valueObjectFields as field>
    /**
     * <p>获取${field.comment}</p>
     * 
     * @return ${field.propertyType} ${field.comment}
     */
    public ${field.propertyType} get${field.propertyName?substring(0,1)?upper_case}${field.propertyName?substring(1)}() {
        return ${field.propertyName};
    }
</#list>
## ----------  END Getter 方法  ----------

    /**
     * <p>值相等性比较</p>
     * 
     * <p>值对象通过属性值比较相等性，而非引用比较。</p>
     * 
     * @param obj 比较对象
     * @return boolean 是否相等
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        ${valueObjectName} that = (${valueObjectName}) obj;
        // TODO: 实现属性值比较逻辑
<#list valueObjectFields as field>
<#if field.propertyType == "String">
        if (${field.propertyName} != null ? !${field.propertyName}.equals(that.${field.propertyName}) : that.${field.propertyName} != null) {
            return false;
        }
<#else>
        if (${field.propertyName} != that.${field.propertyName}) {
            return false;
        }
</#if>
</#list>
        return true;
    }

    /**
     * <p>计算哈希值</p>
     * 
     * <p>值对象的哈希值基于所有属性值计算。</p>
     * 
     * @return int 哈希值
     */
    @Override
    public int hashCode() {
        // TODO: 实现哈希值计算逻辑
        int result = 17;
<#list valueObjectFields as field>
<#if field.propertyType == "String">
        result = 31 * result + (${field.propertyName} != null ? ${field.propertyName}.hashCode() : 0);
<#else>
        result = 31 * result + (int) (${field.propertyName} ^ (${field.propertyName} >>> 32));
</#if>
</#list>
        return result;
    }

    /**
     * <p>转换为字符串</p>
     * 
     * @return String 字符串表示
     */
    @Override
    public String toString() {
        return "${valueObjectName}{" +
<#list valueObjectFields as field>
                "${field.propertyName}=" + ${field.propertyName} +
<#if field_has_next> ", " + </#if>
</#list>
                '}';
    }
}
