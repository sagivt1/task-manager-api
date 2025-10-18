from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from task_manager_api.model import Task, TaskCreate, TaskUpdate
from task_manager_api.database  import get_session

# create router for the task endpoint
router = APIRouter()

@router.get("/", response_model=list[Task])
def get_tasks(session: Session = Depends(get_session)):
    """
    Retrieve all tasks from the database.
    """
    task = session.exec(select(Task)).all()
    return task
    

@router.post('/', response_model=Task)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    """
    Create a new task.
    """
    db_task = Task(title=task.title, description=task.description)
    session.add(db_task)
    session.commit()
    session.refresh(db_task) # to get auto-generated ID
    return db_task

@router.patch('/{task_id}', response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate, session: Session = Depends(get_session)):
    """
    Update a task. Only provided fields will be updated.
    """
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task no found")
    # update only the field that provided
    task_data = task_update.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(db_task, key, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.delete('/{task_id}', status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    """
    Delete a task by ID.
    """
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task no found")

    session.delete(db_task)
    session.commit()
