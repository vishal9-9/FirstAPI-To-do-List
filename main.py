from fastapi import FastAPI,HTTPException
from schemas import TodoValid
import models
from models import Todo_table
from database import engine,session

models.Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def index():
    return "index"

@app.post('/todo')
def create(request: TodoValid):
    toadd = Todo_table(task = request.task )
    session.add(toadd)
    session.commit()
    session.close()
    return "added to list"

@app.get('/todo')
def read_all():
    readall = session.query(Todo_table).all()
    return readall

@app.get('/todo/{id}')
def read_id(id: int):
    readid = session.query(Todo_table).get(id)
    if not readid:
        raise HTTPException(status_code = 404, detail = f"{id} do not have any elements") 
    return readid

@app.put('/todo/{id}')
def update(id: int,task: str):
    updateid = session.query(Todo_table).get(id)
    if updateid:
        updateid.task = task
        session.commit()
        session.close()
    raise HTTPException(status_code = 404, detail = f"{id} is not a valid ID")
    return "Updated"

@app.delete('/todo/{id}')
def delete(id: int):
    delete = session.query(Todo_table).get(id)
    session.delete(delete)
    session.commit()
    session.close()
    return "delted"
