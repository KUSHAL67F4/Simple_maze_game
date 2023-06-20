import pygame
from pygame.locals import *

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define block size and maze dimensions
BLOCK_SIZE = 50
MAZE_WIDTH = 21
MAZE_HEIGHT = 12

# Define maze
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#"],
    ["#", ".", "#", "#", "#", ".", "#", "#", "#", "#", ".", "#", ".", "#", ".", "#", "#", "#", ".", "#", "#"],
    ["#", ".", "#", "O", "#", ".", "#", "#", "#", "#", ".", "#", ".", "#", ".", "#", "#", "#", ".", ".", "."],
    ["#", ".", "#", ".", ".", ".", "#", "#", "#", "#", "O", "#", ".", "#", ".", "#", "#", "#", "#", "#", "."],
    ["#", ".", "#", "#", "#", "#", "#", "#", "#", "#", ".", "#", ".", "#", ".", ".", ".", "#", "#", "#", "."],
    ["#", ".", ".", ".", ".", ".", "#", "#", "#", "#", ".", "#", ".", "#", ".", "#", "#", ".", ".", ".", "."],
    ["#", ".", "#", "#", "#", "#", ".", ".", "#", "#", ".", "#", ".", "#", ".", "#", "#", "#", "#", "#", "."],
    ["#", ".", "#", "#", "#", ".", ".", ".", ".", "#", ".", "#", "O", "#", "#", ".", ".", ".", ".", ".", "."],
    ["#", ".", ".", ".", ".", ".", "O", "#", ".", ".", "#", "#", ".", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", ".", "#", "#", "#", "#", "#"]
]

# Define player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.rect.x += dx * BLOCK_SIZE
        self.rect.y += dy * BLOCK_SIZE

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x >= MAZE_WIDTH * BLOCK_SIZE:
            self.rect.x = (MAZE_WIDTH - 1) * BLOCK_SIZE

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y >= MAZE_HEIGHT * BLOCK_SIZE:
            self.rect.y = (MAZE_HEIGHT - 1) * BLOCK_SIZE

        if maze[self.rect.y // BLOCK_SIZE][self.rect.x // BLOCK_SIZE] == "#":
            self.rect.x -= dx * BLOCK_SIZE
            self.rect.y -= dy * BLOCK_SIZE

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((MAZE_WIDTH * BLOCK_SIZE, MAZE_HEIGHT * BLOCK_SIZE))
pygame.display.set_caption("Maze Game")

# Create player sprite
player = Player(BLOCK_SIZE, BLOCK_SIZE)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                player.move(0, -1)
            elif event.key == K_DOWN:
                player.move(0, 1)
            elif event.key == K_LEFT:
                player.move(-1, 0)
            elif event.key == K_RIGHT:
                player.move(1, 0)

    screen.fill(WHITE)

    # Draw maze
    for row in range(MAZE_HEIGHT):
        for col in range(MAZE_WIDTH):
            if maze[row][col] == "#":
                pygame.draw.rect(screen, BLACK, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            elif maze[row][col] == "O":
                pygame.draw.rect(screen, WHITE, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Draw player
    all_sprites.draw(screen)

    # Check if player reached the end
    if player.rect.x // BLOCK_SIZE == 15 and player.rect.y // BLOCK_SIZE == 11:
        print("\n\nYou Won The Game\n\n")
        running = False

    pygame.display.flip()

pygame.quit()
