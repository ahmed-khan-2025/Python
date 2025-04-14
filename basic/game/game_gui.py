import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Rectangle")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Rectangle setup
rect_width, rect_height = 60, 40
rect_x, rect_y = 100, 100
rect_speed_x, rect_speed_y = 3, 2  # Change these for faster/slower speed

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # Limit to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the rectangle
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Bounce off edges
    if rect_x <= 0 or rect_x + rect_width >= WIDTH:
        rect_speed_x *= -1
    if rect_y <= 0 or rect_y + rect_height >= HEIGHT:
        rect_speed_y *= -1

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
