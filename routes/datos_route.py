import json
from fastapi import APIRouter, Response
from sqlalchemy.exc import SQLAlchemyError
from starlette.status import *
from schemas.data import DataSchema
from persistencia import ControladorDatos as control

datos = APIRouter()

@datos.get('/datos')
def get_all_data():
    respuesta = control.consultar()
    return Response(content=respuesta.__str__(),status_code=HTTP_200_OK)


@datos.post('/datos')
def post_data(data: DataSchema):
    new_data = data.dict()
    try:
        respuesta = control.guardar(datos=new_data)
    except SQLAlchemyError as e:
        print(f'Error: {e}')
    return Response(content=json.dumps(respuesta), status_code=HTTP_201_CREATED)