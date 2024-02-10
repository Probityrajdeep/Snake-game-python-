import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
SNAKE_SIZE = 20
SNAKE_SPEED = 10
APPLE_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.direction = "RIGHT"

    def move(self):
        head = self.body[0]
        x, y = head

        if self.direction == "UP":
            y -= SNAKE_SIZE
        elif self.direction == "DOWN":
            y += SNAKE_SIZE
        elif self.direction == "LEFT":
            x -= SNAKE_SIZE
        elif self.direction == "RIGHT":
            x += SNAKE_SIZE

        self.body = [(x, y)] + self.body[:-1]

    def grow(self):
        tail = self.body[-1]
        x, y = tail

        if self.direction == "UP":
            y += SNAKE_SIZE
        elif self.direction == "DOWN":
            y -= SNAKE_SIZE
        elif self.direction == "LEFT":
            x += SNAKE_SIZE
        elif self.direction == "RIGHT":
            x -= SNAKE_SIZE

        self.body.append((x, y))

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, SNAKE_SIZE, SNAKE_SIZE))

# Apple class
class Apple:
    def __init__(self):
        self.position = (random.randint(0, SCREEN_WIDTH // APPLE_SIZE - 1) * APPLE_SIZE,
                         random.randint(0, SCREEN_HEIGHT // APPLE_SIZE - 1) * APPLE_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, APPLE_SIZE, APPLE_SIZE))

# Main function
def main():
    snake = Snake()
    apple = Apple()
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"

        snake.move()

        if snake.body[0] == apple.position:
            snake.grow()
            apple = Apple()

        snake.draw()
        apple.draw()

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

    pygame.quit()

if __name__ == "__main__":
    main()
