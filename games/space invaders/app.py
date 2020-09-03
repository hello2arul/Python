import pygame
import random
import math
from pygame import mixer

# initializes pygame
pygame.init()

# creates the screen with 800 width and 600 height
screen = pygame.display.set_mode((800, 600))

# background music
mixer.music.load("assets/background.wav")
# to continuously play the music, provide -1
mixer.music.play(-1)

# setting the title of the widow
pygame.display.set_caption("Space Invaders")

# 32px icon from flaticon.com
icon = pygame.image.load("assets/ufo-24.png")
# setting the icon in the window near the title
pygame.display.set_icon(icon)

# backgroud image
backgroudImg = pygame.image.load("assets/background.png")

# player
# 64px icon from flaticon.com
playerImg = pygame.image.load("assets/ufo-64.png")
# to place the ufo in the bottom middle of the screen
playerX = 370
playerY = 480
playerX_change = 0

# enemies
enemyImgs = []
enemyXs = []
enemyYs = []
enemyXs_change = []
enemyYs_change = []
number_of_enemies = 10

# adding multiple enemies with the same image
for enemyIdx in range(number_of_enemies):
    enemyImgs.append(pygame.image.load("assets/alien-32.png"))
    # to place the enemy in random position
    # X - anywhere from left to right
    enemyXs.append(random.randint(0, 736))
    # Y - anywhere from 50 to 150, i.e top to a bit bottom
    enemyYs.append(random.randint(50, 150))
    # left to right change
    enemyXs_change.append(1)
    # when it hits the boundary move it down by 40 px
    enemyYs_change.append(40)



# bullet
bulletImg = pygame.image.load("assets/bullet.png")
# initial position of the bullet is same as the spaceship 
bulletX = 0
bulletY = 480
bulletY_change = 5
bullet_state = "ready"

# score
score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def display_score(x, y):
    # RGB - white
    score_to_render = score_font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_to_render, (x, y))
    
def draw_player(x, y):
    # scren.blit - draws the playerImg in the specified position
    # X - distance from the left
    # Y - distance from the top
    screen.blit(playerImg, (x, y))

def draw_enemy(x, y, idx):
    screen.blit(enemyImgs[idx], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # to make the bullet appear from the nose of spaceship
    screen.blit(bulletImg, (x + 16, y + 10)) 

def is_colliding(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bulletX - enemyX, 2) + math.pow(bulletY - enemyY, 2))
    # 27 gives accurate result
    return distance < 27 


def game_over():
    game_over_sound = mixer.Sound("assets/game-over.wav")
    game_over_sound.play()
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    # 200, 250 -> middle of the screen
    screen.blit(game_over_text, (200, 250))
    


# Game loop
running = True
while running:
    # iterates through every event occuring 
    for event in pygame.event.get():
        # checks if event is QUIT
        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN - checks if keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                # play sound
                bullet_sound = mixer.Sound("assets/laser.wav")
                bullet_sound.play()
                # fire the bullet only when the bullet is in ready state
                if bullet_state == "ready":
                    # bulledX prevents the bullet from following the ship even after fired
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            
        # KEYUP - checks if keys are released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    
    # RGB - each color ranges from 0 - 255
    # screen.fill((0, 0, 0))
    # to make the background image appear from the 0,0 position
    screen.blit(backgroudImg, (0,0))    

    # player movement
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    # total width - spaceship width => 800 - 64 
    if playerX >= 736:
        playerX = 736

    # enemy movement
    for enemyIdx in range(number_of_enemies):
        # if enemy reaches the spaceship's position, remove every enemy from the screen
        # and display game over
        if enemyYs[enemyIdx] > 440:
            for idx in range(number_of_enemies):
                enemyYs[idx] = 2000
            game_over()
            break

        enemyXs[enemyIdx] += enemyXs_change[enemyIdx]

        if enemyXs[enemyIdx] <= 0:
            enemyXs_change[enemyIdx] = 10
            # if end is reached, come down a row
            enemyYs[enemyIdx] += enemyYs_change[enemyIdx]

        # total width - enemy width => 800 - 64
        if enemyXs[enemyIdx] >= 736:
            enemyXs_change[enemyIdx] = -10
            # if end is reached, come down a row
            enemyYs[enemyIdx] += enemyYs_change[enemyIdx]

        # collision
        if is_colliding(enemyXs[enemyIdx], enemyYs[enemyIdx], bulletX, bulletY):
            exploding_sound = mixer.Sound("assets/explosion.wav")
            exploding_sound.play()
            bullet_state = "ready"
            bulletY = 480
            # after the bullet hits the enemy, respawn it to a random position and update the score
            score += 1
            # print(score)
            enemyXs[enemyIdx] = random.randint(0, 736)
            enemyYs[enemyIdx] = random.randint(50, 150)
        
        draw_enemy(enemyXs[enemyIdx], enemyYs[enemyIdx], enemyIdx)

    # bullet movement
    # reset the bullet position once it hits the top
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        # bullet goes up
        bulletY -= bulletY_change

    display_score(textX, textY)
    draw_player(playerX, playerY)
    

    # updates the screen with whatever drawn on the screen
    pygame.display.update()
