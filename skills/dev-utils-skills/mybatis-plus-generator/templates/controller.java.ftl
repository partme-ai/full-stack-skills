package ${package.Controller};

import ${package.Entity}.${entity};
import ${package.Service}.${table.serviceName};
<#if swagger>
<#if swaggerVersion == "swagger2">
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
<#elseif swaggerVersion == "openapi3">
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;
</#if>
</#if>
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
<#if restControllerStyle>
import org.springframework.web.bind.annotation.RestController;
<#else>
import org.springframework.stereotype.Controller;
</#if>
<#if superControllerClassPackage??>
import ${superControllerClassPackage};
</#if>

/**
 * <p>${table.comment}控制器</p>
 * 
 * <p>提供${table.comment}相关的 REST API 接口，包括${table.comment}的创建、查询、更新和删除操作。
 * 本控制器遵循 RESTful 设计规范，使用标准的 HTTP 方法进行资源操作。</p>
 * 
 * <p>主要功能：
 * <ul>
 *   <li>创建${table.comment}</li>
 *   <li>根据ID查询${table.comment}信息</li>
 *   <li>更新${table.comment}信息</li>
 *   <li>删除${table.comment}</li>
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
@Api(value = "${table.comment}管理", tags = "${table.comment}管理接口")
<#elseif swaggerVersion == "openapi3">
@Tag(name = "${table.comment}管理", description = "${table.comment}管理接口")
</#if>
</#if>
<#if restControllerStyle>
@RestController
<#else>
@Controller
</#if>
@RequestMapping("<#if package.ModuleName??>/${package.ModuleName}</#if>/<#if controllerMappingHyphenStyle>${table.entityPath}<#else>${table.entityPath}</#if>"<#if superControllerClass??>, produces = "application/json;charset=UTF-8"</#if>)
<#if superControllerClass??>
public class ${table.controllerName} extends ${superControllerClass} {
<#else>
public class ${table.controllerName} {
</#if>

    @Autowired
    private ${table.serviceName} ${table.serviceName?substring(0,1)?lower_case}${table.serviceName?substring(1)};

    /**
     * <p>创建${table.comment}</p>
     * 
     * <p>接收${table.comment}创建请求，验证数据后创建新${table.comment}并返回${table.comment}信息。</p>
     * 
     * @param entity ${table.comment}实体对象
     * @return ${table.comment}实体对象
     */
<#if swagger>
<#if swaggerVersion == "swagger2">
    @ApiOperation(value = "创建${table.comment}", notes = "创建新的${table.comment}记录")
<#elseif swaggerVersion == "openapi3">
    @Operation(summary = "创建${table.comment}", description = "创建新的${table.comment}记录")
</#if>
</#if>
    @PostMapping
    public ${entity} create(@RequestBody ${entity} entity) {
        return ${table.serviceName?substring(0,1)?lower_case}${table.serviceName?substring(1)}.save(entity);
    }

    /**
     * <p>根据ID查询${table.comment}</p>
     * 
     * <p>根据提供的${table.comment}ID查询对应的${table.comment}详细信息。</p>
     * 
     * @param id ${table.comment}唯一标识符
     * @return ${table.comment}实体对象
     */
<#if swagger>
<#if swaggerVersion == "swagger2">
    @ApiOperation(value = "根据ID查询${table.comment}", notes = "根据ID查询${table.comment}详细信息")
    @ApiParam(name = "id", value = "${table.comment}ID", required = true)
<#elseif swaggerVersion == "openapi3">
    @Operation(summary = "根据ID查询${table.comment}", description = "根据ID查询${table.comment}详细信息")
    @Parameter(name = "id", description = "${table.comment}ID", required = true)
</#if>
</#if>
    @GetMapping("/{id}")
    public ${entity} getById(@PathVariable Long id) {
        return ${table.serviceName?substring(0,1)?lower_case}${table.serviceName?substring(1)}.getById(id);
    }

    /**
     * <p>更新${table.comment}</p>
     * 
     * <p>根据${table.comment}ID和更新请求，更新${table.comment}的指定字段信息。</p>
     * 
     * @param id ${table.comment}唯一标识符
     * @param entity ${table.comment}实体对象
     * @return 更新后的${table.comment}实体对象
     */
<#if swagger>
<#if swaggerVersion == "swagger2">
    @ApiOperation(value = "更新${table.comment}", notes = "更新${table.comment}信息")
<#elseif swaggerVersion == "openapi3">
    @Operation(summary = "更新${table.comment}", description = "更新${table.comment}信息")
</#if>
</#if>
    @PutMapping("/{id}")
    public ${entity} update(@PathVariable Long id, @RequestBody ${entity} entity) {
        entity.setId(id);
        return ${table.serviceName?substring(0,1)?lower_case}${table.serviceName?substring(1)}.updateById(entity) ? entity : null;
    }

    /**
     * <p>删除${table.comment}</p>
     * 
     * <p>根据${table.comment}ID删除指定的${table.comment}。删除操作会级联删除${table.comment}相关的数据。</p>
     * 
     * @param id ${table.comment}唯一标识符
     * @return 操作结果
     */
<#if swagger>
<#if swaggerVersion == "swagger2">
    @ApiOperation(value = "删除${table.comment}", notes = "根据ID删除${table.comment}")
<#elseif swaggerVersion == "openapi3">
    @Operation(summary = "删除${table.comment}", description = "根据ID删除${table.comment}")
</#if>
</#if>
    @DeleteMapping("/{id}")
    public boolean delete(@PathVariable Long id) {
        return ${table.serviceName?substring(0,1)?lower_case}${table.serviceName?substring(1)}.removeById(id);
    }
<#if customMethods??>

## ----------  BEGIN 自定义接口  ----------
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
     */
<#if swagger>
<#if swaggerVersion == "swagger2">
    @ApiOperation(value = "${method.description}", notes = "${method.detailDescription}")
<#elseif swaggerVersion == "openapi3">
    @Operation(summary = "${method.description}", description = "${method.detailDescription}")
</#if>
</#if>
    @GetMapping("/${method.mappingPath}")
    public ${method.returnType} ${method.name}(<#list method.parameters as param>@RequestParam ${param.type} ${param.name}<#if param_has_next>, </#if></#list>) {
        return ${table.serviceName?substring(0,1)?lower_case}${table.serviceName?substring(1)}.${method.name}(<#list method.parameters as param>${param.name}<#if param_has_next>, </#if></#list>);
    }
</#list>
## ----------  END 自定义接口  ----------
</#if>
}
