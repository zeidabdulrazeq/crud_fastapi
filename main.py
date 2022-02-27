from email.mime import base
from os import stat
from typing import Optional
from urllib import response
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange



class Post(BaseModel):
    """ pydantic models to define the schema of the post """
    title: str
    content: str
    rating: Optional[int]


app = FastAPI()


my_posts = [
    {"title": "z",
    "content": "zz",
    "id": 1},
    {"title": "a",
    "content": "aa",
    "id": 1}    
]


def find_post(id):
    """find post id from in memory list of dict"""
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i



@app.get("/posts")
def get_posts():
    """get all posts"""
    return {"data": my_posts} #fast api will serialize the data into json  format



@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post): 
    post_dict = post.dict()
    post_dict['id'] = randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data":my_posts}



@app.get("/posts/{id}")
def get_posts(id: int, response:Response):
    """get specific post"""
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
                            , detail=f"this id {id} is not found")
    return {'data':post}


@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    indx = find_index_post(id)
    if indx == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not a valid post id")
    my_posts.pop(indx)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
