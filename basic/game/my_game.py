import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the rectangle
rect_x, rect_y = 100, 100
rect_width, rect_height = 50, 50
speed_x, speed_y = 5, 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the rectangle
    rect_x += speed_x
    rect_y += speed_y

    # Bounce the rectangle off the walls
    if rect_x <= 0 or rect_x + rect_width >= width:
        speed_x = -speed_x
    if rect_y <= 0 or rect_y + rect_height >= height:
        speed_y = -speed_y

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Set the frames per second (FPS)
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
