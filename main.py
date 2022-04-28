from fastapi import Depends, FastAPI
import auth.router
from database import Model, engine
from routers import Usersrout
import uvicorn



Model.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(Usersrout.router)
app.include_router(auth.router.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)

