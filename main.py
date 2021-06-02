import pygame

# Initialize the pygame
pygame.init()


# Create Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Attacks")
icon = pygame.image.load("img/rocket.png")
pygame.display.set_icon(icon)

# GAME LOOP
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB
    screen.fill((255, 255, 255))
    pygame.display.update()
