from fastapi import FastAPI

from src.routers import rotas_produtos, rotas_auth, rotas_pedidos

app = FastAPI()


@app.get('/')
def home():
    return {'msg': 'BLX - Back-end API'}


# Rotas de produtos
app.include_router(rotas_produtos.router)


# Rotas de segurança
app.include_router(rotas_auth.router, prefix='/auth')

# Rotas de pedidos
app.include_router(rotas_pedidos.router)
