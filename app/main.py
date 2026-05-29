from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.classify_router import (
    router as classify_router
)

from app.routers.burnout_router import (
    router as burnout_router
)

load_dotenv()

app = FastAPI(
    title="Mind Sentiment AI Service"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(classify_router)
app.include_router(burnout_router)

@app.get("/")
async def root():
    return {
        "message": "AI Service Running"
    }