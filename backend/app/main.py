from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Linux Digital Twin API",
    description="Affichage Digital phase 1 de developpement",
    version="0.1.0"
)

app.include_router(router, prefix="/api")

@app.get('/')
async def root():
    return{
        "Message" : "Linux Digital",
        "docs/Swagger" : "http://localhost:8000/docs",
    }