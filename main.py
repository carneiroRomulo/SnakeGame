import pygame
from pygame.locals import *
import time

BLOCK_SIZE = 20
SCREEN_X_SIZE = 600
SCREEN_Y_SIZE = 600


class Apple:
    def __init__(self, surface):
        self.image = pygame.image.load("images/snake.png").convert()
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))

        self.surface = surface
        self.x = BLOCK_SIZE * 3
        self.y = BLOCK_SIZE * 3

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
        pygame.display.flip()


class Snake:
    def __init__(self, surface, size):
        self.surface = surface
        self.size = size

        self.block = pygame.image.load("images/snake.png").convert()
        self.block = pygame.transform.scale(self.block, (BLOCK_SIZE, BLOCK_SIZE))

        self.direction = 'down'
        self.x = [BLOCK_SIZE]*self.size
        self.y = [BLOCK_SIZE]*self.size

    def draw(self):
        self.surface.fill((255, 255, 100))
        for i in range(self.size):
            self.surface.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.size - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= BLOCK_SIZE

        if self.direction == 'right':
            self.x[0] += BLOCK_SIZE

        if self.direction == 'up':
            self.y[0] -= BLOCK_SIZE

        if self.direction == 'down':
            self.y[0] += BLOCK_SIZE

        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_X_SIZE, SCREEN_Y_SIZE))
        self.surface.fill((255, 255, 100))

        self.snake = Snake(self.surface, 10)
        self.snake.draw()

        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.1)


if __name__ == '__main__':
    game = Game()
    game.run()
