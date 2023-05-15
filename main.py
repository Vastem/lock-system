from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.datos_route import datos

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir el acceso desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(datos)