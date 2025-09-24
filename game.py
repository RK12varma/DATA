import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake setup
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def score_display(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])


def gameLoop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2

    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            msg = font.render("You Lost! Press Q-Quit or C-Play Again", True, RED)
            screen.blit(msg, [WIDTH / 6, HEIGHT / 3])
            score_display(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = snake_block
                    dx = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += dx
        y += dy
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        score_display(snake_length - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
