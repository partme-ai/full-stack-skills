## Instructions

Architecture diagrams are used to show the relationship between services and resources commonly found within the Cloud or CI/CD deployments. In an architecture diagram, services (nodes) are connected by edges. Related services can be placed within groups to better illustrate how they are organized.

**⚠️ Important Compatibility Note**: `architecture-beta` requires Mermaid v11.1.0 or higher. If your rendering environment doesn't support this diagram type (you'll see "No diagram type detected" error), please use the **Flowchart alternatives** provided below each example, which are compatible with all Mermaid versions.

### Syntax

- Use `architecture-beta` keyword (requires Mermaid v11.1.0+)
- **If your environment doesn't support `architecture-beta`**: Each example below includes a flowchart alternative that works with all Mermaid versions
- Building blocks: `groups`, `services`, `edges`, and `junctions`
- Icons: Declared by surrounding the icon name with `()`
- Labels: Declared by surrounding the text with `[]`
- Groups: `group {group id}({icon name})[{title}] (in {parent id})?`
- Services: `service {service id}({icon name})[{title}] (in {parent id})?`
- Edges: `{serviceId}{{group}}?:{T|B|L|R} -- {T|B|L|R}:{serviceId}{{group}}?` (use `--` not `-->`)
- Junctions: `junction {junction id} (in {parent id})?`
- Default icons: `cloud`, `database`, `disk`, `internet`, `server`
- Custom icons: Can use 200,000+ icons from iconify.design by registering an icon pack

Reference: [Mermaid Architecture Diagram Documentation](https://mermaid.ai/open-source/syntax/architecture.html)

### Example (Basic Architecture)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    group api(cloud)[API]
    service db(database)[Database] in api
    service disk1(disk)[Storage] in api
    service disk2(disk)[Storage] in api
    service server(server)[Server] in api
    db:L -- R:server
    disk1:T -- B:server
    disk2:T -- B:db
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    subgraph API["API"]
        DB[(Database)]
        Disk1[(Storage)]
        Disk2[(Storage)]
        Server[Server]
    end
    DB --> Server
    Disk1 --> Server
    Disk2 --> DB
```

### Example (With Edges and Directions)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    service db(database)[Database]
    service server(server)[Server]
    service gateway(internet)[Gateway]

    db:L -- R:server
    server:T -- B:gateway
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart LR
    DB[(Database)]
    Server[Server]
    Gateway[Gateway]

    DB --> Server
    Server --> Gateway
```

### Example (With Arrows)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    service subnet(server)[Subnet]
    service gateway(internet)[Gateway]

    subnet:R --> L:gateway
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart LR
    Subnet[Subnet]
    Gateway[Gateway]

    Subnet --> Gateway
```

### Example (Groups and Nested Services)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    group frontend(cloud)[Frontend]
    group backend(cloud)[Backend]

    service web(server)[Web Server] in frontend
    service api(server)[API Server] in backend
    service db(database)[Database] in backend

    web:L -- R:api
    api:L -- R:db
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    subgraph Frontend["Frontend"]
        Web[Web Server]
    end
    subgraph Backend["Backend"]
        API[API Server]
        DB[(Database)]
    end
    Web --> API
    API --> DB
```

### Example (With Junctions)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    service left_disk(disk)[Disk]
    service top_disk(disk)[Disk]
    service bottom_disk(disk)[Disk]
    service top_gateway(internet)[Gateway]
    service bottom_gateway(internet)[Gateway]
    junction junctionCenter
    junction junctionRight

    left_disk:R -- L:junctionCenter
    top_disk:B -- T:junctionCenter
    bottom_disk:T -- B:junctionCenter
    junctionCenter:R -- L:junctionRight
    top_gateway:B -- T:junctionRight
    bottom_gateway:T -- B:junctionRight
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    LeftDisk[(Disk)]
    TopDisk[(Disk)]
    BottomDisk[(Disk)]
    TopGateway[Gateway]
    BottomGateway[Gateway]

    LeftDisk --> TopDisk
    LeftDisk --> BottomDisk
    TopDisk --> TopGateway
    BottomDisk --> BottomGateway
```

### Example (Edge from Group to Group)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    group groupOne(cloud)[Group One]
    group groupTwo(cloud)[Group Two]

    service server[Server] in groupOne
    service subnet[Subnet] in groupTwo

    server{group}:B --> T:subnet{group}
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    subgraph GroupOne["Group One"]
        Server[Server]
    end
    subgraph GroupTwo["Group Two"]
        Subnet[Subnet]
    end
    Server --> Subnet
```

### Example (Complex Cloud Architecture)

**Note**: Requires Mermaid v11.1.0+. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    group public(cloud)[Public Cloud]
    group private(cloud)[Private Cloud]

    service gateway(internet)[Internet Gateway] in public
    service loadbalancer(server)[Load Balancer] in public
    service app1(server)[App Server 1] in private
    service app2(server)[App Server 2] in private
    service db(database)[Database] in private
    service storage(disk)[Storage] in private

    gateway:L -- R:loadbalancer
    loadbalancer:B -- T:app1
    loadbalancer:B -- T:app2
    app1:L -- R:db
    app2:L -- R:db
    db:B -- T:storage
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    subgraph Public["Public Cloud"]
        Gateway[Internet Gateway]
        LB[Load Balancer]
    end
    subgraph Private["Private Cloud"]
        App1[App Server 1]
        App2[App Server 2]
        DB[(Database)]
        Storage[(Storage)]
    end

    Gateway --> LB
    LB --> App1
    LB --> App2
    App1 --> DB
    App2 --> DB
    DB --> Storage
```

### Example (With Custom Icons)

**Note**: Requires Mermaid v11.1.0+ and icon pack registration. If not supported, use the flowchart alternative below.

```mermaid
architecture-beta
    group api(logos:aws-lambda)[API]
    service db(logos:aws-aurora)[Database] in api
    service disk1(logos:aws-glacier)[Storage] in api
    service disk2(logos:aws-s3)[Storage] in api
    service server(logos:aws-ec2)[Server] in api
    db:L -- R:server
    disk1:T -- B:server
    disk2:T -- B:db
```

**Flowchart Alternative (Compatible with all versions):**

```mermaid
flowchart TD
    subgraph API["API"]
        DB[(Database)]
        Disk1[(Storage)]
        Disk2[(Storage)]
        Server[Server]
    end
    DB --> Server
    Disk1 --> Server
    Disk2 --> DB
```
