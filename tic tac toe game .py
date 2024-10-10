# Simple Tic-Tac-Toe game in Python

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for _ in range(9):
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row and column (0-2, space-separated): ").split())

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move, try again.")
    
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
