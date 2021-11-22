# PyGAME testing examples, simple functions
import sys, pygame

pygame.init()

size = width, height = 320, 240
speed = [2,2]
black = 0,0,0
color = 224,255,255

screen = pygame.display.set_mode(size, pygame.HIDDEN)
screen.fill(color)
pygame.display.set_mode(size, pygame.SHOWN)


# MAIN all final drawing/displaying is hapening here
while 1:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q: sys.exit() # Quit using key "q" (on release the letter event)
        if event.type == pygame.QUIT: sys.exit() # Quit using red x in the top-right corner
    pygame.display.flip()

# print(f'S: {size}, W: {width}, H: {height}. B: {black}')
