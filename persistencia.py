import json
from config.db import engine
from model.datos import datos as modelo_datos
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class ControladorDatos:
    @classmethod
    def guardar(cls, datos):
        try:
            ins = modelo_datos.insert().values(datos)
            session.execute(ins)
            session.commit()
            print("Datos almacenados")
            return datos
        except Exception as e:
            print(e)
            session.rollback()
            return None
        finally:
            session.close()

    @classmethod
    def consultar(cls):
        try:
            datos_query = session.query(modelo_datos).all()
            datos_dict = []
            for dato in datos_query:
                dato_dict = {
                    "id": dato.id,
                    "estado": dato.estado,
                    "fecha": dato.fecha
                }
                datos_dict.append(dato_dict)
            return json.dumps(datos_dict)
        except:
            session.rollback()
            return False
        finally:
            session.close()

    @classmethod
    def consultarId(cls, id):
        try:
            return session.query(modelo_datos).filter(modelo_datos.id == id)
        except:
            session.rollback()
            return False
        finally:
            session.close()