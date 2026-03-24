package ${package.ServiceImpl}

import ${package.Entity}.${entity}
import ${package.Mapper}.${table.mapperName}
import ${package.Service}.${table.serviceName}
import ${superServiceImplClassPackage}
import org.springframework.stereotype.Service
<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.Api
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.tags.Tag
</#if>
</#if>

/**
 * <p>${table.comment}服务实现类</p>
 * 
 * <p>实现 ${table.serviceName} 接口，提供${table.comment}相关的业务逻辑实现。
 * 本类负责处理${table.comment}创建、查询、更新、删除等核心业务操作。</p>
 * 
 * <p>主要功能：
 * <ul>
 *   <li>${table.comment}创建：包括数据验证、业务规则检查</li>
 *   <li>${table.comment}查询：支持按ID查询、条件查询、分页查询</li>
 *   <li>${table.comment}更新：支持部分字段更新、业务规则验证</li>
 *   <li>${table.comment}删除：级联删除相关数据</li>
<#if customMethods??>
<#list customMethods as method>
 *   <li>${method.description}：${method.detailDescription}</li>
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
@Api(value = "${table.comment}服务实现类", tags = "${table.comment}管理")
<#elseif swaggerVersion == "openapi3">
@Tag(name = "${table.comment}管理", description = "${table.comment}服务实现类")
</#if>
</#if>
@Service
class ${table.serviceImplName} : ${superServiceImplClass}<${table.mapperName}, ${entity}>(), ${table.serviceName} {

<#if customMethods??>
## ----------  BEGIN 自定义方法实现  ----------
<#list customMethods as method>
    /**
     * <p>${method.description}</p>
     * 
     * <p>${method.detailDescription}</p>
     * 
     * <p>实现逻辑：
     * <ol>
     *   <li>参数验证：检查输入参数的有效性</li>
     *   <li>业务逻辑：执行具体的业务操作</li>
     *   <li>数据持久化：调用 Mapper 层进行数据操作</li>
     *   <li>结果返回：返回处理结果</li>
     * </ol>
     * </p>
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
    override fun ${method.name}(<#list method.parameters as param>${param.name}: ${param.type}<#if param_has_next>, </#if></#list>): ${method.returnType} {
        // TODO: 实现 ${method.description} 的业务逻辑
        // 1. 参数验证
<#if method.parameters??>
<#list method.parameters as param>
        requireNotNull(${param.name}) { "${param.description}不能为空" }
<#if param.type == "String">
        require(${param.name}.isNotEmpty()) { "${param.description}不能为空" }
</#if>
</#list>
</#if>
        
        // 2. 业务逻辑处理
        // TODO: 根据业务需求实现具体逻辑
        
        // 3. 数据持久化
        // TODO: 调用 Mapper 层进行数据操作
        
        // 4. 返回结果
        // TODO: 返回处理结果
        return null as ${method.returnType}
    }
</#list>
## ----------  END 自定义方法实现  ----------
</#if>
}
