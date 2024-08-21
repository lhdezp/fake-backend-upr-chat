
import os

import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from routers.llm import router as llm_router
from routers.source import router as source_router
from routers.collectionjobs import router as jobs_router
from routers.chat import router as chats_router
from routers.user import router as user_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(llm_router, prefix="/llms")
app.include_router(source_router, prefix="/sources")
app.include_router(jobs_router, prefix="/jobs")
app.include_router(chats_router, prefix="/chats")
app.include_router(user_router, prefix="/user")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  
    uvicorn.run(app, host="0.0.0.0", port=port)
