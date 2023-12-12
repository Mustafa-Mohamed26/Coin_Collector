import math
import random
import pygame
from random import randint
import pygame.mixer as m

# Made by Mustafa Mohamed
# Initialize Pygame
pygame.init()

# music pygame
m.music.load('audio\\piccoin.wav')
m.music.play(-1)
m.music.set_volume(1)

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")

# Load images for the fox, fox2 and coin
over_font = pygame.font.Font('freesansbold.ttf', 64)
# fox
foxImg = pygame.image.load("imges\\fox.png")
foxX = 100
foxY = 100
foxX_change = 0
foxY_change = 0
fox_score = 0

# fox2
fox2Img = pygame.image.load("imges\\fox2.png")
fox2X = 700
fox2Y = 100
fox2X_change = 0
fox2Y_change = 0
fox2_score = 0

# coin
coinImg = []
coinX = []
coinY = []
num_of_coins = 6

for i in range(num_of_coins):
    coinImg.append(pygame.image.load("imges\\coin.png"))
    coinX.append(randint(20, WIDTH - 30))
    coinY.append(randint(20, HEIGHT - 30))

# chest
chestImg = pygame.image.load("imges\\Chest.png")
chestX = random.randint(0, 736)
chestY = random.randint(25, 480)

# chest score
chestScore = 0


def fox(x, y):
    screen.blit(foxImg, (x, y))


def fox2(x, y):
    screen.blit(fox2Img, (x, y))


def coin(x, y, index):
    screen.blit(coinImg[index], (x, y))


def chest(x, y):
    screen.blit(chestImg, (x, y))


def isCollision(cx, cy, playerX, playerY):
    distance = math.sqrt(math.pow(playerX - cx, 2) + (math.pow(playerY - cy, 2)))
    if distance < 35:
        return True
    else:
        return False


def fox_winner():
    over_text = over_font.render("THE YELLOW FOX WINS", True, (255, 255, 255))
    screen.blit(over_text, (75, 250))


def fox2_winner():
    over_text = over_font.render("THE RED FOX WINS", True, (255, 255, 255))
    screen.blit(over_text, (75, 250))


running = True
while running:
    # Draw the game
    screen.fill((0, 128, 0))

    # p1_fox score
    font1 = pygame.font.Font(None, 36)
    score1_text = font1.render("Score: " + str(fox_score), True, (255, 255, 255))
    screen.blit(score1_text, (15, 15))

    # p2_fox score
    font2 = pygame.font.Font(None, 36)
    score2_text = font2.render("Score: " + str(fox2_score), True, (255, 255, 255))
    screen.blit(score2_text, (680, 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            # fox
            if event.key == pygame.K_a:
                foxX_change -= 0.5
            if event.key == pygame.K_d:
                foxX_change += 0.5
            if event.key == pygame.K_w:
                foxY_change -= 0.5
            if event.key == pygame.K_s:
                foxY_change += 0.5

            # fox2
            if event.key == pygame.K_LEFT:
                fox2X_change -= 0.5
            if event.key == pygame.K_RIGHT:
                fox2X_change += 0.5
            if event.key == pygame.K_UP:
                fox2Y_change -= 0.5
            if event.key == pygame.K_DOWN:
                fox2Y_change += 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                foxX_change = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                foxY_change = 0

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fox2X_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                fox2Y_change = 0

    # foxX
    foxX += foxX_change
    if foxX <= 0:
        foxX = 0
    elif foxX >= 736:
        foxX = 736

    # fox2X
    fox2X += fox2X_change
    if fox2X <= 0:
        fox2X = 0
    elif fox2X >= 736:
        fox2X = 736

    # foxY
    foxY += foxY_change
    if foxY <= 0:
        foxY = 0
    elif foxY >= 520:
        foxY = 520

    # fox2Y
    fox2Y += fox2Y_change
    if fox2Y <= 0:
        fox2Y = 0
    elif fox2Y >= 520:
        fox2Y = 520

    # coins
    for i in range(num_of_coins):

        # display winner
        if fox_score >= 500:
            for j in range(num_of_coins):
                coinY[j] = 2000
                foxY = 2000
                fox2Y = 2000
                fox_winner()
            break
        elif fox2_score >= 500:
            for j in range(num_of_coins):
                coinY[j] = 2000
                foxY = 2000
                fox2Y = 2000
                fox2_winner()
            break

        # collision for fox
        collision_fox = isCollision(coinX[i], coinY[i], foxX, foxY)
        if collision_fox:
            coinX[i] = random.randint(0, 736)
            coinY[i] = random.randint(25, 400)
            fox_score += 5
            chestScore += 5

        # collision for fox2
        collision_fox2 = isCollision(coinX[i], coinY[i], fox2X, fox2Y)
        if collision_fox2:
            coinX[i] = random.randint(0, 736)
            coinY[i] = random.randint(25, 400)
            fox2_score += 5
            chestScore += 5

        coin(coinX[i], coinY[i], i)

    # chest

    # fox
    collision_fox_chest = isCollision(chestX, chestY, foxX, foxY)
    if collision_fox_chest:
        chestX = random.randint(0, 736)
        chestY = random.randint(25, 480)
        chestScore = 0
        fox_score += random.randint(0, 100)

    # fox2
    collision_fox2_chest = isCollision(chestX, chestY, fox2X, fox2Y)
    if collision_fox2_chest:
        chestX = random.randint(0, 736)
        chestY = random.randint(25, 480)
        chestScore = 0
        fox2_score += random.randint(0, 100)

    if chestScore > 75:
        chest(chestX, chestY)

    fox(foxX, foxY)
    fox2(fox2X, fox2Y)
    pygame.display.update()
