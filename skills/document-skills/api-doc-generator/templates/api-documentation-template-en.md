# {Product Name} - {Module Name} API Documentation V1.0

## 1. Document Overview

### 1.1 Version History
| Version | Date | Author | Changes | Notes |
| :--- | :--- | :--- | :--- | :--- |
| V1.0.0 | {Date} | - | Initial version | - |

### 1.2 Responsibilities
| Role | Name | Responsibilities |
| :--- | :--- | :--- |
| Product | - | Requirements confirmation, acceptance |
| Frontend | - | API integration, joint debugging |
| Backend | - | API development, documentation maintenance |
| Testing | - | API testing, quality control |

---

## 2. API Interface List

| No. | Interface URL | Method | Description | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `{interface_path}` | `{GET/POST/PUT/DELETE}` | {interface_description} | ✅ Completed / ⏳ In Progress / ❌ Not Started |

---

## 3. Interface Definitions

### 3.1 {Interface Name}

- **Interface URL**: `{Method} {Interface Path}`
- **Description**:
  - This interface corresponds to backend `{Controller Class Name}#{Method Name}`.
  - {Interface functionality description}
  - {Business rules if any}
- **Request**:
  - Method: `{GET/POST/PUT/DELETE}`
  - URL: `{Interface Path}`
  - **Headers**:

    | Parameter Name | Type | Required | Description |
    |:---------------| :--- | :--- |:-----------|
    | `Authorization` | String | Yes | Bearer Token (user authentication credential) |
    | `App-Id` | String | No | Application ID |
    | `App-Channel` | String | No | Application Channel |
    | `App-Version` | String | No | Application Version |
    | `System-Id` | String | No | System ID |
    | `Tenant-Id` | String | Yes | Tenant ID |
  - **Path Parameters**:

    | Parameter Name | Type | Required | Description |
    | :--- | :--- | :--- | :--- |
    | `{parameter_name}` | {type} | {Yes/No} | {parameter_description} |
  - **Query Parameters**:

    | Parameter Name | Type | Required | Description |
    | :--- | :--- | :--- | :--- |
    | `{parameter_name}` | {type} | {Yes/No} | {parameter_description} |
  - **Request Body** (POST/PUT requests only):
    ```json
    {
      "{field_name}": "{field_value}",
      "{field_name}": "{field_value}"
    }
    ```
    - **Request Field Definitions**:

      | Field Name | Type | Required | Description |
      | :--- | :--- | :--- | :--- |
      | `{field_name}` | {type} | {Yes/No} | {field_description} |
- **Response**:
  - **Response Structure**: Follows standard response structure `R<T>`
    ```json
    {
      "code": 200,
      "msg": "success",
      "data": {response_data}
    }
    ```
  - **Response Field Definitions**:

    | Field Name | Type | Description |
    | :--- | :--- | :--- |
    | `{field_name}` | {type} | {field_description} |
  - **Response Example**:
    ```json
    {
      "code": 200,
      "msg": "success",
      "data": {
        "{field_name}": "{field_value}"
      }
    }
    ```
  - **Error Response Example**:
    ```json
    {
      "code": 400,
      "msg": "Parameter error",
      "data": null
    }
    ```

### 3.2 {Interface Name 2}

- **Interface URL**: `{Method} {Interface Path}`
- **Description**:
  - This interface corresponds to backend `{Controller Class Name}#{Method Name}`.
  - {Interface functionality description}
- **Request**:
  - Method: `{GET/POST/PUT/DELETE}`
  - URL: `{Interface Path}`
  - **Query Parameters**:

    | Parameter Name | Type | Required | Description |
    | :--- | :--- | :--- | :--- |
    | `{parameter_name}` | {type} | {Yes/No} | {parameter_description} |
- **Response**:
  - Returns `{Response Type}` object/list.
  - **Response Field Definitions ({Response Type})**:

    | Field Name | Type | Description |
    | :--- | :--- | :--- |
    | `{field_name}` | {type} | {field_description} |
  - **Response Example**:
    ```json
    {
      "code": 200,
      "msg": "success",
      "data": [
        {
          "{field_name}": "{field_value}"
        }
      ]
    }
    ```

---

## 4. Standard Response Structure

### 4.1 Standard Response Format

All interfaces follow a unified response structure:

```typescript
interface ApiResponse<T> {
  code: number;      // 200: Success, >200: Business error
  msg: string;       // Message
  data: T;           // Business data
}
```

### 4.2 Pagination Response Format

Pagination query interfaces return pagination structure:

```typescript
interface PageResponse<T> {
  records: T[];      // Data list
  total: number;     // Total records
  size: number;      // Page size
  current: number;   // Current page
  pages: number;     // Total pages
}
```

### 4.3 Error Code Conventions

| Error Code | Description | Handling Suggestion |
| :--- | :--- | :--- |
| 200 | Success | - |
| 400 | Parameter error | Toast error message |
| 401 | Token expired | Redirect to login page |
| 403 | No permission | Toast "No permission to access" |
| 404 | Resource not found | Toast "Resource not found" |
| 500 | Server error | Toast "Server error, please try again later" |

---

## 5. Request Header Specifications

All interface requests need to automatically inject the following request headers:

| Header | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Authorization` | String | Yes | Bearer Token (user authentication credential) |
| `App-Id` | String | No | Application ID |
| `App-Channel` | String | No | Application Channel |
| `App-Version` | String | No | Application Version |
| `System-Id` | String | No | System ID |
| `Tenant-Id` | String | Yes | Tenant ID |

---

## 6. Important Notes

1. **System Isolation**: All interfaces need to validate `System-Id` to ensure data isolation
2. **Application Isolation**: All interfaces need to validate `App-Id` to ensure application data isolation
3. **Multi-tenant Isolation**: All interfaces need to validate `Tenant-Id` to ensure tenant data isolation
4. **Permission Control**: Interfaces need to validate user permissions to ensure only authorized data operations
5. **Parameter Validation**: All required parameters need to be validated, parameter errors return 400 error code
6. **Exception Handling**: Interface exceptions need to return unified error response format
7. **Data Format**: Time fields uniformly use `yyyy-MM-dd HH:mm:ss` format
8. **Amount Fields**: Amount fields uniformly use `BigDecimal` type, retain 2 decimal places

---

**Document Version**: V1.0.0  
**Created Date**: {Date}  
**Last Updated**: {Date}  
**Maintainer**: {Maintainer}
