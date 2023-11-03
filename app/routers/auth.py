from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])

# Login 
@router.post("/login", response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), 
                db: Session = Depends(database.get_db)):
    
    # user_credentials = { "username": 
    #                      "password" :   }

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    # Invalid Email ID
    if not user:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                            detail = "Invalid Credentials")

    # Invalid Password
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                            detail = "Invalid Credentials")

    # Create access token
    payload = {
        "user_id" : user.id
    }
    access_token = oauth2.create_access_token(data = payload)
    
    # Return token
    return_token = {
            "access_token" : access_token, 
            "token_type" : "Bearer"
            }
    return return_token
