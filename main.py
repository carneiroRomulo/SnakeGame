import pygame
from pygame.locals import *


def draw_block():
    surface.fill((255, 255, 100))
    surface.blit(snake, (snake_x, snake_y))
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((500, 500))
    surface.fill((255, 255, 100))

    snake = pygame.image.load("images/snake.png").convert()
    snake = pygame.transform.scale(snake, (50, 50))
    snake_x = 10
    snake_y = 10

    surface.blit(snake, (snake_x, snake_y))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    snake_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    snake_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    snake_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    snake_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False
