from exercise_2.wsgi import WSGI

import pytest
import json
import falcon
from falcon import testing


@pytest.fixture
def client():
	wsgi = WSGI()
	return testing.TestClient(wsgi.create())

def test_get(client):
	path = "/quotes"
	actual = client.simulate_request(method="GET", path=path)
	excpected = {
		"Hello": "World"
	}

	assert actual.status == falcon.HTTP_200
	assert actual.json == excpected

def test_valid_post(client):
	path = "/quotes"
	body = {
		"Hello_again": "world"
	}
	actual = client.simulate_request(method="POST", path=path, body=json.dumps(body))

	assert actual.status == falcon.HTTP_200
	assert actual.json == body

def test_invalid_post(client):
	path = "/quotes"
	actual = client.simulate_request(method="POST", path=path, body=json.dumps({}))

	assert actual.status == falcon.HTTP_400
	assert actual.json == {
		  "message": "Request body is empty"
	}