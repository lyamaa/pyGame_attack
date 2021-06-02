import pygame
import random

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

# Enemy
enemyImg = pygame.image.load("img/cthulhu.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


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

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3

    playerY += playerY_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
