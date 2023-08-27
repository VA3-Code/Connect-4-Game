import pygame


# initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((960, 540), pygame.RESIZABLE)

# Game Loop
running = True

while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()