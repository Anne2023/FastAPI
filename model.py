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
  primeiro_nome: str
  ultimo_nome: str
  gender: Gender
  roles: List[Role]

class UpdateUser(BaseModel):
  primeiro_nome: Optional[str]
  ultimo_nome: Optional[str]
  roles: Optional[List[Role]]