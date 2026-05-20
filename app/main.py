from fastapi import FastAPI
from .database import engine
from . import models
from .routes import router
from fastapi.middleware.cors import CORSMiddleware
from app import models

models.Base.metadata.create_all(bind=engine)  # this is main thing it creates the engine based on the metadata 

app = FastAPI(
    title="Todo CRUD API"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Todo API Running"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)