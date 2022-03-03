from fastapi import FastAPI

from src.routers import rotas_produtos, rotas_usuarios

app = FastAPI()


@app.get('/')
def home():
    return {'msg': 'BLX - Back-end API'}


# Rotas de produtos
app.include_router(rotas_produtos.router)


# Rotas de usuarios
app.include_router(rotas_usuarios.router)
