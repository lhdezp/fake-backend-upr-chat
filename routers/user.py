
from fastapi import APIRouter, HTTPException, Body

router = APIRouter()

@router.post('/')
async def autenticate(username:str = Body(..., embed=True), password:str = Body(..., embed=True)):
    try :
        flag = False
        print("asdasdad")
        if username == "adminuser" and password == "adminpass":
            flag = True
        if username == "basicuser" and password == "basicpass":
            flag = True
        if not flag:
            raise HTTPException(401, "Authentication wrong")
        return "Successfully authenticated"
    except Exception as e:
        print(e)
        return HTTPException(500, detail = str(e))
