from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator


# Database model for tasks
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) # Auto increment ID
    title: str
    description: Optional[str] = None
    completed: bool = False # Default is False

# Input model for creating a new task
class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None

    @field_validator('title')
    def non_empty_title(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty')
        return v


# Input Model for updating task
class TaskUpdate(SQLModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = None
