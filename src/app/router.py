from fastapi import APIRouter, Path, HTTPException, \
     status, Request, Depends
from fastapi.templating import Jinja2Templates

from .model import Todo, Item, Items

router = APIRouter()

todos = []

templates = Jinja2Templates(directory="src/app/templates/")

@router.post("/todo")
async def add_todo(
    request: Request,
    todo: Todo = Depends(Todo.as_form)
):
    todo.id = len(todos) + 1
    todos.append(todo)
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todos 
    })


@router.get("/todo", response_model=Items)
async def retrieve_todos(request: Request):
    return templates.TemplateResponse(
        "todo.html", 
        {
            "request": request,
            "todos": todos
        })


@router.get("/todo/{todo_id}")
async def get_todo(
    request: Request,
    todo_id: int = Path(
        ...,
        title="ID of todo to retrieve"
    )
):
    for todo in todos:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                "todo.html",
                {
                    "request": request,
                    "todo": todo
                })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with given ID doesn't exist" 
    )


@router.put("/todo/{todo_id}")
async def update_todo(
    request: Request,
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
    request: Request,
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
