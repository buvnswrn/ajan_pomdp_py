from pydantic import BaseModel
from typing import Dict, Optional, Tuple


class CreateResponse(BaseModel):
    name: str
    id: int = None
    message: str = None


class BooleanResponse(BaseModel):
    success: bool
    message: str = None
