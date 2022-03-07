import pytest
from starlette.testclient import TestClient

from src.server import app

client = TestClient(app)


@pytest.fixture
def resp():
    return client.get('/')


def test_listar_produtos(resp):
    assert resp.status_code == 200
