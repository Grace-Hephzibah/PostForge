from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])

# Login 
@router.post("/login")
async def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    # Invalid Email ID
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = "Invalid Credentials")

    # Invalid Password
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = "Invalid Credentials")

    # create access token
    payload = {
        "user_id" : user.id
    }
    access_token = oauth2.create_access_token(data = payload)
    
    # return token
    return_token = {
            "access_token" : access_token, 
            "token_type" : "bearer"
            }
    return return_token