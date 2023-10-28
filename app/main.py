# Importing all needed files 
import time 
import psycopg2
from psycopg2.extras import RealDictCursor
from .routers import post, user, auth

# Not needed imports 
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from typing import Optional, List


# Creating an instance of the app 
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Connecting with the database
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user="postgres", password="2918", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Conection successful!")
        break
    except Exception as error:
        print("Connection failed!")
        print("Error : ", error)
        time.sleep(2)

# Include routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# Root Function 
@app.get("/")
async def root():
    return {"Messages Here" : "Hello World!"}