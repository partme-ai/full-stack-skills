# Salt Wireframe | Salt 线框图

**官方文档**: https://plantuml.com/zh/salt

## Instructions

Salt diagrams create wireframe mockups of user interfaces. They are useful for UI/UX design and prototyping.

## Key Concepts

- Use `@startsalt` and `@endsalt` to wrap the diagram
- Use UI elements: buttons, text fields, labels, etc.
- Use layout commands for positioning
- Supports common UI components

## Example: Basic Login Form

```plantuml
@startsalt
{
  Login Form
  [Username:        ]
  [Password:        ]
  [Login] [Cancel]
}
@endsalt
```

## Example: Web Page Layout

```plantuml
@startsalt
{
  {* Header
    [Logo] | "Navigation" | [Search]
  }
  --
  {
    {* Sidebar
      [Menu Item 1]
      [Menu Item 2]
      [Menu Item 3]
    }
    |
    {* Main Content
      "Article Title"
      "Article content goes here..."
      [Read More]
    }
  }
  --
  {* Footer
    "Copyright 2024"
  }
}
@endsalt
```

## Example: Dashboard

```plantuml
@startsalt
{
  {* Dashboard
    [Statistics Card 1] | [Statistics Card 2] | [Statistics Card 3]
    --
    [Chart Area]
    --
    [Recent Activity] | [Notifications]
  }
}
@endsalt
```

## Example: Mobile App Screen

```plantuml
@startsalt
{
  {* Mobile App
    [Back] | "Screen Title" | [Menu]
    --
    [Content Area]
    "Main content here..."
    --
    [Button 1] [Button 2]
  }
}
@endsalt
```

## Key Points

- Use `@startsalt` and `@endsalt` for wireframe diagrams
- Use `{*` for sections and `}` for closing
- Use `|` for horizontal layout, `--` for vertical layout
- Use `[` and `]` for buttons and input fields
- Salt diagrams are ideal for UI mockups and prototyping
