import pygame
import js  # This is provided by Pygbag to interact with WebAssembly
import asyncio

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chess Game")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Async function to get the board state from the C code compiled to WASM
async def get_initial_board():
    # Wait for the WASM module to be initialized
    await js.Module.onRuntimeInitialized

    # Assuming initializeChessBoard and fillBoard are available via ccall
    board_ptr = js.Module.ccall("initializeChessBoard", "number", [], [])
    js.Module.ccall("fillBoard", None, ["number"], [board_ptr])

    # Call the outputBoard function from WASM to retrieve board state
    board_string = js.Module.ccall("outputBoard", "string", ["number"], [board_ptr])
    return board_string

# Async main function to run the game loop
async def main():
    # Get the board from WASM
    board_data = None
    while board_data is None:
        try:
            board_data = await get_initial_board()
        except Exception as e:
            print(f"Error fetching board: {e}")

    # Main game loop
    running = True
    while running:
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
        clock.tick(60)

    pygame.quit()

# Run the async main function
asyncio.run(main())
