from game import reset_player_X


def test_reset_player_X():

    assert reset_player_X(0) == 16
    assert reset_player_X(17) == 17
    assert reset_player_X(800) == 750
