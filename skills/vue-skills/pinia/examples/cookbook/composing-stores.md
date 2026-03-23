## Instructions

- Use this page as the authoritative reference for **Composing Stores**.
- Follow the official Pinia docs for supported APIs and patterns.
- Keep examples aligned with the section (Introduction / Core Concepts / Cookbook / SSR / API).

## Parameters

- Identify key inputs, configuration options, or function parameters from the official docs.
- Use exact naming and casing from the documentation.
- Document required vs optional parameters.

## Returns

- Describe expected behavior, return values, or output for the documented feature.
- If the page is conceptual, summarize the expected result or effect.

## Common Errors

- Mismatched store IDs or invalid store definitions.
- Using stores before Pinia is installed.
- Accessing stores outside of component context without proper setup.
- Type errors in TypeScript when using stores.
- State mutations outside of actions (in strict mode).

## Best Practices

- Use `defineStore()` for all store definitions.
- Keep state flat and normalized when possible.
- Use getters for computed values derived from state.
- Use actions for async operations and mutations.
- Use TypeScript for type safety.
- Split large stores into smaller, focused stores.

## Scenarios

### Typical usage

- Apply the official steps and validate expected behavior.
- Follow Pinia patterns for store creation and usage.

### Troubleshooting

- Cross-check store setup and Pinia installation.
- Verify store IDs are unique and correctly referenced.
- Check TypeScript types if using TypeScript.

Reference: https://pinia.vuejs.org/cookbook/composing-stores
