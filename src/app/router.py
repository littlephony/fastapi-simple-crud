from fastapi import APIRouter, Path
from model import Todo, Item

router = APIRouter()

todos = []

@router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todos.append(todo)
    return {"message": "Todo added successfully."}

@router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todos}

@router.get("/todo/{todo_id}")
async def get_todo(
    todo_id: int = Path(
        ...,
        title="ID of todo to retrieve"
    )
) -> dict:
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo with provided ID doesn't exist"}

    
    
