from fastapi import APIRouter
from models import todo as todo_model
from schemas.todo import Todo

router = APIRouter()

@router.get('/todos')
def get_todos():
    return todo_model.todos

@router.post('/todos')
def create_todos(todo:Todo):
    todo_model.todos.append(todo)
    return {"message": "Todo added", "todo":todo}

@router.delete('todos/{todo_id}')
def delete(todo_id:int):
    global todos
    todo_model.todos = [t for t in todo_model.todos if t.id != todo_id]
    return {'message': "todo deleted"}

