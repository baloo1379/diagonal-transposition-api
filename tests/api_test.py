import pytest
from fastapi.testclient import TestClient
from requests.auth import HTTPBasicAuth
from seed import seeder

from main import app


@pytest.fixture(autouse=True, scope='module')
def setup():
    seeder()
    yield


def test_health():
    with TestClient(app) as client:
        response = client.get('/api/v1')
        assert response.status_code == 200
        assert response.json() == {"health": "ok"}


def test_encode_security():
    auth = HTTPBasicAuth(username='diagonal', password='transposition')
    with TestClient(app) as client:
        response = client.post('/api/v1/encode', auth=auth, json={
            "text": "ola ma kota",
            "secret": "klucz"
        })
        assert response.status_code == 200, response.text
        assert response.json() == {"text": " k ot la a amo "}


def test_encode_no_credentials():
    with TestClient(app) as client:
        response = client.post('/api/v1/encode')
        assert response.json() == {"detail": "Not authenticated"}
        assert response.status_code == 401, response.text
        assert response.headers['WWW-Authenticate'] == 'Basic'


def test_encode_invalid_credentials():
    auth = HTTPBasicAuth(username='invalid', password='credentials')
    with TestClient(app) as client:
        response = client.post('/api/v1/encode', auth=auth)
        assert response.status_code == 401, response.text
        assert response.headers["WWW-Authenticate"] == 'Basic'
        assert response.json() == {"detail": "Incorrect username or password"}


def test_decode_security():
    auth = HTTPBasicAuth(username='diagonal', password='transposition')
    with TestClient(app) as client:
        response = client.post('/api/v1/decode', auth=auth, json={
            "text": " k ot la a amo ",
            "secret": "klucz"
        })
        assert response.status_code == 200, response.text
        assert response.json() == {"text": "ola ma kota    "}


def test_decode_no_credentials():
    with TestClient(app) as client:
        response = client.post('/api/v1/decode')
        assert response.json() == {"detail": "Not authenticated"}
        assert response.status_code == 401, response.text
        assert response.headers['WWW-Authenticate'] == 'Basic'


def test_decode_invalid_credentials():
    auth = HTTPBasicAuth(username='invalid', password='credentials')
    with TestClient(app) as client:
        response = client.post('/api/v1/decode', auth=auth)
        assert response.status_code == 401, response.text
        assert response.headers["WWW-Authenticate"] == 'Basic'
        assert response.json() == {"detail": "Incorrect username or password"}
