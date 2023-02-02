import pytest
from game import fix_bullet_direction


def test_fix_bullet_direction():
    bullet1 = {
        "x": 45,
        "y": 0,
        "state": "rest"
    }
    bullet2 = {
        "y": 500,
        "x": 0,
        "state": "fire"
    }
    player_one = {
        "x": 120,
        "state": "rest"
    }
    player_two = {
        "x": 130 ,
        "state": "rest"
    }
    assert fix_bullet_direction(bullet1, player_one)["x"] == 120
    assert fix_bullet_direction(bullet2, player_two)["x"] != 130

    