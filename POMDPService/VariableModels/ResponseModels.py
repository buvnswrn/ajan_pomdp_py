from pydantic import BaseModel
from typing import Dict, Optional, Tuple


class CreateResponse(BaseModel):
    name: str
    id: int = None
    message: str = None


class CreateActionResponse(BaseModel):
    name: str
    attributes: Dict = None
    message: str = None
    id: int = None
    data: str = None


class BooleanResponse(BaseModel):
    success: bool
    message: str = None
