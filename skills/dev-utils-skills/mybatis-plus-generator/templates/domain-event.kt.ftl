package ${package.Domain}.model.event

import java.io.Serializable
import java.time.LocalDateTime

/**
 * <p>${eventName}领域事件</p>
 * 
 * <p>${eventDescription}，领域事件用于表示领域模型中发生的重要业务事件。
 * 领域事件是领域层的一部分，用于实现领域对象之间的解耦通信。</p>
 * 
 * <p>领域事件特性：
 * <ul>
 *   <li>不可变性：领域事件创建后不可修改</li>
 *   <li>时间戳：记录事件发生的时间</li>
 *   <li>事件源：记录触发事件的聚合根信息</li>
 *   <li>事件数据：包含事件相关的业务数据</li>
 * </ul>
 * </p>
 * 
 * @author ${author}
 * @since ${date}
 */
data class ${eventName} private constructor(
    /**
     * <p>事件ID</p>
     * 
     * <p>事件的唯一标识符</p>
     */
    val eventId: String,

    /**
     * <p>聚合根ID</p>
     * 
     * <p>触发事件的聚合根ID</p>
     */
    val aggregateId: Long,

    /**
     * <p>事件发生时间</p>
     * 
     * <p>记录事件发生的时间戳</p>
     */
    val occurredOn: LocalDateTime,
## ----------  BEGIN 事件数据字段  ----------
<#list eventFields as field>
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
    val ${field.propertyName}: ${field.propertyType}<#if field.propertyType == "String">?</#if><#if field_has_next>,</#if>

</#list>
## ----------  END 事件数据字段  ----------
) : Serializable {

    companion object {
        private const val serialVersionUID: Long = 1L

        /**
         * <p>创建${eventName}领域事件</p>
         * 
         * <p>创建新的${eventName}领域事件实例。</p>
         * 
         * @param aggregateId 聚合根ID
<#list eventFields as field>
         * @param ${field.propertyName} ${field.comment}
</#list>
         * @return ${eventName}领域事件实例
         */
        fun create(aggregateId: Long<#list eventFields as field>, ${field.propertyName}: ${field.propertyType}<#if field.propertyType == "String">?</#if></#list>): ${eventName} {
            return ${eventName}(
                eventId = java.util.UUID.randomUUID().toString(),
                aggregateId = aggregateId,
                occurredOn = LocalDateTime.now(),
<#list eventFields as field>
                ${field.propertyName} = ${field.propertyName}<#if field_has_next>,</#if>
</#list>
            )
        }
    }
}
