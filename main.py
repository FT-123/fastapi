from fastapi import FastAPI
import Photo.Photorout
import User.router
import User.Usersrout
import Comment.Commentrout
from database import Model, engine


Model.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(User.Usersrout.router)
app.include_router(User.router.router)
app.include_router(Photo.Photorout.router)
app.include_router(Comment.Commentrout.router)




