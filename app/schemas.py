"""Schema definitions for the API."""
from pydantic import BaseModel
from typing import List


class Input(BaseModel):
    """Base schema for user input."""
    input: str

class Output(Input):
    output: List[dict]