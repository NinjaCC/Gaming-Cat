import math

import pygame
import random
pygame.init()

MAX_WIDTH = 1500
MAX_HEIGHT = 800
FPS = 60

BLACK_COLOR = (0,0,0)

# Set up the drawing window  - SIZE of the window
screen = pygame.display.set_mode([MAX_WIDTH, MAX_HEIGHT])
clock = pygame.time.Clock()

circle_left = 100
circle_left_dir = 1
circle_top = 250
circle_top_dir = 1
score=0
personImg = pygame.image.load('person.png')
jumpSound = pygame.mixer.Sound('jump.mp3')

level = []
for i in range(10000):
    if random.randint(0, 100) < min(10,int(i/10)):
        level.append(1)
    else:
        level.append(0)
level_pos = 0
obstacle_pos=0
is_jumping=False
jumping_percent=0
# 0 = no obstace, 1 = obstance
#ok mmhmok

FONT = pygame.font.SysFont("Courier New", 100)  # name, size


def display_text(message, x, y, size = 30):
    text_color = (0, 0, 0)
    #f = pygame.font.SysFont("Courier New", size)  # name, size
    text = FONT.render(message, False, text_color)
    screen.blit(text, (x, y))

def draw_person(x,y):
    screen.blit(personImg,( x, y))
    # display_text("  O ", x, y, size)
    # display_text(" /|\\", x, y + size, size)
    # display_text(" / \\", x, y + size*2, size)
    #pygame.draw.circle(screen,BLACK_COLOR,(x + 25,y + 25 ), 25)
    #pygame.draw.line(screen, BLACK_COLOR, (x + 20, y + 50), (x+20, y+100), 10)
# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Make background white
    screen.fill((255, 255, 255))

    circle_color = (0, 0, 255)
    circle_pos = (circle_left, circle_top)  # pos from left, top
    circle_size = 30

    circle_speed = 2
    circle_left = circle_left + circle_speed * circle_left_dir
    circle_top = circle_top + circle_speed * circle_top_dir

    if circle_top > MAX_HEIGHT:
        circle_top_dir = -1
    if circle_left > MAX_WIDTH:
        circle_left_dir = -1
    if circle_top < 0:
        circle_top_dir = 1
    if circle_left < 0:
        circle_left_dir = 1

    # here ball hits paddle
    circle_bottom = circle_top + circle_size / 2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and jumping_percent==0:
        is_jumping= True
        jumping_percent=1
    if not jumping_percent ==0:
        jumping_percent=jumping_percent+1
    if jumping_percent==50:
        is_jumping=False
        jumping_percent=-20

    if is_jumping:
        y_pos = int(math.sin(jumping_percent/50*math.pi) * 200)
        draw_person(20,510-y_pos)
    else:
        draw_person(20,510)

    pygame.draw.circle(screen, circle_color, circle_pos, circle_size)

    # Display level
    pos = 100
    level_pos = level_pos+4
    if level_pos > 50:
        level_pos-=50
        obstacle_pos += 1
        if level[obstacle_pos]==1:
            score=score+1
    for i in range(100):
        display_text("_", i*50 - level_pos, 600, 100)
        if level[obstacle_pos+i] == 1:
            display_text("x", i*50 - level_pos, 625, 100)
    display_text('score '+str(score),20,20)
    if (level[obstacle_pos+2] == 1 or level[obstacle_pos+2] == 1) and not is_jumping:
        if score>1:
            jumpSound.play()
        score=0
    # Flip the display
    pygame.display.flip()
    clock.tick(FPS)
# Done! Time to quit.
pygame.quit()
