from sqlalchemy.orm import Session
from . import models, schemas


def create_task(db: Session, task: schemas.TaskCreate):   # to craeet  a task it takes task from schemas 
    db_task = models.Task(
        title=task.title,
        description=task.description
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_tasks(db: Session):    # to get all tasks 
    return db.query(models.Task).all()


def get_task(db: Session, task_id: int):   # to get the task based on id 
    return db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()


def update_task(db: Session, task_id: int):   # it updates one task in place of other
    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if task:
        task.completed = True
        db.commit()
        db.refresh(task)

    return task


def delete_task(db: Session, task_id: int):    # just deletes the task 
    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if task:
        db.delete(task)  #  it delets from databse
        db.commit()  # it will update the task and it is important step 

    return task