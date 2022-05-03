from pydantic import BaseModel

class TodoValid(BaseModel):
    task: str