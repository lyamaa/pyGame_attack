import pygame

# Initialize the pygame
pygame.init()


# Create Screen
screen = pygame.display.set_mode((800, 600))


# GAME LOOP
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
