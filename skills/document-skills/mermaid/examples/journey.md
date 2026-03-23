## Instructions

User journey diagrams visualize the experience of a user as they interact with a system or service, showing different stages and touchpoints. User journeys describe at a high level of detail exactly what steps different users take to complete a specific task within a system, application or website. This technique shows the current (as-is) user workflow, and reveals areas of improvement for the to-be workflow.

### Syntax

- Use `journey` keyword
- Title: `title Title Text` (optional)
- Sections: `section Section Name` (groups steps into stages)
- Steps: `Task name: <score>: <comma separated list of actors>`
- Score: Number between 1 and 5 (inclusive) - represents satisfaction level
- Actors: Comma-separated list of actors who perform the step

Reference: [Mermaid User Journey Documentation](https://mermaid.js.org/syntax/userJourney.html)

### Example (Basic User Journey)

A user journey split into sections, with tasks showing scores and actors:

```mermaid
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 5: Me
```

### Example (E-commerce Purchase)

A complete e-commerce purchase journey with multiple sections:

```mermaid
journey
    title Online Shopping Experience
    section Discovery
      Browse products: 4: Customer
      Search for item: 3: Customer
      View product details: 5: Customer
    section Decision
      Compare prices: 4: Customer
      Read reviews: 5: Customer
      Add to cart: 4: Customer
    section Purchase
      Checkout: 3: Customer
      Enter payment info: 2: Customer
      Confirm order: 4: Customer
    section Fulfillment
      Receive confirmation: 5: Customer
      Track shipment: 4: Customer
      Receive product: 5: Customer
```

### Example (Product Onboarding)

A product onboarding journey for new users:

```mermaid
journey
    title New User Onboarding
    section Sign Up
      Visit website: 4: User
      Create account: 3: User
      Verify email: 2: User
    section First Steps
      Complete profile: 3: User
      Take tutorial: 4: User
      Explore features: 5: User
    section Engagement
      Invite friends: 4: User
      Use core feature: 5: User
      Subscribe to plan: 4: User
```

### Example (Customer Support)

A customer support journey showing different touchpoints:

```mermaid
journey
    title Customer Support Experience
    section Issue Discovery
      Encounter problem: 1: Customer
      Search help center: 3: Customer
      Contact support: 2: Customer
    section Resolution
      Explain issue: 3: Customer, Support Agent
      Receive solution: 4: Customer, Support Agent
      Test solution: 4: Customer
    section Follow-up
      Confirm resolution: 5: Customer
      Provide feedback: 4: Customer
```

### Example (App Installation)

A mobile app installation and setup journey:

```mermaid
journey
    title Mobile App Installation
    section Discovery
      See app in store: 4: User
      Read app description: 4: User
      Check reviews: 5: User
    section Installation
      Download app: 4: User
      Install app: 3: User
      Open app: 4: User
    section Setup
      Grant permissions: 2: User
      Create account: 3: User
      Complete setup: 4: User
```

### Example (Simple Journey)

A simple journey without title, showing basic syntax:

```mermaid
journey
    section Morning Routine
      Wake up: 3: Person
      Exercise: 4: Person
      Have breakfast: 5: Person
    section Work
      Commute: 2: Person
      Attend meetings: 3: Person
      Complete tasks: 4: Person
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If user journey diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    Start[Start] --> Browse[Browse Products]
    Browse --> Select[Select Product]
    Select --> Cart[Add to Cart]
    Cart --> Checkout[Checkout]
    Checkout --> Payment[Payment]
    Payment --> Confirm[Order Confirmation]
    Confirm --> End[End]
```
