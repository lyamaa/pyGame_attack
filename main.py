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
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# GAME LOOP
running = True

while running:
    # RGB
    screen.fill((0, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arroe pressed")
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                print("Right key pressed")
                playerX_change = 0.1
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("KEY Released")
                playerX_change = 0
                playerY_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
