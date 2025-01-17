from fastapi.testclient import TestClient
from macrostrat.embedding_tiler import app
from contextlib import contextmanager
from time import sleep

client = TestClient(app)


def test_tile_request():
    response = client.get("/search/Magmatic%20sulfide%20PGE/tiles/5/6/12")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-protobuf"
    assert response.content is not None
    assert len(response.content) > 0
