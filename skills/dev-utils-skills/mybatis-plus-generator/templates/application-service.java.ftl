package ${package.Application}.service;

import ${package.Domain}.model.aggregate.${entity?lower_case}.${entity};
import ${package.Application}.dto.${entity}DTO;
import java.util.List;

/**
 * <p>${table.comment}应用服务</p>
 * 
 * <p>${table.comment}的应用服务接口，位于应用层，负责协调领域对象完成业务用例。
 * 应用服务不包含业务逻辑，只负责编排领域服务和聚合根完成业务流程。</p>
 * 
 * <p>主要职责：
 * <ul>
 *   <li>协调领域对象完成业务用例</li>
 *   <li>处理事务边界</li>
 *   <li>DTO 与领域对象的转换</li>
 *   <li>调用领域服务和聚合根</li>
 *   <li>分页查询${table.comment}</li>
 *   <li>批量创建${table.comment}</li>
 *   <li>批量更新${table.comment}</li>
 *   <li>批量删除${table.comment}</li>
 *   <li>判断${table.comment}是否存在</li>
 *   <li>统计${table.comment}数量</li>
<#if customMethods??>
<#list customMethods as method>
 *   <li>${method.description}</li>
</#list>
</#if>
 * </ul>
 * </p>
 * 
 * <p>注意：应用服务不应包含业务逻辑，业务逻辑应在领域层实现。</p>
 * 
 * @author ${author}
 * @since ${date}
 */
public interface ${entity}ApplicationService {

    /**
     * <p>创建${table.comment}</p>
     * 
     * <p>创建新的${table.comment}聚合根，并返回DTO对象。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)}DTO ${table.comment}DTO对象
     * @return ${table.comment}DTO对象
     */
    ${entity}DTO create${entity}(${entity}DTO ${entity?substring(0,1)?lower_case}${entity?substring(1)}DTO);

    /**
     * <p>根据ID查询${table.comment}</p>
     * 
     * <p>根据${table.comment}ID查询${table.comment}聚合根，并转换为DTO返回。</p>
     * 
     * @param id ${table.comment}ID
     * @return ${table.comment}DTO对象
     */
    ${entity}DTO get${entity}ById(Long id);

    /**
     * <p>更新${table.comment}</p>
     * 
     * <p>更新${table.comment}聚合根的信息。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)}DTO ${table.comment}DTO对象
     * @return ${table.comment}DTO对象
     */
    ${entity}DTO update${entity}(${entity}DTO ${entity?substring(0,1)?lower_case}${entity?substring(1)}DTO);

    /**
     * <p>删除${table.comment}</p>
     * 
     * <p>根据${table.comment}ID删除${table.comment}聚合根。</p>
     * 
     * @param id ${table.comment}ID
     */
    void delete${entity}(Long id);

    /**
     * <p>查询所有${table.comment}</p>
     * 
     * <p>查询所有${table.comment}聚合根列表，并转换为DTO列表返回。</p>
     * 
     * @return ${table.comment}DTO列表
     */
    List<${entity}DTO> getAll${entity}s();

    /**
     * <p>分页查询${table.comment}</p>
     * 
     * <p>分页查询${table.comment}聚合根列表，并转换为DTO列表返回。</p>
     * 
     * @param pageNum 页码（从1开始）
     * @param pageSize 每页数量
     * @return ${table.comment}DTO分页列表
     */
    List<${entity}DTO> get${entity}sByPage(Integer pageNum, Integer pageSize);

    /**
     * <p>批量创建${table.comment}</p>
     * 
     * <p>批量创建新的${table.comment}聚合根，并返回DTO列表。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)}DTOList ${table.comment}DTO列表
     * @return ${table.comment}DTO列表
     */
    List<${entity}DTO> batchCreate${entity}s(List<${entity}DTO> ${entity?substring(0,1)?lower_case}${entity?substring(1)}DTOList);

    /**
     * <p>批量更新${table.comment}</p>
     * 
     * <p>批量更新${table.comment}聚合根的信息。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)}DTOList ${table.comment}DTO列表
     * @return ${table.comment}DTO列表
     */
    List<${entity}DTO> batchUpdate${entity}s(List<${entity}DTO> ${entity?substring(0,1)?lower_case}${entity?substring(1)}DTOList);

    /**
     * <p>批量删除${table.comment}</p>
     * 
     * <p>根据${table.comment}ID列表批量删除${table.comment}聚合根。</p>
     * 
     * @param ids ${table.comment}ID列表
     */
    void batchDelete${entity}s(List<Long> ids);

    /**
     * <p>判断${table.comment}是否存在</p>
     * 
     * <p>根据${table.comment}ID判断${table.comment}聚合根是否存在。</p>
     * 
     * @param id ${table.comment}ID
     * @return boolean 是否存在
     */
    boolean exists${entity}(Long id);

    /**
     * <p>统计${table.comment}数量</p>
     * 
     * <p>统计${table.comment}聚合根的总数量。</p>
     * 
     * @return long ${table.comment}数量
     */
    long count${entity}s();
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
    ${method.returnType} ${method.name}(<#list method.parameters as param>${param.type} ${param.name}<#if param_has_next>, </#if></#list>);
</#list>
## ----------  END 自定义方法  ----------
</#if>
}
