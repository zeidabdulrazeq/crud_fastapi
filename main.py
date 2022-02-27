from email.mime import base
from os import stat
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

#pydantic models to define the schema to insure validity
class Post(BaseModel):
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
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post    
#path operation in this case it's the root path ... decorator @ with get method 
#doesnt need to be async


#order of functions matters when its the same path first will be executed and ended
@app.get("/posts")
def get_posts():
    return {"data": my_posts} #fast api will serialize the data into json  format


@app.post("/posts", status_code=status.HTTP_201_CREATED) #change from default 200 
def create_post(post: Post): #post is a dytantic model
    print()
    post_dict = post.dict()
    post_dict['id'] = randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data":my_posts}



#get a specific post
#path parameter are always returned as a string unless u spec type
@app.get("/posts/{id}")
def get_posts(id: int, response:Response):

    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
                            , detail=f"this id {id} is not found")
    return {'data':post}


@app.delete('/posts/{id}')