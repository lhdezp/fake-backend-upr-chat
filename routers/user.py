
from fastapi import APIRouter, HTTPException, Body, status

router = APIRouter()


@router.post('/')
async def autenticate(username: str = Body(..., embed=True), password: str = Body(..., embed=True)):
    flag = False
    if username == "adminuser" and password == "adminpass":
        flag = True
    if username == "basicuser" and password == "basicpass":
        flag = True
    if not flag:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return "Successfully authenticated"