package ${package.Interfaces}.assembler

import ${package.Domain}.model.aggregate.${entity?lower_case}.${entity}
import ${package.Interfaces}.web.dto.request.${entity}RequestDTO
import ${package.Interfaces}.web.dto.response.${entity}ResponseDTO
import ${package.Application}.dto.${entity}DTO
import org.springframework.stereotype.Component

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
class ${entity}Assembler {

    /**
     * <p>聚合根转换为响应DTO</p>
     * 
     * <p>将${table.comment}聚合根转换为响应DTO，用于API响应。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)} ${table.comment}聚合根对象
     * @return ${table.comment}响应DTO对象
     */
    fun toResponseDTO(${entity?substring(0,1)?lower_case}${entity?substring(1)}: ${entity}?): ${entity}ResponseDTO? {
        if (${entity?substring(0,1)?lower_case}${entity?substring(1)} == null) {
            return null
        }
        
        val dto = ${entity}ResponseDTO()
        // TODO: 实现聚合根到响应DTO的转换逻辑
<#list table.fields as field>
        dto.${field.propertyName} = ${entity?substring(0,1)?lower_case}${entity?substring(1)}.${field.propertyName}
</#list>
        return dto
    }

    /**
     * <p>请求DTO转换为聚合根</p>
     * 
     * <p>将请求DTO转换为${table.comment}聚合根，用于创建或更新操作。</p>
     * 
     * @param requestDTO ${table.comment}请求DTO对象
     * @return ${table.comment}聚合根对象
     */
    fun toAggregate(requestDTO: ${entity}RequestDTO?): ${entity}? {
        if (requestDTO == null) {
            return null
        }
        
        val ${entity?substring(0,1)?lower_case}${entity?substring(1)} = ${entity}()
        // TODO: 实现请求DTO到聚合根的转换逻辑
<#list table.fields as field>
        ${entity?substring(0,1)?lower_case}${entity?substring(1)}.${field.propertyName} = requestDTO.${field.propertyName}
</#list>
        return ${entity?substring(0,1)?lower_case}${entity?substring(1)}
    }

    /**
     * <p>应用DTO转换为聚合根</p>
     * 
     * <p>将应用层DTO转换为${table.comment}聚合根。</p>
     * 
     * @param dto ${table.comment}应用DTO对象
     * @return ${table.comment}聚合根对象
     */
    fun toAggregate(dto: ${entity}DTO?): ${entity}? {
        if (dto == null) {
            return null
        }
        
        val ${entity?substring(0,1)?lower_case}${entity?substring(1)} = ${entity}()
        // TODO: 实现应用DTO到聚合根的转换逻辑
<#list table.fields as field>
        ${entity?substring(0,1)?lower_case}${entity?substring(1)}.${field.propertyName} = dto.${field.propertyName}
</#list>
        return ${entity?substring(0,1)?lower_case}${entity?substring(1)}
    }

    /**
     * <p>聚合根转换为应用DTO</p>
     * 
     * <p>将${table.comment}聚合根转换为应用层DTO。</p>
     * 
     * @param ${entity?substring(0,1)?lower_case}${entity?substring(1)} ${table.comment}聚合根对象
     * @return ${table.comment}应用DTO对象
     */
    fun toDTO(${entity?substring(0,1)?lower_case}${entity?substring(1)}: ${entity}?): ${entity}DTO? {
        if (${entity?substring(0,1)?lower_case}${entity?substring(1)} == null) {
            return null
        }
        
        val dto = ${entity}DTO()
        // TODO: 实现聚合根到应用DTO的转换逻辑
<#list table.fields as field>
        dto.${field.propertyName} = ${entity?substring(0,1)?lower_case}${entity?substring(1)}.${field.propertyName}
</#list>
        return dto
    }
}
