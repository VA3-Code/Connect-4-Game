# Example file showing a circle moving on screen
from pygame import init, quit, Vector2, QUIT, K_w, K_s, K_a, K_d
from pygame.display import set_mode, flip
from pygame.time import Clock
from pygame.event import get
from pygame.draw import circle
from pygame.key import get_pressed

# pygame setup
init()
screen = set_mode((960, 540))
clock = Clock()
running = True
dt = 0

player_pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for evnt in get():
        if evnt.type == QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    circle(screen, "red", player_pos, 40)

    keys = get_pressed()

    if keys[K_w]:
        player_pos.y -= 300 * dt

    if keys[K_s]:
        player_pos.y += 300 * dt

    if keys[K_a]:
        player_pos.x -= 300 * dt

    if keys[K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

quit()
