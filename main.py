from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    task:str

@app.get('/todos')
def get_todos():
    return todos

@app.post('/todos')
def create_todos(todo:Todo):
    todos.append(todo)
    return {"message": "Todo added", "todo":todo}

@app.delete('todos/{todo_id}')
def delete(todo_id:int):
    global todos
    todos = [todo for todo in todos if todo.id !=todo_id]
    return {'message': "todo deleted"}

