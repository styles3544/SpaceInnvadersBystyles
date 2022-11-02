from game import event_action
import pytest

running = True


def test_event_action():
    import pygame

    bullet1 = {
        "y": 0,
        "state": "rest"
    }
    bullet2 = {
        "y": 500,
        "state": "fire"
    }
    player1 = {
        "x": 370,
        "y": 523
    }
    player2 = {
        "x": -100,
        "y": 100
    }

    event1 = pygame.event.Event(pygame.QUIT)
    event2 = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
    event3 = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    event4 = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
    event5 = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
    bullet1_return, player1_return, running = event_action(
        event1,
        bullet1,
        player1
    )
    assert bullet1_return == bullet1 and player1_return == player1
    assert not running
    bullet1_return, player1_return, running = event_action(
        event2,
        bullet1,
        player1
    )
    assert bullet1_return == bullet1
    assert player1_return["x"] == 370 - 1.7
    assert running
    with pytest.raises(NameError):
        event_action(event3, bullet1, player1)

    bullet2_return, player2_return, running = event_action(
        event4,
        bullet2,
        player2
    )
    assert bullet2_return == bullet2
    assert player2_return["x"] == -100 + 1.7
    assert running
    bullet2_return, player2_return, running = event_action(
        event5,
        bullet2,
        player2
    )
    assert bullet2_return == bullet2 and player2_return == player2
    assert running
