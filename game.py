from multiprocessing import Event
import pygame
import random
import math
from pygame import mixer

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

bulletImage = pygame.image.load('data/bullet.png')

mixer.init()
mixer.music.load('data/background.wav')
mixer.music.play(-1)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


# FUNCTIONS #

def show_score(score, x, y):
    score_text = font.render("Points: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

    
def game_over_display():
    """
    Display game-over when the player has lesser than or equal to an 80 point difference from the invader and the invader is above 450 points.

    Parameters:
    ----
    N.A

    Display:
    ----
    "GAME OVER" <string> in defined font and at approriate position 
    
    """  
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (190, 250))


def reset_player_X(player_X: float) -> float:
    """
    Resets the x-coordinates of the player if outside the screen

    Parameters:
    ----
    player_X <float>: Current x-coordinate

    Return:
    ----
    player_X <float>: Updated x-coordinate
    """
    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750
    return player_X


def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance <= 50:
        return True
    else:
        return False


def show_player(player):
    screen.blit(playerImage, (player["x"] - 16, player["y"] + 10))


def show_invader(invader):
    screen.blit(invaderImage, (invader["x"], invader["y"]))


def show_bullet(bullet):
    screen.blit(bulletImage, (bullet["x"], bullet["y"]))
    bullet["state"] = "fire"
    return bullet


def event_action(event: object,
                bullet: dict[str, float],
                player: dict[str, float]) -> \
                tuple[dict[str, float], dict[str, float], bool]:
    """
    Given an event (key), updates the player and bullet dictionary

    Parameters:
    ----
    event <class 'Event'>: pygame.event.Event(), a representation of a key.
    
    bullet <dict[str, float]>: bullet associated data dictionary
    
    player <dict[str, float]>: player associated data dictionary
    
    Return:
    ----
    tuple(bullet, player, running)

    bullet <dict[str, float]>: bullet associated data dictionary
    
    player <dict[str, float]>: player associated data dictionary
    
    running <bool>: indicator whether to keep running the loop
    """
    running = True
    if event.type == pygame.QUIT:
        running = False

    # Controling the player movement from the arrow keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player["x"] -= 5
        if event.key == pygame.K_RIGHT:
            player["x"] += 5
        if event.key == pygame.K_SPACE:
            # Fixing the change of direction of bullet
            bullet = fix_bullet_direction(bullet, player)

    return bullet, player, running


def fix_bullet_direction(bullet, player):
    """
    Given the x coordinate of the player (value), shoots the bullet from that position
    
    Parameters:
    ----
    event <class 'Event'>: pygame.event.Event(), a representation of a key.
    
    bullet <dict[str, float]>: bullet associated data dictionary
    
    player <dict[str, float]>: player associated data dictionary
    
    Return:
    ----

    bullet <dict[str, float]>: bullet associated data dictionary
  
    """    
    if bullet["state"] == "rest":
        bullet["x"] = player["x"]
        bullet = show_bullet(bullet)
        play_sound('data/bullet.wav')
    return bullet


def play_sound(dir):
    sound = mixer.Sound(dir)
    sound.play()


def update_invaders_x(invaders):
    for invader in invaders:
        invader["x"] += invader["x_change"]
    return invaders


def bullet_movement(bullet: dict[str, float]) -> dict[str, float]:
    """
    Given an event (key), updates the player and bullet dictionary

    Parameters:
    ----
    bullet <dict[str, int]>: bullet associated data dictionary
    
    Return:
    ----
    bullet <dict[str, int]>: bullet associated data dictionary
    """
    if bullet["y"] <= 0:
        bullet["y"] = 600
        bullet["state"] = "rest"
    if bullet["state"] == "fire":
        show_bullet(bullet)
        bullet["y"] -= bullet["y_change"]
    return bullet


def game_over(invaders, invader, player):
    is_game_over = False
    if invader["y"] >= 450:
        if abs(player["x"]-invader["x"]) < 80:
            invaders = remove_invaders(invaders)
            game_over_display()
            is_game_over = True
    return invaders, invader, is_game_over


def remove_invaders(invaders):
    for invader_ in invaders:
        invader_["y"] = 2000
        play_sound('data/explosion.wav')
    return invaders


def move_next_line(invader):
    if invader["x"] >= 735 or invader["x"] <= 0:
        invader["x_change"] *= -1
        invader["y"] += invader["y_change"]
    return invader


def update_score_and_invaders(score, bullet, invader):
    score += 1
    bullet["y"] = 600
    bullet["state"] = "rest"
    invader["x"] = random.randint(64, 736)
    invader["y"] = random.randint(30, 200)
    invader["x_change"] *= -1
    return score, bullet, invader


if __name__ == "__main__":

    # INITIALIZE #
    pygame.init()

    # creating screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # caption and icon
    pygame.display.set_caption("Welcome to Space Invaders Game by:- styles")

    # Score
    score = 0
    scoreX = 5
    scoreY = 5
    font = pygame.font.Font('freesansbold.ttf', 20)

    # Game Over
    game_over_font = pygame.font.Font('freesansbold.ttf', 64)

    # Background Sound
    mixer.music.load('data/background.wav')
    mixer.music.play(-1)

    # player
    playerImage = pygame.image.load('data/spaceship.png')
    player = {
        "x": 370,
        "y": 523
    }

    # Invader
    invaders = []
    no_of_invaders = 8
    invaderImage = pygame.image.load('data/alien.png')
    for num in range(no_of_invaders):
        invader = {
            "x": random.randint(64, 737),
            "y": random.randint(30, 180),
            "x_change": 1.2,
            "y_change": 50
        }
        invaders.append(invader)

    # Bullet
    # rest - bullet is not moving
    # fire - bullet is moving
    bulletImage = pygame.image.load('data/bullet.png')
    bullet = {
        "x": 0,
        "y": 500,
        "y_change": 3,
        "state": "rest"
    }

    # GAME LOOP #

    running = True
    while running:

        # RGB
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            bullet, player, running = event_action(event, bullet, player)

        # updating the invaders x-coordinate
        invaders = update_invaders_x(invaders)

        # bullet movement
        bullet = bullet_movement(bullet)

        # movement of the invader
        for invader in invaders:

            invaders, invader, is_game_over = game_over(
                invaders,
                invader,
                player
            )
            if is_game_over:
                break

            invader = move_next_line(invader)

            # Collision
            collision = isCollision(
                bullet["x"],
                invader["x"],
                bullet["y"],
                invader["y"]
            )
            if collision:
                score, bullet, invader = update_score_and_invaders(
                    score,
                    bullet,
                    invader
                )

            show_invader(invader)

        # restricting the spaceship so that it doesn't go out of screen
        player["x"] = reset_player_X(player["x"])

        show_player(player)
        show_score(score, scoreX, scoreY)
        pygame.display.update()
        
        
        
       
#   '''
#   Test for the iscollision function:
  
#   def test(num : int, msg : str, func_out, exp_out) :
#     if func_out == exp_out :
#         print(f"+ TEST [{num}] PASSED")
#     else :
#         print(f"- TEST [{num}] FAILED; {msg}")
#   '''
