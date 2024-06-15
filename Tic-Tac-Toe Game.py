def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def check_winner(board, player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False

def play_game():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already taken!")

play_game()