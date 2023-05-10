from datetime import datetime

from pydantic import  BaseModel
from typing import Optional

class DataSchema(BaseModel):
    id: Optional[int]
    estado: str
    fecha: int

    def as_dict(self):
        return {"id": self.id, "estado": self.estado, "fecha": self.fecha}