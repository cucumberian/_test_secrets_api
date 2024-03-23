from fastapi import FastAPI
from routes.index_router import index_router

app = FastAPI()
app.include_router(prefix="", router=index_router)
