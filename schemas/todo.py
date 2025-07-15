from pydantic import BaseModel


class TodoBase(BaseModel):
    task:str
    is_complete: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoOut(TodoBase):
    id:int
    class Config:
        orm_mode = True