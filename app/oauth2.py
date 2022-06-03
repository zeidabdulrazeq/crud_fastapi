from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings
oath2_scheme = OAuth2PasswordBearer(tokenUrl='login')

#secret key

#algorithm to use 

#experiration time of the token

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_min

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id:str = payload.get("user_id")

        if not id:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError as e:
        raise credentials_exception        
    return token_data        


def get_current_user(token: str = Depends(oath2_scheme), 
                     db: Session = Depends(database.get_db)):
    credintial_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                        detail="could not validate credintials", 
                                        headers={"WWW:Authenticate":"Bearer"}
                                        )
    token =  verify_access_token(token, credintial_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()                         
    return user

