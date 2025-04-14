import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Rectangle with Chasers")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)

# Main rectangle (target)
target_width, target_height = 60, 40
target_x, target_y = 100, 100
target_speed_x, target_speed_y = 4, 3

# Chasers setup
num_chasers = 5
chasers = []
chaser_size = 30
chaser_speed = 2  # Lower = slower chasers

for _ in range(num_chasers):
    chasers.append({
        'x': random.randint(0, WIDTH - chaser_size),
        'y': random.randint(0, HEIGHT - chaser_size)
    })

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move target
    target_x += target_speed_x
    target_y += target_speed_y

    # Bounce logic
    if target_x <= 0 or target_x + target_width >= WIDTH:
        target_speed_x *= -1
    if target_y <= 0 or target_y + target_height >= HEIGHT:
        target_speed_y *= -1

    # Move chasers toward the target
    for chaser in chasers:
        dx = target_x - chaser['x']
        dy = target_y - chaser['y']
        dist = math.hypot(dx, dy)
        if dist != 0:
            chaser['x'] += chaser_speed * dx / dist
            chaser['y'] += chaser_speed * dy / dist

    # Drawing
    screen.fill(BLACK)

    # Draw main rectangle
    pygame.draw.rect(screen, RED, (target_x, target_y, target_width, target_height))

    # Draw chasers
    for chaser in chasers:
        pygame.draw.rect(screen, BLUE, (chaser['x'], chaser['y'], chaser_size, chaser_size))

    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
