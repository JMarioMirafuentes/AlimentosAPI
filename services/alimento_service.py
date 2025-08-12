from sqlalchemy.orm import Session
from models.alimento_entity import Alimento
from models.alimento_dto import AlimentoCreateDTO, AlimentoUpdateDTO
from exceptions.custom_exceptions import NotFoundException

def get_all(db: Session):
    return db.query(Alimento).all()

def get_by_id(db: Session, alimento_id: int):
    alimento = db.query(Alimento).filter(Alimento.id == alimento_id).first()
    if not alimento:
        raise NotFoundException(f"Alimento con ID {alimento_id} no encontrado")
    return alimento

def create(db: Session, alimento_dto: AlimentoCreateDTO):
    nuevo_alimento = Alimento(**alimento_dto.dict())
    db.add(nuevo_alimento)
    db.commit()
    db.refresh(nuevo_alimento)
    return nuevo_alimento

def update(db: Session, alimento_id: int, alimento_dto: AlimentoUpdateDTO):
    alimento = get_by_id(db, alimento_id)
    alimento.nombre = alimento_dto.nombre
    alimento.categoria = alimento_dto.categoria
    db.commit()
    db.refresh(alimento)
    return alimento

def delete(db: Session, alimento_id: int):
    alimento = get_by_id(db, alimento_id)
    db.delete(alimento)
    db.commit()
