import pygame


# initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((960, 540), pygame.RESIZABLE)

pygame.display.set_caption("Connect 4 - Game developed by Mohit and Vinayak")

pygame.display.set_icon(pygame.display.load_image("assets/icon.png"))

# Game Loop
running = True

while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()