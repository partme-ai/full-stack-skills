## Instructions

Packet diagrams are visual representations used to illustrate the structure and contents of a network packet. Network packets are the fundamental units of data transferred over a network. This diagram type is particularly useful for developers, network engineers, educators, and students who require a clear and concise way to represent the structure of network packets.

### Syntax

- Use `packet` keyword (requires Mermaid v11.0.0+)
- Title: `title "Packet Title"` or `--- title: "Packet Title" ---` (optional)
- Fields:
  - `start-end: "Field Description"` - Multi-bit blocks (e.g., `0-15: "Field Name"`)
  - `start: "Field Description"` - Single-bit block (e.g., `0: "Flag"`)
- Bit Syntax (v11.7.0+): Use `+<count>` to set the number of bits, which starts from the end of the previous field automatically
  - `+1: "Block name"` - Single-bit block
  - `+8: "Block name"` - 8-bit block
  - You can mix and match: `9-15: "Manually set start and end"`
- Ranges: Each line after the title represents a different field in the packet. The range (e.g., `0-15`) indicates the bit positions in the packet.
- Field Description: A brief description of what the field represents, enclosed in quotes.

Reference: [Mermaid Packet Diagram Documentation](https://mermaid.js.org/syntax/packet.html)

### Example (TCP Packet with Configuration)

A complete TCP packet example using configuration block and traditional bit range syntax:

```mermaid
---
title: "TCP Packet"
---
packet
0-15: "Source Port"
16-31: "Destination Port"
32-63: "Sequence Number"
64-95: "Acknowledgment Number"
96-99: "Data Offset"
100-105: "Reserved"
106: "URG"
107: "ACK"
108: "PSH"
109: "RST"
110: "SYN"
111: "FIN"
112-127: "Window"
128-143: "Checksum"
144-159: "Urgent Pointer"
160-191: "(Options and Padding)"
192-255: "Data (variable length)"
```

### Example (UDP Packet with Bit Count Syntax)

A UDP packet example using bit count syntax (v11.7.0+):

```mermaid
packet
title UDP Packet
+16: "Source Port"
+16: "Destination Port"
32-47: "Length"
48-63: "Checksum"
64-95: "Data (variable length)"
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If packet diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    subgraph Packet["Packet Structure"]
        Field1["0-47: Destination MAC"]
        Field2["48-95: Source MAC"]
        Field3["96-111: Type/Length"]
        Field4["112-: Payload"]
    end
```
