import pytest
from starlette.testclient import TestClient

from src.server import app

client = TestClient(app)


def test_listar_produtos():
    resp = client.get('/')
    assert resp.status_code == 200


def test_obter_produto_inexistente():
    resp = client.get('/produtos/1234')
    assert resp.status_code == 404, resp.text
    assert resp.json() == {'detail': 'Produto não localizado'}
