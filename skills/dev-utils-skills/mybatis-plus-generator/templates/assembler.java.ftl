package ${package.Interfaces}.assembler;

import ${package.Domain}.model.aggregate.${entity?lower_case}.${entity};
import ${package.Interfaces}.web.dto.request.${entity}RequestDTO;
import ${package.Interfaces}.web.dto.response.${entity}ResponseDTO;
import ${package.Application}.dto.${entity}DTO;
import org.springframework.stereotype.Component;

/**
 * <p>${table.comment}DTO装配器</p>
 * 
 * <p>负责${table.comment}聚合根与DTO之间的转换，位于接口层。
 * 装配器封装了领域对象与DTO之间的转换逻辑，保持领域模型的纯净性。</p>
 * 
 * <p>主要职责：
 * <ul>
 *   <li>聚合根转换为DTO</li>
 *   <li>DTO转换为聚合根</li>
 *   <li>处理DTO与领域对象的映射关系</li>
 * </ul>
 * </p>
 * 
 * @author ${author}
 * @since ${date}
 */
@Component
public class ${entity}Assembler {

    /**
     * <p>聚合根转换为响应DTO</p>
     * 
     * <p>将${table.comment}聚合根转换为响应DTO，用于API响应。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)} ${table.comment}聚合根对象
     * @return ${table.comment}响应DTO对象
     */
    public ${entity}ResponseDTO toResponseDTO(${entity} ${entity?substring(0,1)?lower_case}${entity?substring(1)}) {
        if (${entity?substring(0,1)?lower_case}${entity?substring(1)} == null) {
            return null;
        }
        
        ${entity}ResponseDTO dto = new ${entity}ResponseDTO();
        // TODO: 实现聚合根到响应DTO的转换逻辑
<#list table.fields as field>
        dto.set${field.propertyName?substring(0,1)?upper_case}${field.propertyName?substring(1)}(${entity?substring(0,1)?lower_case}${entity?substring(1)}.get${field.propertyName?substring(0,1)?upper_case}${field.propertyName?substring(1)}());
</#list>
        return dto;
    }

    /**
     * <p>请求DTO转换为聚合根</p>
     * 
     * <p>将请求DTO转换为${table.comment}聚合根，用于创建或更新操作。</p>
     * 
     * @param requestDTO ${table.comment}请求DTO对象
     * @return ${table.comment}聚合根对象
     */
    public ${entity} toAggregate(${entity}RequestDTO requestDTO) {
        if (requestDTO == null) {
            return null;
        }
        
        ${entity} ${entity?substring(0,1)?lower_case}${entity?substring(1)} = new ${entity}();
        // TODO: 实现请求DTO到聚合根的转换逻辑
<#list table.fields as field>
        ${entity?substring(0,1)?lower_case}${entity?substring(1)}.set${field.propertyName?substring(0,1)?upper_case}${field.propertyName?substring(1)}(requestDTO.get${field.propertyName?substring(0,1)?upper_case}${field.propertyName?substring(1)}());
</#list>
        return ${entity?substring(0,1)?lower_case}${entity?substring(1)};
    }

    /**
     * <p>应用DTO转换为聚合根</p>
     * 
     * <p>将应用层DTO转换为${table.comment}聚合根。</p>
     * 
     * @param dto ${table.comment}应用DTO对象
     * @return ${table.comment}聚合根对象
     */
    public ${entity} toAggregate(${entity}DTO dto) {
        if (dto == null) {
            return null;
        }
        
        ${entity} ${entity?substring(0,1)?lower_case}${entity?substring(1)} = new ${entity}();
        // TODO: 实现应用DTO到聚合根的转换逻辑
<#list table.fields as field>
        ${entity?substring(0,1)?lower_case}${entity?substring(1)}.set${field.propertyName?substring(0,1)?upper_case}${field.propertyName?substring(1)}(dto.get${field.propertyName?substring(0,1)?upper_case}${field.propertyName?substring(1)}());
</#list>
        return ${entity?substring(0,1)?lower_case}${entity?substring(1)};
    }

    /**
     * <p>聚合根转换为应用DTO</p>
     * 
     * <p>将${table.comment}聚合根转换为应用层DTO。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)} ${table.comment}聚合根对象
     * @return ${table.comment}应用DTO对象
     */
    public ${entity}DTO toDTO(${entity} ${entity?substring(0,1)?lower_case}${entity?substring(1)}) {
        if (${entity?substring(0,1)?lower_case}${entity?substring(1)} == null) {
            return null;
        }
        
        ${entity}DTO dto = new ${entity}DTO();
        // TODO: 实现聚合根到应用DTO的转换逻辑
<#list table.fields as field>
        dto.set${field.propertyName?substring(0,1)?upper_case}${field.propertyName?substring(1)}(${entity?substring(0,1)?lower_case}${entity?substring(1)}.get${field.propertyName?substring(0,1)?upper_case}${field.propertyName?substring(1)}());
</#list>
        return dto;
    }
}
