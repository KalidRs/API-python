from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Genero, Rol, User, UpdateUser  

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        nombre="kalid",
        apellidos="reyes",
        genero=Genero.masculino,
        roles=[Rol.admin],
    ),
    User(
        id=uuid4(),
        nombre="Abril",
        apellidos="Galindo",
        genero=Genero.femenino,
        roles=[Rol.admin],
    ),
    User(
        id=uuid4(),
        nombre="José Daniel",
        apellidos="Loza Marín",
        genero=Genero.otro,
        roles=[Rol.user],
    ),
]

@app.get("/")
async def root():
    return {"message": "Hola ", "description": "Esto es FastAPI"}

@app.get("/users")
async def get_users():
    return db

@app.post("/create-users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": f"Usuario con ID {id} eliminado exitosamente."}
    raise HTTPException(
        status_code=404, detail=f"Error al eliminar, ID {id} no encontrado."
    )

@app.put("/users/{id}")
async def update_user(id: UUID, user_update: UpdateUser):
    for user in db:
        if user.id == id:
            if user_update.nombre is not None:
                user.nombre = user_update.nombre
            if user_update.apellidos is not None:
                user.apellidos = user_update.apellidos
            if user_update.genero is not None:
                user.genero = user_update.genero
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": f"Usuario con ID {id} actualizado exitosamente."}
    raise HTTPException(
        status_code=404, detail=f"Error al actualizar, ID {id} no encontrado."
    )
