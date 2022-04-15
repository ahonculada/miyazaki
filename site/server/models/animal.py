from typing import Optional
from pydantic import BaseModel, Field

class AnimalSchema(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    ascii: str = Field(...)
    artist: str = Field(...)
    
    class Config:
        schema_extra = {
            "example" : {
                "id": 123,
                "name": "fish",
                "ascii": "<><",
                "artist": "vangogh",
            }
        }
class updateAnimalModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    ascii: Optional[str]
    artist: Optional[str]

    class Config:
        schema_extra = {
            "example" : {
                "id": 1234,
                "name": "fish",
                "ascii": "<><",
                "artist": "bach",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}