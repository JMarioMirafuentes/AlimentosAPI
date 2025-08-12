from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from models.alimento_dto import AlimentoCreateDTO, AlimentoUpdateDTO
from services import alimento_service
from utils.response_handler import success_response, error_response
from exceptions.custom_exceptions import NotFoundException

router = APIRouter(prefix="/alimentos", tags=["Alimentos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_alimentos(db: Session = Depends(get_db)):
    return success_response(alimento_service.get_all(db))

@router.get("/{alimento_id}")
def obtener_alimento(alimento_id: int, db: Session = Depends(get_db)):
    try:
        return success_response(alimento_service.get_by_id(db, alimento_id))
    except NotFoundException as e:
        return error_response(e.message, 404)

@router.post("/")
def crear_alimento(dto: AlimentoCreateDTO, db: Session = Depends(get_db)):
    return success_response(alimento_service.create(db, dto), "Alimento creado correctamente")

@router.put("/{alimento_id}")
def actualizar_alimento(alimento_id: int, dto: AlimentoUpdateDTO, db: Session = Depends(get_db)):
    try:
        return success_response(alimento_service.update(db, alimento_id, dto), "Alimento actualizado correctamente")
    except NotFoundException as e:
        return error_response(e.message, 404)

@router.delete("/{alimento_id}")
def eliminar_alimento(alimento_id: int, db: Session = Depends(get_db)):
    try:
        alimento_service.delete(db, alimento_id)
        return success_response(message="Alimento eliminado correctamente")
    except NotFoundException as e:
        return error_response(e.message, 404)
