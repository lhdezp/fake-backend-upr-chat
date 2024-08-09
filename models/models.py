
from pydantic import BaseModel

from typing import List

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

