import pygame

# Initialize the pygame
pygame.init()


# Create Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Attacks")
icon = pygame.image.load("img/rocket.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("img/spacecraft.png")
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(playerImg, (x, y))


# GAME LOOP
running = True

while running:
    # RGB
    screen.fill((0, 255, 0))
    playerY -= 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()
