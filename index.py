import pygame


# initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((960, 540), pygame.RESIZABLE)

while True:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
