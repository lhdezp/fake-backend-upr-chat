from fastapi import APIRouter, HTTPException, status, Body

import json
import os

from fastapi import APIRouter, status, HTTPException, Body
from typing import Dict

json_path = 'routers/jsons/chats.json'
router = APIRouter()

@router.get("/{username}")
async def get_chats(username:str):
    if not os.path.exists(json_path):
        return []
    try :
        with open(json_path, 'r') as f:
            chats = json.load(f)
            user_chats = list(filter(lambda x: x["username"] == username, chats))[0]
            return user_chats
    except Exception as e : 
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))

@router.post("/")
async def answer_query(query: str = Body(..., embed=True), username:str = Body(..., embed=True)):
    try:
        chats_list = []
        with open(json_path, 'r') as f:
            chats_list = json.load(f)
        user_chats = list(filter(lambda x: x["username"] == username, chats_list))
        user_chats[0]["chats"].append([query, "Funcionalidad en desarrollo"])
        def update_chats(old_user_chats: Dict):
            nonlocal username
            if username == old_user_chats["username"]:
                nonlocal user_chats
                return user_chats[0]
            return old_user_chats
        chats_list = list(map(update_chats, chats_list))
        with open(json_path, 'w') as f:
            json.dump(chats_list, f)
            print(user_chats[0]["chats"])
            return list(user_chats[0]["chats"])
    except Exception as e :
        print(e)
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))
