import pygame
from constants import *
from player import * 

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = []
    drawable = []

    player = Player(x, y)
    updatable.append(player)
    drawable.append(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for up in updatable:
            up.update(dt)

        screen.fill((0, 0, 0))

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
