from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users", 
    tags = ['Users']
)

# Create User
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
async def create_posts(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash of the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    newuser = models.User(**user.model_dump())
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser

# Retreive User 
@router.get("/{id}", response_model=schemas.UserResponse)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"User with id: {id} does not exist")

    return user
