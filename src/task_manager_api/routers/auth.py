from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
from task_manager_api.database import get_session
from task_manager_api.model import User
from task_manager_api.auth import hash_password, verify_password, create_access_token
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    """
    Pydantic model for user creation
    """
    username: str
    password: str

class Token(BaseModel):
    """
    Pydantic model for token
    """
    access_token: str 
    token_type: str = "bearer"

@router.post("/register", response_model=Token)
def register(user: UserCreate, session: Session = Depends(get_session)):
    """
    Register a new user
    """
    existing_user = session.exec(select(User).where(User.username == user.username)).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    db_user = User(
        username = user.username,
        hashed_password= hash_password(user.password)
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    access_token  = create_access_token(data={"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    """
    Login a user
    """

    db_user = session.exec(select(User).where(User.username == form_data.username)).first()
    
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": db_user.username})
    return Token(access_token=access_token, token_type="bearer")
