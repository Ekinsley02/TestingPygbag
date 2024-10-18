import pygame
import sys
import asyncio

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Set a title for the window
pygame.display.set_caption("Red Screen")

# Define a color (RGB) for blue
blue = (255, 0, 0)

async def main():
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

        # Use asyncio sleep to allow other tasks to run
        await asyncio.sleep(0)  # Yield control to the event loop

    pygame.quit()
    sys.exit()

# Run the asyncio event loop
asyncio.run(main())
