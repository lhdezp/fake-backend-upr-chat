
from pydantic import BaseModel

from typing import List, Tuple

class LLM(BaseModel):
    name: str
    url: str
    apikey: str

class Source(BaseModel):
    name: str
    urls: List[str]
    domains: List[str]
    collector: str

class CollectionJobs(BaseModel):
    name: str
    sources: List[str]
    date: str

class Chat(BaseModel):
    name:str
    chats: List[List[str]]

class User(BaseModel):
    username: str
    password: str
    chats: List[Chat]