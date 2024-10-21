import pygame
import js  # This is provided by Pygbag to interact with JavaScript
import asyncio

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chess Game1")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Call the JavaScript function getInitialBoard
def get_initial_board():
    board_data = js.getInitialBoard()
    return board_data

async def main():
    running = True
    board_data = None

    # Get the board from JavaScript
    while board_data is None:
        try:
            board_data = get_initial_board()
        except Exception as e:
            print(f"Error fetching board: {e}")
            await asyncio.sleep(0.1)

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # Display the board string (if retrieved)
        if board_data:
            y = 50
            for line in board_data.split("\n"):
                text = font.render(line, True, (0, 0, 0))
                screen.blit(text, (50, y))
                y += 40

        pygame.display.flip()

# Run the main coroutine
asyncio.run(main())

pygame.quit()
