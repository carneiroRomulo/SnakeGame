import pygame
from pygame.locals import *
import time


class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("images/snake.png").convert()
        self.block = pygame.transform.scale(self.block, (50, 50))

        self.direction = 'down'
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((255, 255, 100))
        self.parent_screen.blit(self.block, (self.x, self.y))
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
        if self.direction == 'left':
            self.x -= 10

        if self.direction == 'right':
            self.x += 10

        if self.direction == 'up':
            self.y -= 10

        if self.direction == 'down':
            self.y += 10

        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((255, 255, 100))

        self.snake = Snake(self.surface)
        self.snake.draw()

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

            self.snake.walk()
            time.sleep(0.05)


if __name__ == '__main__':
    game = Game()
    game.run()
