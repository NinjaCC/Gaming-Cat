
import pygame

pygame.init()

MAX_WIDTH = 1000
MAX_HEIGHT = 500
# Set up the drawing window  - SIZE of the window
screen = pygame.display.set_mode([MAX_WIDTH, MAX_HEIGHT])
score = 0
top_score = 0
FPS = 100
clock = pygame.time.Clock()
RECT_WIDTH = 151
i = 0
circle_left = 100
circle_left_dir = 1
circle_top = 250
circle_top_dir = 1
rect_left = 400
rect_top = 450
# Run until the user asks to quit
running = True
while running:

    if i < 255:
        i = i + 1
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    #            RED  GREEN BLUE , all between 0-255
    screen.fill((i, i, i))

    # Draw a solid blue circle in the center
    circle_color = (255 - i, 255 - i, 255 - i)
    circle_pos = (circle_left, circle_top)  # pos from left, top
    circle_size = 30

    circle_speed = 2
    circle_left = circle_left + circle_speed * circle_left_dir
    circle_top = circle_top + circle_speed * circle_top_dir

    if circle_top > MAX_HEIGHT:
        circle_top_dir = -1
        score = 0
    if circle_left > MAX_WIDTH:
        circle_left_dir = -1
    if circle_top < 0:
        circle_top_dir = 1
    if circle_left < 0:
        circle_left_dir = 1

    FPS = 100 + score * 50

    # here ball hits paddle
    circle_bottom = circle_top + circle_size / 2
    rect_right = rect_left + RECT_WIDTH
    if rect_left < circle_left < rect_right:
        if circle_bottom < rect_top <= circle_bottom + circle_speed * circle_top_dir:
            circle_top_dir = -1
            score = score + 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect_left > 0:
        rect_left -= 5
    if keys[pygame.K_RIGHT] and rect_left < MAX_WIDTH - RECT_WIDTH:
        rect_left = rect_left + 5
    if top_score < score:
        top_score = score

    f = pygame.font.SysFont(pygame.font.get_default_font(), 30)  # name, size
    text = f.render('top scrore ' + str(top_score) + ' score ' + str(score), False, circle_color)
    screen.blit(text, (20, 20))

    pygame.draw.rect(screen, circle_color, pygame.Rect(rect_left, rect_top, RECT_WIDTH, 10))

    pygame.draw.circle(screen, circle_color, circle_pos, circle_size)

    # Flip the display
    pygame.display.flip()
    clock.tick(FPS)
# Done! Time to quit.
pygame.quit()
