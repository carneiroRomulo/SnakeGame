import pygame
from pygame.locals import *
import time
import random

BLOCK_SIZE = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FONT_COLOR = (255, 255, 255)


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


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")

        pygame.mixer.init()
        self.play_background_music()
        pygame.mixer.music.set_volume(0.3)

        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.render_background()

        self.snake = Snake(self.surface, 2)
        self.snake.draw()

        self.apple = Apple(self.surface)
        self.apple.draw()

    # noinspection PyMethodMayBeStatic
    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + BLOCK_SIZE:
            if y2 <= y1 < y2 + BLOCK_SIZE:
                return True

        return False

    # noinspection PyMethodMayBeStatic
    def play_sound(self, sound):
        music = pygame.mixer.Sound(f"sounds/{sound}.wav")
        music.set_volume(0.3)
        music.play()

    # noinspection PyMethodMayBeStatic
    def play_background_music(self):
        pygame.mixer.music.load("sounds/background.wav")
        pygame.mixer.music.play()

    def render_background(self):
        background = pygame.image.load("images/background.jpg")
        self.surface.blit(background, (0, 0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Snake Colliding With Apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("eat")
            self.snake.increase_size()
            self.apple.move()

        # Snake Colliding With Itself
        for i in range(1, self.snake.size):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("quack")
                raise Exception("Game over")

        # Cross The Map Boundary
        if self.snake.x[0] == SCREEN_WIDTH:
            self.snake.x[0] = 0
        if self.snake.x[0] == - BLOCK_SIZE:
            self.snake.x[0] = SCREEN_WIDTH

        if self.snake.y[0] == SCREEN_HEIGHT:
            self.snake.y[0] = 0
        if self.snake.y[0] == - BLOCK_SIZE:
            self.snake.y[0] = 0

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.size}", True, FONT_COLOR)
        self.surface.blit(score, (SCREEN_WIDTH - 180, SCREEN_HEIGHT - (SCREEN_HEIGHT - 20)))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 20)

        line1 = font.render(f"Game over! Your score was: {self.snake.size}", True, FONT_COLOR)
        text_rect1 = line1.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30))
        self.surface.blit(line1, text_rect1)

        line2 = font.render(f"To play again press ENTER, to exit press ESCAPE", True, FONT_COLOR)
        text_rect2 = line2.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.surface.blit(line2, text_rect2)
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False
                        self.snake.size = 2

                    if not pause:
                        if not self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[1], self.snake.y[1]):
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

            try:
                if not pause:
                    self.play()
            except Exception:
                self.show_game_over()
                pause = True

            time.sleep(0.1)


if __name__ == '__main__':
    game = Game()
    game.run()
