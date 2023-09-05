from typing import List
from uuid import uuid4
from fastapi import FastAPI
from  model import Gender, Role, User
from uuid import UUID
from fastapi import HTTPException


app = FastAPI()
bd: List[User] = [
  User(
    id=uuid4(),
    primeiro_nome="Pedro",
    ultimo_nome="Almeida",
    gender=Gender.masculino,
    roles=[Role.user]
  ),
  User(
    id=uuid4(),
    primeiro_nome="Cecilia",
    ultimo_nome="Santos",
    gender=Gender.femenino,
    roles=[Role.user],
  ),
  User(
    id=uuid4(),
    primeiro_nome="Andrew",
    ultimo_nome="Carvalho",
    gender=Gender.masculino,
    roles=[Role.user],
  ),
  User(
    id=uuid4(),
    primeiro_nome="Maria",
    ultimo_nome="Silva",
    gender=Gender.femenino,
    roles=[Role.user],
  ),
]

@app.get("/")
async def root():
  return{"Hello": "World",}
@app.get("/api/v1/users")
async def get_users():
  return bd
@app.post("/api/v1/users")
async def create_user(user: User):
  bd.append(user)
  return{"id": user.id}
@app.delete("/api/v1/users/{id}")
async def delete_user(id:UUID):
  for user in bd:
    if user.id == id:
      bd.remove(user)
      return
    raise HTTPException(
      status_code=404, detail=f"Delete user failed,id {id} not found."
    )
@app.put("/api/v1/user/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
  for user in bd:
    if user.id == id:
      if user_update.primeiro_nome is not None:
        user.primeiro_nome= user_update.primeiro_nome
        if user_update.ultimo_nome is not None:
          user.ultimo_nome = user_update.ultimo_nome
          user.roles = user_update.roles
          return user.id
        raise HTTPException(status_code=404, detail=f"Could not find user with id:{id}")