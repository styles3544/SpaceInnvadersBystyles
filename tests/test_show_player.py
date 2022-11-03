import pygame
from game import show_player

def test_show_player():
    player = {
        "x": 370,
        "y": 523
    }
    assert show_player(player) == None

