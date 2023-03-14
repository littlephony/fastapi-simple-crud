from pydantic import BaseModel
from fastapi import Form
from typing import Optional

class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)

    class Config:
        schema = {
            "example": {
                "id": 1,
                "item": "example schema"
            }
        }

class Item(BaseModel):
    item: str

    class Config:
        schema = {
            "example": {
                "item": "example schema"
            }
        }

class Items(BaseModel):
    todos: list[Item]

    class Config:
        schema = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1"
                    },
                    {
                        "item": "Example schema 2"
                    }
                ]
            }
        }
