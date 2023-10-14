# Importing all needed files 
from typing import Optional, List
import time 

from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body

import psycopg2
from psycopg2.extras import RealDictCursor

from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

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


# Root Function 
@app.get("/")
async def root():
    return {"Messages Here" : "Hello World!"}

# Get All Posts
@app.get("/posts",  response_model=List[schemas.PostResponse])
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

# Create A New Post
@app.post("/createposts", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
async def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    newpost = models.Post(**post.model_dump())
    db.add(newpost)
    db.commit()
    db.refresh(newpost)
    return newpost

# Get a specific Post
@app.get("/posts/{id}", response_model=schemas.PostResponse)
async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    return post

# Delete a specific post 
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {
            "Actual Return Value": delete_post, 
            "Response:" : Response(status_code=status.HTTP_204_NO_CONTENT)
            }

# Update a post
@app.put("/posts/{id}",  response_model=schemas.PostResponse)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found")
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()