from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class TaskDB(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(255), nullable=False)
    task_description = Column(Text)


Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def get_all_tasks(db: Session):
    return db.query(TaskDB).all()

@app.get("/tasks")
def getalltasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)






def create_task(db: Session, task: dict):
    new_task = TaskDB(task_name=task["task_name"], task_description=task.get("task_description"))
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.post("/tasks/addTasks/")
def addtasks(task: dict, db: Session = Depends(get_db)):
    return create_task(db, task)





def update_task(db: Session, task_id: int, updated_task: dict):
    task = db.query(TaskDB).filter(TaskDB.task_id == task_id).first()
    if task:
        task.task_name = updated_task["task_name"]
        task.task_description = updated_task.get("task_description")
        db.commit()
        db.refresh(task)
    return task

@app.put("/tasks/update/{task_id}")
def updatetask(task_id: int, updated_task: dict, db: Session = Depends(get_db)):
    return update_task(db, task_id, updated_task)





def delete_task(db: Session, task_id: int):
    task = db.query(TaskDB).filter(TaskDB.task_id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task

@app.delete("/tasks/delete/{task_id}")
def deletetask(task_id: int, db: Session = Depends(get_db)):
    return delete_task(db, task_id)