from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal
from . import schemas, crud

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# frontend lo user data pampinchinappudu , or request appudu adhi router ki vachi adhi method ni call chesidhi andhukani routers vadamu

@router.post("/tasks", response_model=schemas.TaskResponse)  
def create_new_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    return crud.create_task(db, task)


@router.get("/tasks")
def get_all_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@router.get("/tasks/{task_id}")
def get_single_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = crud.get_task(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task
 # task id base meedha chesamu

@router.put("/tasks/{task_id}")
def complete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = crud.update_task(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.delete("/tasks/{task_id}")
def remove_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = crud.delete_task(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully"}