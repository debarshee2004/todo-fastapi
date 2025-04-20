from fastapi import FastAPI
from app.database import engine, Base
from api.v1.todos import router as todo_router

app = FastAPI(title="Todo API", description="A simple Todo API using FastAPI and PostgreSQL")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(todo_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}