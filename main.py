import pygame
from pygame.locals import *
import time
from apple import Apple
from snake import Snake

BLOCK_SIZE = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FONT_COLOR = (255, 255, 255)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")

        pygame.mixer.init()
        self.play_background_music()
        pygame.mixer.music.set_volume(0.3)

        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.render_background()

        self.pause = False
        self.running = True

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

        # Hit The Map Boundary
        if self.snake.x[0] == SCREEN_WIDTH or self.snake.x[0] == - BLOCK_SIZE or self.snake.y[0] == SCREEN_HEIGHT \
                or self.snake.y[0] == - BLOCK_SIZE:
            self.play_sound("quack")
            raise Exception("Game over")

    def reset_game(self):
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)

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

        self.pause = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                    if event.key == K_RETURN:
                        self.pause = False
                        self.reset_game()

                    if not self.pause:
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
                    self.running = False

            try:
                if not self.pause:
                    self.play()
            except Exception:
                self.show_game_over()

            time.sleep(0.05)


if __name__ == '__main__':
    game = Game()
    game.run()
