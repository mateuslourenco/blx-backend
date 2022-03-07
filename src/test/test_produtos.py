import pytest
from starlette.testclient import TestClient

from src.server import app

client = TestClient(app)


@pytest.fixture
def resp():
    return client.get('/')


def test_listar_produtos(resp):
    assert resp.status_code == 200


@pytest.fixture
def resp_produto_inexistente():
    return client.get('/produtos/1234')


def test_obter_produto_inexistente(resp_produto_inexistente):
    assert resp_produto_inexistente.status_code == 404, resp_produto_inexistente.text
    assert resp_produto_inexistente.json() == {'detail': 'Produto não localizado'}
