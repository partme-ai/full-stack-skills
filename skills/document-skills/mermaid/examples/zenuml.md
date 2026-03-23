## Instructions

ZenUML provides a simplified way to create sequence diagrams with a more concise syntax than the original Sequence Diagram in Mermaid. A sequence diagram is an interaction diagram that shows how processes operate with one another and in what order.

### Syntax

- Use `zenuml` keyword
- Title: `title Diagram Title` (optional)
- Participants: Defined implicitly by order of appearance, or explicitly with `participant Name`
- Annotators: Use symbols instead of rectangles (e.g., `@Actor`, `@User`, `@Database`)
- Aliases: `participant Alias as "Label"` or `A as Alice`
- Messages:
  - Sync message: `Participant1.method() -> Participant2` or `A.method()` (blocking)
  - Async message: `Participant1.method() => Participant2` or `Alice->Bob: message` (non-blocking)
  - Creation message: `new Participant()` (creates new object)
  - Reply message: `a = A.SyncMessage()`, `return result`, or `@return A->B: result`
- Nesting: Sync and Creation messages are naturally nestable with `{}`
- Comments: `// comment` (Markdown supported)
- Control structures:
  - Loops: `while(condition)`, `for(condition)`, `forEach(condition)`, `loop(condition)`
  - Alt: `if(condition) { } else if(condition) { } else { }`
  - Opt: `opt { }`
  - Parallel: `par { statement1 statement2 }`
  - Try/Catch/Finally: `try { } catch { } finally { }`

Reference: [Mermaid ZenUML Documentation](https://mermaid.js.org/syntax/zenuml.html)

### Example (Basic Sequence)

A simple sequence diagram with implicit participants:

```mermaid
zenuml
    title Demo
    Alice->John: Hello John, how are you?
    John->Alice: Great!
    Alice->John: See you later!
```

### Example (With Participants)

Declare participants explicitly to control their order:

```mermaid
zenuml
    title Declare participant (optional)
    Bob
    Alice
    Alice->Bob: Hi Bob
    Bob->Alice: Hi Alice
```

### Example (With Annotators)

Use annotators to show symbols instead of rectangles:

```mermaid
zenuml
    title Annotators
    @Actor Alice
    @Database Bob
    Alice->Bob: Hi Bob
    Bob->Alice: Hi Alice
```

### Example (With Aliases)

Use aliases for convenient identifiers with descriptive labels:

```mermaid
zenuml
    title Aliases
    A as Alice
    J as John
    A->J: Hello John, how are you?
    J->A: Great!
```

### Example (Sync Message)

Sync (blocking) messages with nesting:

```mermaid
zenuml
    title Sync message
    A.SyncMessage
    A.SyncMessage(with, parameters) {
      B.nestedSyncMessage()
    }
```

### Example (Async Message)

Async (non-blocking) messages:

```mermaid
zenuml
    title Async message
    Alice->Bob: How are you?
```

### Example (Creation Message)

Create new objects using the new keyword:

```mermaid
zenuml
    new A1
    new A2(with, parameters)
```

### Example (Reply Message - Three Ways)

Three ways to express reply messages:

```mermaid
zenuml
    // 1. assign a variable from a sync message.
    a = A.SyncMessage()

    // 1.1. optionally give the variable a type
    SomeType a = A.SyncMessage()

    // 2. use return keyword
    A.SyncMessage() {
    return result
    }

    // 3. use @return or @reply annotator on an async message
    @return
    A->B: result
```

### Example (Reply Message - Complex)

Complex reply message with early return:

```mermaid
zenuml
    title Reply message
    Client->A.method() {
      B.method() {
        if(condition) {
          return x1
          // return early
          @return
          A->Client: x11
        }
      }
      return x2
    }
```

### Example (With Nesting)

Nest sync messages naturally with braces:

```mermaid
zenuml
    A.method() {
      B.nested_sync_method()
      B->C: nested async message
    }
```

### Example (With Comments)

Add comments with Markdown support:

```mermaid
zenuml
    // a comment on a participant will not be rendered
    BookService
    // a comment on a message.
    // **Markdown** is supported.
    BookService.getBook()
```

### Example (With Loops)

Express loops using while, for, forEach, or loop:

```mermaid
zenuml
    Alice->John: Hello John, how are you?
    while(true) {
      John->Alice: Great!
    }
```

### Example (With Alt - Alternative Paths)

Express alternative paths with if/else:

```mermaid
zenuml
    Alice->Bob: Hello Bob, how are you?
    if(is_sick) {
      Bob->Alice: Not so good :(
    } else {
      Bob->Alice: Feeling fresh like a daisy
    }
```

### Example (With Opt - Optional)

Render optional fragments:

```mermaid
zenuml
    Alice->Bob: Hello Bob, how are you?
    Bob->Alice: Not so good :(
    opt {
      Bob->Alice: Thanks for asking
    }
```

### Example (With Parallel)

Show actions happening in parallel:

```mermaid
zenuml
    par {
        Alice->Bob: Hello guys!
        Alice->John: Hello guys!
    }
```

### Example (With Try/Catch/Finally)

Indicate exception handling with try/catch/finally:

```mermaid
zenuml
    try {
      Consumer->API: Book something
      API->BookingService: Start booking process
    } catch {
      API->Consumer: show failure
    } finally {
      API->BookingService: rollback status
    }
```

### Alternative (Standard Sequence Diagram - compatible with all Mermaid versions)

If ZenUML is not supported, use the standard sequence diagram:

```mermaid
sequenceDiagram
    participant U as User
    participant S as System
    participant D as Database

    U->>S: Login Request
    activate S
    S->>D: Query User
    activate D
    D-->>S: User Data
    deactivate D
    S-->>U: Login Success
    deactivate S
```
