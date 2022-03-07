# blx-backend
[![Python application](https://github.com/mateuslourenco/blx-backend/actions/workflows/python-app.yml/badge.svg)](https://github.com/mateuslourenco/blx-backend/actions/workflows/python-app.yml)


## Descrição 
BLX Backend é uma Rest API de marketplace construída com FastAPI. 

## Documentação
https://blx-backend-api.herokuapp.com/docs

##

- Clone esse repositório
- Instale o piptools 
- Instale as dependencias
- Copie as variáveis de ambiante
- Rode as migrações


```
git clone https://github.com/mateuslourenco/blx-backend
pip install pip-tools
pip-sync requirements.txt dev-requirements.txt
cp contrib/env-sample .env
alembic upgrade head     
```
