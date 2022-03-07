from fastapi import FastAPI

from src.routers import rotas_produtos, rotas_auth, rotas_pedidos

tags_metadata = [
    {
        "name": "auth",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "produtos",
        "description": "Manage products",
    },
    {
        "name": "pedidos",
        "description": "Manage orders",
    },
]

app = FastAPI(openapi_tags=tags_metadata)


@app.get('/')
def home():
    return {'msg': 'BLX - Back-end API'}


# Rotas de segurança
app.include_router(rotas_auth.router, prefix='/auth', tags=['auth'])

# Rotas de produtos
app.include_router(rotas_produtos.router, tags=['produtos'])

# Rotas de pedidos
app.include_router(rotas_pedidos.router, tags=['pedidos'])
