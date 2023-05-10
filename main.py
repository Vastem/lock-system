from fastapi import FastAPI
from routes.datos_route import datos

app = FastAPI()
app.include_router(datos)