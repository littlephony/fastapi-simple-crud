from fastapi import APIRouter, Path
from model import Todo, Item

router = APIRouter()

todos = []

@router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todos.append(todo)
    return {"message": "Todo added successfully."}

