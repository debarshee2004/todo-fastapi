from fastapi import APIRouter, Depends
from typing import List
from app.schemas.todos import TodoCreate, TodoUpdate, TodoResponse
from app.controllers.todos import create_todo, get_todos, get_todo, update_todo, delete_todo
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/v1/todos", tags=["api-v1-todos"])

@router.post("/", response_model=TodoResponse)
async def create_todo_route(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(todo, db)

@router.get("/", response_model=List[TodoResponse])
async def get_todos_route(db: Session = Depends(get_db)):
    return get_todos(db)

@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo_route(todo_id: int, db: Session = Depends(get_db)):
    return get_todo(todo_id, db)

@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo_route(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    return update_todo(todo_id, todo, db)

@router.delete("/{todo_id}")
async def delete_todo_route(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo(todo_id, db)