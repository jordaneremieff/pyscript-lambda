from pathlib import Path

from fastapi.testclient import TestClient

from src.app import app
from src.app.main import BODY


SRC_PATH = Path(__file__).resolve().parent.parent / "src"


def test_repl():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == BODY
