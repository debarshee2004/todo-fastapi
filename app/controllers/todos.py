from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.todos import Todo
from app.schemas.todos import TodoCreate, TodoUpdate, TodoResponse
from app.database import get_db
from typing import List

def create_todo(todo: TodoCreate, db: Session = Depends(get_db)) -> TodoResponse:
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db: Session = Depends(get_db)) -> List[TodoResponse]:
    return db.query(Todo).all()

def get_todo(todo_id: int, db: Session = Depends(get_db)) -> TodoResponse:
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)) -> TodoResponse:
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> dict:
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}