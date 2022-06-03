from fastapi import FastAPI
from .database import engine, SessionLocal, get_db
from . import models
from .routers import post, user, auth, vote
from.config import settings
from fastapi.middleware.cors import CORSMiddleware

#using sql alchemy to create the db tables when starting
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
