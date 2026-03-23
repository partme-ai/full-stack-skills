# Test Example Templates

## Basic E2E Test

```javascript
// cypress/e2e/example.cy.js
describe('My First Test', () => {
  it('visits the app', () => {
    cy.visit('/')
    cy.contains('Welcome')
  })
})
```

## Component Test (Vue)

```javascript
// Button.cy.js
import { mount } from 'cypress/vue'
import Button from './Button.vue'

describe('Button Component', () => {
  it('renders', () => {
    mount(Button, {
      props: {
        label: 'Click me'
      }
    })
    cy.get('button').should('contain', 'Click me')
  })
})
```

## Login Test

```javascript
// cypress/e2e/login.cy.js
describe('Login', () => {
  it('can login successfully', () => {
    cy.visit('/login')
    cy.get('[data-cy=email]').type('user@example.com')
    cy.get('[data-cy=password]').type('password123')
    cy.get('[data-cy=submit]').click()
    cy.url().should('include', '/dashboard')
  })
})
```

## Test with API Mocking

```javascript
// cypress/e2e/users.cy.js
describe('Users Page', () => {
  it('displays users', () => {
    cy.intercept('GET', '/api/users', {
      statusCode: 200,
      body: [
        { id: 1, name: 'John' },
        { id: 2, name: 'Jane' }
      ]
    }).as('getUsers')

    cy.visit('/users')
    cy.wait('@getUsers')
    cy.get('[data-cy=user]').should('have.length', 2)
  })
})
```

## Test with Custom Command

```javascript
// cypress/support/commands.js
Cypress.Commands.add('login', (email, password) => {
  cy.visit('/login')
  cy.get('[data-cy=email]').type(email)
  cy.get('[data-cy=password]').type(password)
  cy.get('[data-cy=submit]').click()
})

// Test
describe('Dashboard', () => {
  beforeEach(() => {
    cy.login('user@example.com', 'password123')
  })

  it('displays dashboard', () => {
    cy.get('[data-cy=dashboard]').should('be.visible')
  })
})
```
