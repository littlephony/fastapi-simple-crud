from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, Item, Items

router = APIRouter()

todos = []


@router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todos.append(todo)
    return {"message": "Todo added successfully"}


@router.get("/todo", response_model=Items)
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
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with given ID doesn't exist" 
    )


@router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: Item,
    todo_id: int = Path(
        ...,
        title="ID of todo to be updated"
    )
) -> dict:
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[idx].item = todo_data.item
            return {"message": "Todo updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with given ID doesn't exist"
    )


@router.delete("/todo/{todo_id}")
async def delete_todo(
    todo_id: int = Path(
        ...,
        title="ID of todo to delete"
    )
) -> dict:
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(idx)
            return {"message": "Todo was deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with given ID doesn't exist"
    )


@router.delete("/todo")
async def delete_todos() -> dict:
    todos.clear()
    return {"message": "Todos were deleted successfully"}
