from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from task_manager_api.model import Task, TaskCreate, TaskUpdate
from task_manager_api.database  import get_session

# create router for the task endpoint
router = APIRouter()

@router.get("/", response_model=list[Task])
def get_tasks(
    completed: bool | None = Query(default=None, description="filter tasks by completion status"),
    limit: int | None = Query(default=10, ge=1, le=100, description="limit the number of tasks returned"),
    offset: int | None = Query(default=0, ge=0, description="offset for pagination"),
    search: str | None = Query(None, description="search tasks by title or description"),
    session: Session = Depends(get_session),
):
    """
    Retrieve tasks with pagination, filtering, and searching.  
    """
    query = select(Task)
    # filter by completed status
    if completed is not None:
        query = query.where(Task.completed == completed)

    # search by title or description if provided 
    if search:
        search_term = f"%{search}%"
        query = query.where(
            (Task.title.like(search_term)) | (Task.description.like(search_term))
        )

    # Apply pagination
    query = query.offset(offset).limit(limit)

    tasks = session.exec(query).all()
    return tasks
    
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