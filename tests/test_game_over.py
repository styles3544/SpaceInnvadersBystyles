import pytest

from game import game_over, remove_invaders

def test_game_over():
    player = {
        "x": 150, 
        "y": 523
    }
    new_invader = {
        "x": 100,
        "y": 500
    }
    invaders = []
    no_of_invaders = 8
    for num in range(no_of_invaders):
        invader = {
            "x": 100,
            "y": 500,
            "x_change": 1.2,
            "y_change": 50
        }
        invaders.append(invader)
    game_object = game_over(invaders, new_invader, player)

    for invader in game_object[0]:
        assert invader["y"] == 2000
    assert game_object[1]["y"] == 500
    assert game_object[2] == True
