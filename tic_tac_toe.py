def print_board(board):
    """Displays the current state of the 3x3 board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Define winning combinations (rows, columns, diagonals)
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tic_tac_toe():
    """Main game loop for Tic-Tac-Toe."""
    board = [str(i + 1) for i in range(9)]  # Initialize board with positions 1-9
    current_player = "X"
    moves_made = 0

    print("--- Welcome to Tic-Tac-Toe ---")
    print("Players will take turns choosing a position (1-9).")

    while moves_made < 9:
        print_board(board)
        try:
            choice = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            
            # Validate input
            if choice < 0 or choice > 8 or board[choice] in ["X", "O"]:
                print("Invalid move! Position already taken or out of range. Try again.")
                continue
            
            # Place the move
            board[choice] = current_player
            moves_made += 1

            # Check for a win
            if check_winner(board, current_player):
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                return

            # Switch players
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number between 1 and 9.")

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
