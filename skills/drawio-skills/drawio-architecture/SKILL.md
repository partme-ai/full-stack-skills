---
name: drawio-architecture
description: “Creates system architecture, deployment, and component diagrams using Draw.io (diagrams.net). Supports C4 model, UML, AWS/Azure/GCP cloud shapes, swim lanes, and exports to PNG/SVG/PDF. Use when the user needs to design architecture diagrams, visualize system components, or create deployment diagrams for documentation.”
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create system architecture diagrams (microservices, monolith, cloud)
- Design deployment or infrastructure diagrams (AWS, Azure, GCP)
- Build C4 model diagrams (context, container, component, code)
- Generate UML component or package diagrams
- Export diagrams for documentation or design reviews

## How to use this skill

### Workflow

1. **Choose a template** - Start from C4, UML, or cloud provider template in Draw.io
2. **Add shapes** - Use the appropriate shape library (AWS, Azure, GCP, UML, or general)
3. **Define connections** - Use labeled arrows to show data flow and dependencies
4. **Add legend and title** - Include a legend explaining colors/shapes and a diagram title
5. **Export** - Save as `.drawio` for version control; export PNG/SVG/PDF for docs

### Quick-Start Example: C4 Container Diagram (XML)

```xml
<mxGraphModel>
  <root>
    <mxCell id=”0”/>
    <mxCell id=”1” parent=”0”/>
    <!-- Web App container -->
    <mxCell id=”2” value=”Web Application&#xa;[React, TypeScript]” style=”rounded=1;whiteSpace=wrap;fillColor=#438DD5;fontColor=#ffffff;” vertex=”1” parent=”1”>
      <mxGeometry x=”100” y=”100” width=”160” height=”80” as=”geometry”/>
    </mxCell>
    <!-- API container -->
    <mxCell id=”3” value=”API Server&#xa;[Go, Gin]” style=”rounded=1;whiteSpace=wrap;fillColor=#438DD5;fontColor=#ffffff;” vertex=”1” parent=”1”>
      <mxGeometry x=”400” y=”100” width=”160” height=”80” as=”geometry”/>
    </mxCell>
    <!-- Arrow: Web App → API -->
    <mxCell id=”4” value=”REST/JSON” style=”edgeStyle=orthogonalEdgeStyle;” edge=”1” source=”2” target=”3” parent=”1”/>
  </root>
</mxGraphModel>
```

### Collaboration

- **Version control** - Store `.drawio` files in Git alongside source code
- **Confluence** - Use the Draw.io Confluence plugin for inline editing
- **Google Drive** - Open diagrams.net with Google Drive integration

## Best Practices

1. **One diagram, one topic** - Avoid cramming multiple concerns into a single diagram
2. **Consistent styling** - Use the same colors, fonts, and arrow styles across all diagrams
3. **Add a legend** - Explain what colors and shapes represent
4. **Layer complex systems** - Use multiple diagrams at different abstraction levels (C4 levels 1-3)
5. **Note the update date** - Add a “Last updated: YYYY-MM-DD” label for living documents

## Keywords

draw.io, diagrams.net, architecture diagram, C4, deployment diagram, UML, component diagram, 架构图, 部署图, system design, cloud architecture
