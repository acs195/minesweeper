from main import app
from repos.in_memory.game import GameRepo
from tests.conftest import FakeGameRepo

app.dependency_overrides[GameRepo] = FakeGameRepo


def test_game_start(test_client):
    """Test the api to start a new game"""
    response = test_client.post("/api/v1/games/start")
    assert response.status_code == 200
    game = response.json()
    for field in ["id", "board"]:
        assert field in game
    for field in ["id", "slots"]:
        assert field in game["board"]


def test_game_pick_slot(test_client, game):
    """Test to pick a slot in the game"""
    slot = {"x": 1, "y": 1}
    response = test_client.post(f"/api/v1/games/{game.id}/pick-slot", json=slot)
    assert response.status_code == 200
    game = response.json()
    for field in ["id", "board"]:
        assert field in game
    for field in ["id", "slots"]:
        assert field in game["board"]


def test_game_pick_slot_already_picked(test_client, game):
    """Test to pick a slot already picked in the game"""
    game.board.slots[1][1].available = False
    slot = {"x": 1, "y": 1}
    response = test_client.post(f"/api/v1/games/{game.id}/pick-slot", json=slot)
    assert response.status_code == 400
    assert response.json()["detail"] == f"Cannot pick slot {slot['x']}x{slot['y']}"


def test_game_toggle_flag_slot(test_client, game):
    """Test to toogle a flag"""
    slot = {"x": 1, "y": 1}
    response = test_client.post(f"/api/v1/games/{game.id}/toggle-flag-slot", json=slot)
    assert response.status_code == 200
    game = response.json()
    assert game["board"]["slots"][slot["x"]][slot["y"]]["flag"] is True
