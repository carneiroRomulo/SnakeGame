import pygame

BLOCK_SIZE = 20


class Snake:
    def __init__(self, surface, size):
        self.surface = surface
        self.size = size

        self.block = pygame.image.load("images/snake.png").convert()
        self.block = pygame.transform.scale(self.block, (BLOCK_SIZE, BLOCK_SIZE))

        self.direction = 'down'
        self.x = [BLOCK_SIZE]*self.size
        self.y = [BLOCK_SIZE]*self.size

    def increase_size(self):
        self.size += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
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
