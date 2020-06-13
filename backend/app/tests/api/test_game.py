from main import app
from repos.in_memory.game import GameRepo
from tests.conftest import FakeGameRepo

app.dependency_overrides[GameRepo] = FakeGameRepo


def test_read_main(test_client):
    response = test_client.post("/api/v1/games/start")
    assert response.status_code == 200
    game = response.json()
    for field in ['id', 'board']:
        assert field in game
    for field in ['id', 'slots']:
        assert field in game['board']
