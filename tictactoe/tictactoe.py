def create_board():
    """
    Creates an empty 3x3 game board.

    The function initializes a two-dimensional list with three rows and three columns, each element initialized with
    an empty space (' ').

    Args:
    None

    Returns:
    list: A two-dimensional list representing the empty game board.
    """

    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board


def print_board(board):
    """
    Displays the board on the screen.

    Parameters:
    board (list): A two-dimensional list that represents the board.

    Returns:
    None: The function does not return a value.
    """
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def make_move(board, row, col, player):
    """
    Places a player's mark on the specified board location.

    Args:
    board (list): A two-dimensional list representing the game board.
    row (int): The row index of the board location.
    col (int): The column index of the board location.
    player (str): The symbol representing the player making the move.

    Returns:
    bool: True if the move was successful, False otherwise.
   """
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print(f"Cell ({row + 1},{col + 1}) is already occupied. Please choose another cell.")
        return False


def is_board_full(board):
    """
    Checks if the game board is full.

    Args:
    board (list): A two-dimensional list representing the game board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    for row in board:
        if ' ' in row:
            return False
    return True


def check_winner(board):
    """
    Determines if there is a winner in the game.

    Args:
    board (list): A two-dimensional list representing the game board.

    Returns:
    str: The symbol of the winning player if a winner is found, None otherwise.
    """
    # Horizontal check
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]

    # Vertical check
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if column.count(column[0]) == 3 and column[0] != ' ':
            return column[0]

    # Diagonal check
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # If there is no winner
    return None


def main():
    """
    Runs the tic-tac-toe game.
    This function creates a game board, starts the game loop, and determines the winner.

    Args:
    None

    Returns:
    None
    """
    board = create_board()
    current_player = 'X'
    winner = None

    while not winner and not is_board_full(board):
        print_board(board)
        print("Player", current_player)
        valid_move = False

        while not valid_move:
            row = int(input("Enter the line number (1-3): "))
            col = int(input("Enter the column number (1-3): "))

            # Checking the correctness of the entered coordinates
            if 1 <= row <= 3 and 1 <= col <= 3:
                row -= 1
                col -= 1
                valid_move = make_move(board, row, col, current_player)
            else:
                print("Incorrect coordinates. Try again.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Winner:", winner)
        elif is_board_full(board):
            print_board(board)
            print("The game ended in a draw.")

        # Player change
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


if __name__ == '__main__':
    main()
