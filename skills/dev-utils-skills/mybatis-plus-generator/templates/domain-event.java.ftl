package ${package.Domain}.model.event;

import java.io.Serializable;
import java.time.LocalDateTime;

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
public class ${eventName} implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * <p>事件ID</p>
     * 
     * <p>事件的唯一标识符</p>
     */
    private String eventId;

    /**
     * <p>聚合根ID</p>
     * 
     * <p>触发事件的聚合根ID</p>
     */
    private Long aggregateId;

    /**
     * <p>事件发生时间</p>
     * 
     * <p>记录事件发生的时间戳</p>
     */
    private LocalDateTime occurredOn;

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
    private ${field.propertyType} ${field.propertyName};
</#list>
## ----------  END 事件数据字段  ----------

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
    public static ${eventName} create(Long aggregateId<#list eventFields as field>, ${field.propertyType} ${field.propertyName}</#list>) {
        ${eventName} event = new ${eventName}();
        event.eventId = java.util.UUID.randomUUID().toString();
        event.aggregateId = aggregateId;
        event.occurredOn = LocalDateTime.now();
<#list eventFields as field>
        event.${field.propertyName} = ${field.propertyName};
</#list>
        return event;
    }

## ----------  BEGIN Getter 方法  ----------
    /**
     * <p>获取事件ID</p>
     * 
     * @return String 事件ID
     */
    public String getEventId() {
        return eventId;
    }

    /**
     * <p>获取聚合根ID</p>
     * 
     * @return Long 聚合根ID
     */
    public Long getAggregateId() {
        return aggregateId;
    }

    /**
     * <p>获取事件发生时间</p>
     * 
     * @return LocalDateTime 事件发生时间
     */
    public LocalDateTime getOccurredOn() {
        return occurredOn;
    }

<#list eventFields as field>
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
     * <p>转换为字符串</p>
     * 
     * @return String 字符串表示
     */
    @Override
    public String toString() {
        return "${eventName}{" +
                "eventId='" + eventId + '\'' +
                ", aggregateId=" + aggregateId +
                ", occurredOn=" + occurredOn +
<#list eventFields as field>
                ", ${field.propertyName}=" + ${field.propertyName} +
</#list>
                '}';
    }
}
