from operator import mod
from os import access
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
from .. import database, schemas, models, utils, oauth2


router = APIRouter(tags=["Authentication"])

@router.post('/login', response_model=schemas.Token)
def login(user_credintials: OAuth2PasswordRequestForm = Depends(), db: session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credintials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    if not utils.validate(user_credintials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")

    #create a token 
    access_token = oauth2.create_access_token(data = {"user_id":user.id})
    return {"access_token":access_token, "token_type":"bearer"}   