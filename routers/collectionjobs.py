import json
import os

from fastapi import APIRouter, status, HTTPException, Body
from typing import Dict

from models.models import CollectionJobs


json_path = 'routers/jsons/collection_jobs.json'
router = APIRouter()

@router.get("/", status_code = status.HTTP_200_OK)
async def get_all_collection_jobs():
    if not os.path.exists(json_path):
        return []
    try :
        with open(json_path, 'r') as f:
            return json.load(f)
    except Exception as e : 
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))

@router.post("/")
async def create_collection_jobs(collection_jobs: CollectionJobs):
    try:
        collection_jobs_list = []
        with open(json_path, 'r') as f:
            collection_jobs_list = json.load(f)
        flag = list(filter(lambda current_collection_jobs: current_collection_jobs["name"] == collection_jobs.name, collection_jobs_list))
        if flag == []:
            collection_jobs_list.append(collection_jobs.dict())
            with open(json_path, 'w') as f:
                json.dump(collection_jobs_list, f)
                return collection_jobs_list
        return HTTPException(status.HTTP_409_CONFLICT, detail= "Already exists")
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))



@router.put("/")
async def update_collection_jobs(collection_jobs: CollectionJobs):
    try:
        collection_jobs_list = []
        with open(json_path, 'r') as f:
            collection_jobs_list = json.load(f)
        flag = False
        def update_element(element: Dict):
            if element["name"] == collection_jobs.name:
                nonlocal flag
                flag = True
                return collection_jobs.dict()
            return element
        collection_jobs_list = list(map(update_element, collection_jobs_list))
        with open(json_path, 'w') as f:
            json.dump(collection_jobs_list, f)
            return collection_jobs_list if flag else HTTPException(status.HTTP_404_NOT_FOUND, detail="Not found")
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))


@router.delete("/")
async def delete_collection_jobs(name: str = Body(..., embed=True)):
    try:
        collection_jobs_list = []
        with open(json_path, 'r') as f:
            collection_jobs_list = json.load(f)
        flag = False
        def validate_element(element: Dict):
            if element["name"] == name:
                nonlocal flag
                flag = True
                return False
            return True
        collection_jobs_list = list(filter(validate_element, collection_jobs_list))
        with open(json_path, 'w') as f:
            json.dump(collection_jobs_list, f)
            return collection_jobs_list if flag else HTTPException(status.HTTP_404_NOT_FOUND, detail="Not found")
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))