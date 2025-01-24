from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum

class Genero(str, Enum):
    masculino = "masculino"
    femenino = "femenino"
    otro = "otro"

class Rol(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Rol]

class UpdateUser(BaseModel):
    nombre: Optional[str] = None
    apellidos: Optional[str] = None
    genero: Optional[Genero] = None
    roles: Optional[List[Rol]] = None
