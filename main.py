import pygame
import random

# Initialize the pygame
pygame.init()


# Create Screen
screen = pygame.display.set_mode((800, 600))

# Backgroud Image
background = pygame.image.load("img/back.jpg")

# Title and Icon
pygame.display.set_caption("Space Attacks")
icon = pygame.image.load("img/rocket.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("img/spaceship.png")
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


# bullets
bulletImg = pygame.image.load("img/bullets.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"

    screen.blit(bulletImg, (x + 16, y + 10))


# GAME LOOP
running = True

while running:
    # RGB
    screen.fill((0, 255, 0))
    # background img
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Left arroe pressed")
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("Right key pressed")
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                print("Right key pressed")
                bulletX = playerX
                bullet_fire(bulletX, bulletY)
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

    #  Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change

    playerY += playerY_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
