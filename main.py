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
    board_ptr = js.Module.ccall("initializeChessBoard", "number", [], [])
    js.Module.ccall("fillBoard", None, ["number"], [board_ptr])

    # Call the outputBoard function from WASM to retrieve board state
    board_string = js.Module.ccall("outputBoard", "string", ["number"], [board_ptr])
    return board_string

# Main game loop
running = True
board_data = None

# Get the board from WASM
while board_data is None:
    try:
        board_data = get_initial_board()
    except Exception as e:
        print(f"Error fetching board: {e}")

while running:
    clock.tick(60)

    asyncio.sleep(0)
    a
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


pygame.quit()

asyncio.run(main())
