from pydantic import BaseModel
from typing import Dict, Optional, Tuple


class CreateResponse(BaseModel):
    name: str
    message: str = None
