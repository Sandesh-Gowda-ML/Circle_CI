import pytest
from app import app


def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    # assert b'<p>toys</p>' in response.data 



# test_index()