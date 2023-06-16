import requests

ENDPOINT = "http://0.0.0.0:8000"


def test_hello_world():
    res = requests.get(ENDPOINT + "/")

    assert res.status_code == 200
    assert res.json() == {"Hello": "World"}
