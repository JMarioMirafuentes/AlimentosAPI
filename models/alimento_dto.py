from pydantic import BaseModel

class AlimentoCreateDTO(BaseModel):
    nombre: str
    categoria: str

class AlimentoUpdateDTO(BaseModel):
    nombre: str
    categoria: str

class AlimentoResponseDTO(BaseModel):
    id: int
    nombre: str
    categoria: str

    class Config:
        orm_mode = True
