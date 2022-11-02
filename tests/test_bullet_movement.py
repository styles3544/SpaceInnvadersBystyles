import pytest
from game import bullet_movement


def test_bullet_movement():

    bullet1 = {
        "y": 0,
        "state": "rest"
    }
    bullet2 = {
        "y": 500,
        "state": "rest"
    }
    bullet3 = {
        "y": -10,
        "state": "fire"
    }
    bullet4 = {
        "y": 500,
        "state": "fire"
    }
    assert bullet_movement(bullet1)["y"] == 600
    assert bullet_movement(bullet1)["state"] == "rest"
    assert bullet_movement(bullet2)["y"] == 500
    assert bullet_movement(bullet2)["state"] == "rest"
    assert bullet_movement(bullet3)["y"] == 600
    assert bullet_movement(bullet3)["state"] == "rest"
    with pytest.raises(NameError):
        bullet_movement(bullet4)
