---
name: uniapp-cloud
description: A comprehensive skill for uniCloud cloud development in the uni-app ecosystem. Use this skill when you need uniCloud project setup, cloud database CRUD, cloud functions, storage, or datacom components, following official uniCloud documentation.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Use uniCloud cloud development services
- Work with cloud databases (add, query, update, delete data)
- Create and deploy cloud functions
- Use cloud storage for file uploads and management
- Implement datacom components for data binding
- Integrate backend services with uni-app
- Set up uniCloud project and configuration
- Handle cloud database permissions and security

## How to use this skill

This skill is organized to match the official uniCloud documentation:

1. **Start with setup and project configuration**:
   - `examples/guide/intro.md`
   - `examples/guide/project-setup.md`
   - `examples/guide/cloud-space.md`

2. **Choose the cloud capability**:
   - Database → `examples/database/`
   - Cloud functions → `examples/functions/`
   - Storage → `examples/storage/`
   - Datacom → `examples/datacom/`
   - Security/permission → `examples/security/`

3. **Open the API reference**:
   - `api/cloud-api.md`

**Important Notes**:
- This skill focuses on uniCloud integration and usage, not general backend frameworks
- Each example includes official documentation URL
- Follow official permission and security guidance for production

## Examples and Templates

### Examples

Located in `examples/`:

- **guide/** - Intro, project setup, cloud space creation
- **database/** - CRUD, query, index, permissions
- **functions/** - Function structure, deploy, call
- **storage/** - Upload, download, delete
- **datacom/** - datacom components and binding
- **security/** - permissions and security rules

## Best Practices

1. **Security**: Always set proper database permissions and rules
2. **Performance**: Use indexes for frequently queried fields
3. **Cost**: Optimize cloud function execution time
4. **Error handling**: Implement proper error handling for all cloud operations
5. **Data validation**: Validate data before saving to database

## Resources

- **Official Documentation**: https://doc.dcloud.net.cn/uniCloud/
- **Cloud Database**: https://doc.dcloud.net.cn/uniCloud/database.html
- **Cloud Functions**: https://doc.dcloud.net.cn/uniCloud/cf-functions.html
- **Cloud Storage**: https://doc.dcloud.net.cn/uniCloud/storage.html

## Keywords

unicloud, uniCloud, cloud development, cloud database, cloud functions, cloud storage, datacom, 云开发, 云数据库, 云函数, 云存储
