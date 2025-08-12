from fastapi import FastAPI
from config import Base, engine
from controllers import alimento_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Alimentos",
    description="CRUD de alimentos usando FastAPI con arquitectura limpia",
    version="1.0.0"
)

app.include_router(alimento_controller.router)
