import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Set a title for the window
pygame.display.set_caption("Blue Screen")

# Define a color (RGB) for blue
blue = (0, 0, 255)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with blue
    screen.fill(blue)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
