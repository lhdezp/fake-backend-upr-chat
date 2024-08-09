import json
import os

from fastapi import APIRouter, status, HTTPException, Body
from typing import Dict

from models.models import LLM


json_path = 'routers/jsons/llms.json'
router = APIRouter()

@router.get("/", status_code = status.HTTP_200_OK)
async def get_all_llms():
    if not os.path.exists(json_path):
        return []
    try :
        with open(json_path, 'r') as f:
            return json.load(f)
    except Exception as e : 
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))


@router.post("/")
async def create_llm(llm: LLM):
    try:
        llms_list = []
        with open(json_path, 'r') as f:
            llms_list = json.load(f)
        flag = list(filter(lambda current_llm: current_llm["name"] == llm.name, llms_list))
        if flag == []:
            llms_list.append(llm.dict())
            with open(json_path, 'w') as f:
                json.dump(llms_list, f)
                return llms_list
        return HTTPException(status.HTTP_409_CONFLICT, detail= "Already exists")
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))



@router.put("/")
async def update_llm(llm: LLM):
    try:
        llms_list = []
        with open(json_path, 'r') as f:
            llms_list = json.load(f)
        flag = False
        def update_element(element: Dict):
            if element["name"] == llm.name:
                nonlocal flag
                flag = True
                return llm.dict()
            return element
        llms_list = list(map(update_element, llms_list))
        with open(json_path, 'w') as f:
            json.dump(llms_list, f)
            return llms_list if flag else HTTPException(status.HTTP_404_NOT_FOUND, detail="Not found")
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))


@router.delete("/")
async def delete_llm(name: str = Body(..., embed=True)):
    try:
        llms_list = []
        with open(json_path, 'r') as f:
            llms_list = json.load(f)
        flag = False
        def validate_element(element: Dict):
            if element["name"] == name:
                nonlocal flag
                flag = True
                return False
            return True
        llms_list = list(filter(validate_element, llms_list))
        with open(json_path, 'w') as f:
            json.dump(llms_list, f)
            return llms_list if flag else HTTPException(status.HTTP_404_NOT_FOUND, detail="Not found")
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))