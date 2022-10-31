def event_action(event, bullet, player):
    if event.type == pygame.QUIT:
        global running
        running = False

    # Controling the player movement from the arrow keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player["x"] -= 1.7
        if event.key == pygame.K_RIGHT:
            player["x"] += 1.7
        if event.key == pygame.K_SPACE:
            # Fixing the change of direction of bullet
            bullet = fix_bullet_direction(bullet, player)
    #if event.type == pygame.KEYUP:
     #   player_Xchange = 0
    return bullet, player

def fix_bullet_direction(bullet, player):
    if bullet["state"] is "rest":
        bullet["x"] = player["x"]
        bullet = show_bullet(bullet)
        play_sound('data/bullet.wav')
    return bullet

def play_sound(dir):
    sound = mixer.Sound(dir)
    sound.play()