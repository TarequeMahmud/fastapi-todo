from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from models import todo as models
from schemas import todo as schemas

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/todos', response_model=list[schemas.TodoOut])
def read_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()
    

@router.post('/todos')
def create_todos(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(task = todo.task)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo



@router.put("/todos/{todo_id}", response_model=schemas.TodoOut)
def update_todo(todo_id:int, todo_data:schemas.TodoUpdate, db:Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.task = todo_data.task
    todo.is_complete = todo_data.is_complete
    db.commit()
    db.refresh(todo)
    return todo



@router.delete('/todos/{todo_id}')
def delete(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}