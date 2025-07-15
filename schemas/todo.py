from pydantic import BaseModel


class TodoBase(BaseModel):
    task:str

class TodoCreate(TodoBase):
    pass

class TodoOut(TodoBase):
    id:int
    class Config:
        orm_mode = True