## Instructions

Timeline diagrams display events in chronological order, showing the sequence of events over time. A timeline is a type of diagram used to illustrate a chronology of events, dates, or periods of time. It is usually presented graphically to indicate the passing of time, and it is usually organized chronologically. A basic timeline presents a list of events in chronological order, usually using dates as markers.

**Note**: This is an experimental diagram type. The syntax and properties can change in future releases. The syntax is stable except for the icon integration which is the experimental part.

### Syntax

- Use `timeline` keyword
- Title: `title Timeline Title` (optional)
- Time period: `{time period} : {event}` or `{time period} : {event} : {event}` (multiple events per period)
- Sections: `section Section Name` (groups time periods in sections/ages)
- Text wrapping: Use `<br>` to force line breaks
- Multiple events per period: Can be on same line with `:` separator or on separate lines
- Configuration: `disableMulticolor` to disable multi-color scheme
- Theme variables: `cScale0` to `cScale11` for background colors, `cScaleLabel0` to `cScaleLabel11` for foreground colors

Reference: [Mermaid Timeline Diagram Documentation](https://mermaid.js.org/syntax/timeline.html)

### Example (Basic Timeline)

A simple timeline with title and multiple events per period:

```mermaid
timeline
    title History of Social Media Platform
    2002 : LinkedIn
    2004 : Facebook : Google
    2005 : YouTube
    2006 : Twitter
```

### Example (With Sections)

Group time periods in sections/ages:

```mermaid
timeline
    title Timeline of Industrial Revolution
    section 17th-20th century
        Industry 1.0 : Machinery, Water power, Steam <br>power
        Industry 2.0 : Electricity, Internal combustion engine, Mass production
        Industry 3.0 : Electronics, Computers, Automation
    section 21st century
        Industry 4.0 : Internet, Robotics, Internet of Things
        Industry 5.0 : Artificial intelligence, Big data, 3D printing
```

### Example (With Text Wrapping)

Use `<br>` to force line breaks in long text:

```mermaid
timeline
    title England's History Timeline
    section Stone Age
      7600 BC : Britain's oldest known house was built in Orkney, Scotland
      6000 BC : Sea levels rise and Britain becomes an island.<br> The people who live here are hunter-gatherers.
    section Bronze Age
      2300 BC : People arrive from Europe and settle in Britain. <br>They bring farming and metalworking.
                : New styles of pottery and ways of burying the dead appear.
      2200 BC : The last major building works are completed at Stonehenge.<br> People now bury their dead in stone circles.
                : The first metal objects are made in Britain.Some other nice things happen. it is a good time to be alive.
```

### Example (With Section Title Wrapping)

Use `<br>` in section titles and events:

```mermaid
timeline
    title MermaidChart 2023 Timeline
    section 2023 Q1 <br> Release Personal Tier
      Bullet 1 : sub-point 1a : sub-point 1b
           : sub-point 1c
      Bullet 2 : sub-point 2a : sub-point 2b
    section 2023 Q2 <br> Release XYZ Tier
      Bullet 3 : sub-point <br> 3a : sub-point 3b
           : sub-point 3c
      Bullet 4 : sub-point 4a : sub-point 4b
```

### Example (With Configuration - Disable MultiColor)

Disable multi-color scheme using configuration:

```mermaid
---
config:
  logLevel: 'debug'
  theme: 'base'
  timeline:
    disableMulticolor: true
---
timeline
    title History of Social Media Platform
    2002 : LinkedIn
    2004 : Facebook : Google
    2005 : YouTube
    2006 : Twitter
```

### Example (With Theme Variables)

Customize color scheme using theme variables:

```mermaid
---
config:
  logLevel: 'debug'
  theme: 'default'
  themeVariables:
    cScale0: '#ff0000'
    cScaleLabel0: '#ffffff'
    cScale1: '#00ff00'
    cScale2: '#0000ff'
    cScaleLabel2: '#ffffff'
---
timeline
    title History of Social Media Platform
    2002 : LinkedIn
    2004 : Facebook : Google
    2005 : YouTube
    2006 : Twitter
    2007 : Tumblr
    2008 : Instagram
    2010 : Pinterest
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If timeline diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart LR
    Start[2024 Q1<br>Project Kickoff] --> Phase1[2024 Q2<br>Development Phase 1]
    Phase1 --> Phase2[2024 Q3<br>Development Phase 2]
    Phase2 --> Launch[2024 Q4<br>Production Launch]
```
