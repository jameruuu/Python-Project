import pygame

def draw_board(screen, width, height):
    # Draw Tic Tac Toe board
    pygame.draw.line(screen, (255, 255, 255), (width // 3, 0), (width // 3, height), 5)
    pygame.draw.line(screen, (255, 255, 255), (2 * width // 3, 0), (2 * width // 3, height), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, height // 3), (width, height // 3), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, 2 * height // 3), (width, 2 * height // 3), 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]  # Winner in a row
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]  # Winner in a column

    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]  # Winner in the main diagonal

    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]  # Winner in the other diagonal

    return None  # No winner yet


def display_result(screen, result_text):
    pygame.init()
    result_screen = pygame.display.set_mode((400, 300))  # Increase the size for better visibility
    pygame.display.set_caption("Result")
    font = pygame.font.SysFont(None, 48)  # Increase the font size
    text = font.render(result_text, True, (255, 255, 255))

    # Create a background rectangle with a color
    background_rect = pygame.Rect(0, 0, 400, 300)
    pygame.draw.rect(result_screen, (0, 0, 0), background_rect)  # Background color: black

    # Position the text in the center of the screen
    text_rect = text.get_rect(center=(200, 150))

    result_screen.blit(text, text_rect)
    pygame.display.flip()

    # Run a loop to keep the result screen open for 2 seconds
    pygame.time.wait(2000)

    pygame.quit()

def is_board_full(board):
    # Check if the board is full (tie)
    for row in board:
        if '' in row:
            return False
    return True

def main(screen, width, height, font):
    run_game = True
    player_turn = 1  # 1 for Player 1, 2 for Player 2
    board = [['', '', ''], ['', '', ''], ['', '', '']]

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYUP:
                run_game = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # Get the position of the mouse click
                mouseX, mouseY = pygame.mouse.get_pos()

                # Determine the row and column based on the mouse position
                row = mouseY // (height // 3)
                col = mouseX // (width // 3)

                # Check if the clicked cell is empty
                if board[row][col] == '':
                    # Update the board and change player turn
                    if player_turn == 1:
                        board[row][col] = 'X'
                        player_turn = 2
                    else:
                        board[row][col] = 'O'
                        player_turn = 1

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw Tic Tac Toe board
        draw_board(screen, width, height)

        # Draw X and O on the board
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    text = font.render('X', True, (255, 255, 255))
                    screen.blit(text, (j * width // 3 + (width // 6 - text.get_width() // 2),
                                       i * height // 3 + (height // 6 - text.get_height() // 2)))
                elif board[i][j] == 'O':
                    text = font.render('O', True, (255, 255, 255))
                    screen.blit(text, (j * width // 3 + (width // 6 - text.get_width() // 2),
                                       i * height // 3 + (height // 6 - text.get_height() // 2)))

        # Check for a winner or tie
        winner = check_winner(board)
        if winner:
            display_result(screen, "X won!" if winner == 'X' else "O won!")
            return winner  # Return the winner
        elif is_board_full(board):
            display_result(screen, "Tie!")
            return None  # Return None for a tie

        # Update the display
        pygame.display.flip()

    pygame.quit()

# Add a new function to display the result on the main screen
def display_result(screen, result_text):
    pygame.init()
    result_screen = pygame.display.set_mode((400, 300))  # Increase the size for better visibility
    pygame.display.set_caption("Result")
    font = pygame.font.SysFont(None, 48)  # Increase the font size
    text = font.render(result_text, True, (255, 255, 255))

    # Create a background rectangle with a color
    background_rect = pygame.Rect(0, 0, 400, 300)
    pygame.draw.rect(result_screen, (0, 0, 0), background_rect)  # Background color: black

    # Position the text in the center of the screen
    text_rect = text.get_rect(center=(200, 150))

    result_screen.blit(text, text_rect)
    pygame.display.flip()

    # Run a loop to keep the result screen open for 2 seconds
    pygame.time.wait(2000)
