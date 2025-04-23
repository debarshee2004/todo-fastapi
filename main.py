from fastapi import FastAPI
from app.database import engine, Base
from api.controller.v1.routes import v1_router as v1_router

app = FastAPI(
    title="Todo API", description="A simple Todo API using FastAPI and PostgreSQL"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(v1_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Todo API",
        "version": {
            "v1": "/api/v1/todos",
            "v2": "/api/v2/todos",
        },
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
