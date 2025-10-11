from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class Task(BaseModel):
    id: int = None
    title: str
    description: str

# create router for the task endpoint
router = APIRouter()

# memory store for the task (Temporary)
tasks_db = []
# Auto increment ID
current_id = 0

@router.get("/")
def get_tasks():
    # Return all the tasks in memory
    return {"tasks": tasks_db}

@router.post('/')
def create_task(task: Task):
    """
    Accepts a task object via pydantic.
    Assign a unique ID and store in memory.
    """
    global current_id
    current_id += 1
    task.id = current_id
    tasks_db.append(task.model_dump())
    return {"message": "Task created successfully", "task": task}

@router.delete('/{task_id}')
def delete_task(task_id: int):
    """
    Delete task based on ID.
    IF not found raise 404 not found.
    """
    for idx, task in enumerate(tasks_db):
        if task["id"] == task_id:
            deleted_task = tasks_db.pop(task_id)
            return {"message": "Task deleted", "deleted_task": deleted_task}
    raise HTTPException(status_code=404, detail="Task not found") 



