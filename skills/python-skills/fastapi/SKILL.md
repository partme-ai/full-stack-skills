---
name: fastapi
description: "Provides comprehensive guidance for FastAPI framework including routing, request validation, dependency injection, async operations, OpenAPI documentation, and database integration. Use when the user asks about FastAPI, needs to create REST APIs, or build high-performance Python web services."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build REST or async APIs with FastAPI and Pydantic models
- Implement dependency injection, authentication, or middleware
- Configure routing, OpenAPI documentation, and deployment
- Integrate with databases using async patterns

## How to use this skill

### Workflow

1. **Create app** — instantiate `FastAPI()` and define route handlers
2. **Define models** — use Pydantic for request/response validation
3. **Add dependencies** — implement DI for auth, DB sessions, etc.
4. **Test and deploy** — run with uvicorn, verify via `/docs`

### Quick Start Example

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="My API", version="1.0.0")

# Request/Response models
class ItemCreate(BaseModel):
    name: str
    price: float
    description: str | None = None

class ItemResponse(ItemCreate):
    id: int
    created_at: datetime

# Dependency example
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route handlers
@app.post("/items/", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate, db=Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    return db_item

@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db=Depends(get_db)):
    item = db.query(Item).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

```bash
# Run the server
uvicorn main:app --reload

# Interactive docs available at http://localhost:8000/docs
```

### Authentication Example

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
async def read_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user
```

## Best Practices

- Define explicit request and response schemas with Pydantic; use consistent status codes
- Use async functions and database connection pools for high concurrency
- Configure CORS middleware and security headers for production
- Leverage automatic OpenAPI docs (`/docs`, `/redoc`) for API exploration
- Use `BackgroundTasks` for non-blocking operations like email sending

## Reference

- Official documentation: https://fastapi.tiangolo.com/

## Keywords

fastapi, async API, Pydantic, OpenAPI, dependency injection, Python web, REST API, uvicorn
