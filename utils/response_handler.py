from fastapi.responses import JSONResponse
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel
from typing import Any

def success_response(data: Any = None, message: str = "Operación exitosa"):
    if hasattr(data, "__table__"): 
        data = {c.name: getattr(data, c.name) for c in data.__table__.columns}
    elif isinstance(data, list) and len(data) > 0 and hasattr(data[0], "__table__"):
        data = [{c.name: getattr(item, c.name) for c in item.__table__.columns} for item in data]

    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": message,
            "data": data
        }
    )

def error_response(message="Error interno", status_code=400):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "message": message
        }
    )
