from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema = {
            "example": {
                "id": 1,
                "item": "Do the dishes"
            }
        }

class Item(BaseModel):
    item: str

    class Config:
        schema = {
            "example": {
                "item": "Read a chapter"
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
