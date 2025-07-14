from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router

# create tables 
models.Base.metadata.create_all(bind=engine)
app=FastAPI(
    title="KPA from Data API",
    description="Backend assignment for saving and fetching form data",
    version="1.0.0"
)


# including api_routes
app.include_router(router)
