import json
import os

from fastapi import APIRouter, status, HTTPException, Body
from typing import Dict

from models.models import Source


json_path = 'routers/jsons/sources.json'
router = APIRouter()

@router.get("/", status_code = status.HTTP_200_OK)
async def get_all_sources():
    if not os.path.exists(json_path):
        return []
    try :
        with open(json_path, 'r') as f:
            return json.load(f)
    except Exception as e : 
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))

@router.post("/")
async def create_source(source: Source):
    try:
        sources_list = []
        with open(json_path, 'r') as f:
            sources_list = json.load(f)
        flag = list(filter(lambda current_source: current_source["name"] == source.name, sources_list))
        if flag == []:
            sources_list.append(source.dict())
            print("asdasdas")
            with open(json_path, 'w') as f:
                json.dump(sources_list, f)
                return sources_list
        return HTTPException(status.HTTP_409_CONFLICT, detail= "Already exists")
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))



@router.put("/")
async def update_source(source: Source):
    try:
        sources_list = []
        with open(json_path, 'r') as f:
            sources_list = json.load(f)
        flag = False
        def update_element(element: Dict):
            if element["name"] == source.name:
                nonlocal flag
                flag = True
                return source.dict()
            return element
        sources_list = list(map(update_element, sources_list))
        with open(json_path, 'w') as f:
            json.dump(sources_list, f)
            return sources_list if flag else HTTPException(status.HTTP_404_NOT_FOUND, detail="Not found")
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))


@router.delete("/")
async def delete_source(name: str = Body(..., embed=True)):
    try:
        sources_list = []
        with open(json_path, 'r') as f:
            sources_list = json.load(f)
        flag = False
        def validate_element(element: Dict):
            if element["name"] == name:
                nonlocal flag
                flag = True
                return False
            return True
        sources_list = list(filter(validate_element, sources_list))
        with open(json_path, 'w') as f:
            json.dump(sources_list, f)
            return sources_list if flag else HTTPException(status.HTTP_404_NOT_FOUND, detail="Not found")
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))