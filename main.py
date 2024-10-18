import pygame
import js  # This is provided by Pygbag to interact with WebAssembly
import asyncio

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chess Game")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Call the C function outputBoard (already compiled to WASM)
def get_initial_board():
    # Assuming initializeChessBoard and fillBoard are available via ccall
    print("Calling initializeChessBoard and fillBoard...")
    board_ptr = js.Module.ccall("initializeChessBoard", "number", [], [])
    js.Module.ccall("fillBoard", None, ["number"], [board_ptr])

    # Call the outputBoard function from WASM to retrieve board state
    print("Calling outputBoard...")
    board_string = js.Module.ccall("outputBoard", "string", ["number"], [board_ptr])
    print(f"Board string retrieved: {board_string}")
    return board_string

async def main():
    running = True
    board_data = None

    # Wait before getting the board to make sure WASM is initialized
    await asyncio.sleep(1)  # Adding delay to allow WASM to be fully ready

    # Get the board from WASM
    while board_data is None:
        try:
            board_data = get_initial_board()
            print(f"Initial board data: {board_data}")
        except Exception as e:
            print(f"Error fetching board: {e}")

    # Main game loop
    while running:
        clock.tick(60)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Display the board string (if retrieved)
        if board_data:
            y = 50
            for line in board_data.split("\n"):
                text = font.render(line, True, (0, 0, 0))
                screen.blit(text, (50, y))
                y += 40

        # Update the display
        pygame.display.flip()

        # Let asyncio yield control to other tasks
        await asyncio.sleep(0)

    # Quit Pygame once the game loop ends
    pygame.quit()

# Start the asyncio event loop and run the game
asyncio.run(main())
