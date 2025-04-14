import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move the Rectangle")

# Set up the rectangle's initial position
rect_width, rect_height = 50, 50
rect_x, rect_y = width // 2 - rect_width // 2, height // 2 - rect_height // 2
rect_color = (255, 0, 0)  # Red color

# Set the speed of the rectangle's movement
speed = 5

# Main game loop
running = True
while running:
    window.fill((0, 0, 0))  # Fill the window with black background
    
    # Check for events (like quitting the game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the keys pressed
    keys = pygame.key.get_pressed()
    
    # Move the rectangle based on arrow keys
    if keys[pygame.K_LEFT]:
        rect_x -= speed  # Move left
    if keys[pygame.K_RIGHT]:
        rect_x += speed  # Move right
    if keys[pygame.K_UP]:
        rect_y -= speed  # Move up
    if keys[pygame.K_DOWN]:
        rect_y += speed  # Move down

    # Ensure the rectangle stays within the window boundaries
    rect_x = max(0, min(rect_x, width - rect_width))
    rect_y = max(0, min(rect_y, height - rect_height))

    # Draw the rectangle on the window
    pygame.draw.rect(window, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
