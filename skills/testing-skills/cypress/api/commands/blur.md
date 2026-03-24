## Instructions

- Use this page as the authoritative reference for **Blur**.
- Follow the official Cypress docs for supported APIs and patterns.
- Keep examples aligned with the section (App / API).

## Parameters

- Identify key inputs, configuration options, or function parameters from the official docs.
- Use exact naming and casing from the documentation.
- Document required vs optional parameters.

## Returns

- Describe expected behavior, return values, or output for the documented feature.
- If the page is conceptual, summarize the expected result or effect.

## Common Errors

- Element not found or not visible errors.
- Timeout errors when waiting for elements or network requests.
- Incorrect selector usage or stale element references.
- Async/await issues in Cypress commands.
- Configuration errors in cypress.config.js.

## Best Practices

- Use data-cy attributes for stable selectors.
- Avoid hard-coded waits, use Cypress's built-in retry-ability.
- Keep tests isolated and independent.
- Use custom commands for reusable test logic.
- Follow Cypress's best practices for assertions and commands.

## Scenarios

### Typical usage

- Apply the official steps and validate expected behavior.
- Follow Cypress patterns for test creation and execution.

### Troubleshooting

- Cross-check selector strategies and element visibility.
- Verify network requests and responses if testing API calls.
- Check Cypress configuration and environment setup.

Reference: https://docs.cypress.io/api/commands/blur
