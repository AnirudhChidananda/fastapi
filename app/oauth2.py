from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.database import get_db
from . import schemas, models
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRES = settings.ACCESS_TOKEN_EXPIRATION


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credential_exception):
    print('token',token)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print('payload',payload)
        id: str = payload.get("user_id")
        print('id',id)


        if not id:
            raise credential_exception
        token_data = schemas.TokenData(id=str(id))

    except JWTError:
        raise credential_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    print('tokenget_current_user',token)
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could nor validate credentials', headers={'WWW-Authenticate':'Bearer'})
    token = verify_access_token(token, credential_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user