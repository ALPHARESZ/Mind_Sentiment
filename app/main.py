from fastapi import FastAPI

from app.routers.classify_router import router

app = FastAPI(
    title="AI Journaling Service"
)

app.include_router(router)