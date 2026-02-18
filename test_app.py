import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_hello(client):
    resp = client.get('/')
    assert b'Movie Review' in resp.get_data