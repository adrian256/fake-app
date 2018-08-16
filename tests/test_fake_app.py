import pytest
from fakeapp import fakeapp

@pytest.fixture
def client():
    client = fakeapp.app.test_client()
    yield client


def test_home(client):
    rv = client.get('/')
    assert b'fake app' in rv.data
