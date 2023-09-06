from typing import List, Optional
from uuid import UUID, uuid4
from  pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel

class Gender (str, Enum):
  masculino = "homem"
  femenino = "mulher"

class Role(str, Enum):
  admin = " admin"
  user = "user"
class User(BaseModel): #classe user estende basemodel, sendo então importada de pydantic
  id: Optional[UUID] = uuid4()
  primeiro_nome: str #primeiro nome do usuario
  ultimo_nome: str #ultimo nome do usuario
  gender: Gender #genero do usuario
  roles: List[Role] #lista com funções admin e user

class UpdateUser(BaseModel): #classe user estende basemodel, sendo então importada de pydantic
  primeiro_nome: Optional[str]
  ultimo_nome: Optional[str]
  roles: Optional[List[Role]]