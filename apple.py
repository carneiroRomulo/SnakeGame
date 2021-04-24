import pygame
import random

BLOCK_SIZE = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Apple:
    def __init__(self, surface):
        self.image = pygame.image.load("images/apple.png").convert()
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))

        self.surface = surface
        self.x = BLOCK_SIZE * 3
        self.y = BLOCK_SIZE * 3

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, int(SCREEN_WIDTH / BLOCK_SIZE) - 1) * BLOCK_SIZE
        self.y = random.randint(1, int(SCREEN_HEIGHT / BLOCK_SIZE) - 1) * BLOCK_SIZE

