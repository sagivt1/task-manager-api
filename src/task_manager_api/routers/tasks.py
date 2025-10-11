from fastapi import APIRouter

# create router for the task endpoint
router = APIRouter()

# memory store for the task (Temporary)
tasks_db = []

@router.get("/")
def get_tasks():
    # Return all the tasks in memory
    return {"tasks": tasks_db}

@router.post('/')
def create_task(task: dict):
    # append the received task to memory
    tasks_db.append(task)
    return {"message": "Task created successfully", "task": task}

@router.delete('/{task_id}')
def delete_task(task_id: int):
    # delete task based on id(index)
    if 0 <= task_id < len(tasks_db):
        deleted_task = tasks_db.pop(task_id)
        return {"message": "Task deleted", "deleted_task": deleted_task}
    return {"Error": "Task not found"}



