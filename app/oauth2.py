from datetime import datetime, timedelta
from jose import JWTError, jwt

# SECRET_KEY
SECRET_KEY = "kajdlskdlfjijk4en3i4029283rosjdkfxmcowie29734lkasndmfn234"

# Algorithm
ALGORITHM = "HS256"

# Expiration Time
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
