
import os

import uvicorn
from fastapi import FastAPI, APIRouter

from routers.llm import router as llm_router
from routers.source import router as source_router
from routers.collectionjobs import router as jobs_router

app = FastAPI()

app.include_router(llm_router, prefix="/llms")
app.include_router(source_router, prefix="/sources")
app.include_router(jobs_router, prefix="/jobs")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  
    uvicorn.run(app, host="0.0.0.0", port=port)
