from fastapi import FastAPI
import photo.photo_rout
import user.router
import user.users_rout
import comment.comment_rout
from database import Model, engine

Model.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.users_rout.router)
app.include_router(user.router.router)
app.include_router(photo.photo_rout.router)
app.include_router(comment.comment_rout.router)
