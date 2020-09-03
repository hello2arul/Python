import pygame
import random

#INCOMPLETE

# initialize all imported pygame modules
pygame.init()

# creates the screen with 800 width and 600 height

WIDTH = 576
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# instantiating clock object to control fps
clock = pygame.time.Clock()

# to drop the bird
gravity = 0.25
bird_movement = 0
# setting the title of the widow
pygame.display.set_caption("Flappy Bird")

# 32px icon from flaticon
icon = pygame.image.load("assets/images/favicon.ico")
# setting the icon in the window near the title
pygame.display.set_icon(icon)

# loading all the images 
# scale2x doubles the image size
# .convert() optimizes the image to help pygame run the game smoother
BG_IMAGE = pygame.transform.scale2x(pygame.image.load("assets/images/background-day.png").convert())

# floor_image = pygame.transform.scale2x(pygame.image.load("assets/images/base.png").convert())
floor_image = pygame.image.load("assets/images/base.png").convert()
# to move the floor with the bird
floor_x_pos = 0

# bird_image = pygame.transform.scale2x(pygame.image.load("assets/images/bluebird-midflap.png").convert())
bird_image = pygame.image.load("assets/images/bluebird-midflap.png").convert()
# drawing a rectangle around the bird to detect collison
# placing the bird at 100 from the left, half of the height
bird_rect = bird_image.get_rect(center = (100, 325))

# pipe_image = pygame.transform.scale2x(pygame.image.load("assets/images/pipe-green.png"))
pipe_image = pygame.image.load("assets/images/pipe-green.png")
pipe_list = []
# this event is triggered every 1.2 seconds, a userdefined event
SPAWN_PIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE, 1200)
pipe_heights = [400,600,800]

def draw_floor():
    # creating two floors right next to each other so when the floor moves it will be a bit longer
    screen.blit(floor_image, (floor_x_pos, 580))
    screen.blit(floor_image, (floor_x_pos + 576 / 2, 580))

def create_pipe():
    # picks a random height from the pipe_heights list
    random_pipe_pos = random.choice(pipe_heights)
    # draws a rectangle around the pipe and places the pipe in a random position and returns it
    # -300 is the gap in between the two pipes
    top_pipe = pipe_image.get_rect(midtop = (700, random_pipe_pos - 700))
    bottom_pipe = pipe_image.get_rect(midtop = (700 , random_pipe_pos))
    return top_pipe, bottom_pipe

# takes every pipe and moves it the left and returns the list
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_image, pipe)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # KEYDOWN checks if any key is pressed
        if event.type == pygame.KEYDOWN:
            # if space is pressed, we need to reset the bird_movement to zero
            # because the previous value could be 50 and 50-10 is still downwards
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 10

            # i
        if event.type == SPAWN_PIPE:
            # extend performs tuple unpacking
            pipe_list.extend(create_pipe())
    # y position is from the top, -300 with move the image above to adjust to my small screen
    screen.blit(BG_IMAGE, (0,-300))

    # dropping the bird using the rectangle
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_image, bird_rect)

    # reinitializing pipe list with moved x values
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # moving the floor 
    floor_x_pos -= 1
    draw_floor()
    # if the left floor moves out of the screen reset its position
    if floor_x_pos <= -576 / 20:
        floor_x_pos = 0
    # updates the screen with whatever drawn on the screen
    pygame.display.update()
    # limiting the fps to 120 max
    clock.tick(120)


