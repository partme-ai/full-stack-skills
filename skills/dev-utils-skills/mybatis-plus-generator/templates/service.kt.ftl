package ${package.Service}

import ${package.Entity}.${entity}
import ${superServiceClassPackage}
<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.Api
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.tags.Tag
</#if>
</#if>

/**
 * <p>${table.comment}服务接口</p>
 * 
 * <p>定义${table.comment}相关的业务逻辑接口，包括${table.comment}的增删改查操作。
 * 本接口遵循领域驱动设计（DDD）原则，封装${table.comment}领域的核心业务逻辑。</p>
 * 
 * <p>主要职责：
 * <ul>
 *   <li>${table.comment}创建和保存</li>
 *   <li>${table.comment}信息查询（包括条件查询）</li>
 *   <li>${table.comment}信息更新</li>
 *   <li>${table.comment}删除</li>
<#if customMethods??>
<#list customMethods as method>
 *   <li>${method.description}</li>
</#list>
</#if>
 * </ul>
 * </p>
 * 
 * @author ${author}
 * @since ${date}
 */
<#if swagger>
<#if swaggerVersion == "swagger2">
@Api(value = "${table.comment}服务接口", tags = "${table.comment}管理")
<#elseif swaggerVersion == "openapi3">
@Tag(name = "${table.comment}管理", description = "${table.comment}服务接口")
</#if>
</#if>
interface ${table.serviceName} : ${superServiceClass}<${entity}> {
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
