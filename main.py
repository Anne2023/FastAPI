from typing import List 
from uuid import uuid4
from fastapi import FastAPI
from  model import Gender, Role, User
from uuid import UUID
from fastapi import HTTPException
from model import UpdateUser


app = FastAPI()
bd: List[User] = [ #inicializei obanco de dados, cm um tipo de list e passei o modelo User
  User(            #com os atributos necessario tais como primeiro e ultimo nome e o genero
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

@app.get("/api/v1/users") #esse código define o endpoint para enviar um novo usuario e recorreu ao decorador @app.post para criar o metodo POST
async def get_users():
  return print(bd)


@app.post("/api/v1/users")
async def create_user(user: User): # criei a função creat_user que aceita user do modelo user e adicionei um recemcriado user ao banco de dados, para retornar o endpoit em objeto json
  bd.append(user)
  return{"id": user.id}

@app.delete("/api/v1/users/{id}") #criei um endpoint de exclusão
async def delete_user(id:UUID): #async cria a função delete_user que recupera o id a partir da URL.
  for user in bd: # diz ao aplicativo para recorrer aos usuarios no banco de dados e verificar o seo id passou correspondente a um usuario no bd
    if user.id == id:
      bd.remove(user) # se o id corresponder a um usuario, o usuario sera excluido, caso contrario sera gerado
      return
    raise HTTPException( # um erro de exceção
      status_code=404, detail=f"Delete user failed,id {id} not found."
    )
  
@app.put("/api/v1/user/{id}") # criei um endpoit de atualização
async def update_user(user_update: UpdateUser, id: UUID): #criei um metodo
  for user in bd: #usando o loop for para verificar se o usuario associado como id esta no bd
    if user.id == id:
      if user_update.primeiro_nome is not None:
        user.primeiro_nome= user_update.primeiro_nome
        if user_update.ultimo_nome is not None:
          user.ultimo_nome = user_update.ultimo_nome
          user.roles = user_update.roles
          return user.id # se for bem sucedido sera retornado o id do usuario
        raise HTTPException(status_code=404, detail=f"Could not find user with id:{id}") # caso nao seja localizado aparecera uma exceção