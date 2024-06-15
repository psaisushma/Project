def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    empty_cell = find_empty_location(board)
    if not empty_cell:
        return True  # No empty cell means the board is solved
    row, col = empty_cell
     
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Undo the current cell for backtracking
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num!= 0 else '.' for num in row))

def get_sudoku_board_from_user():
    board = []
    for i in range(9):
        row = input(f"Enter row {i + 1} of the Sudoku puzzle (separated by spaces): ")
        row = list(map(int, row.split()))
        board.append(row)
    return board

def main():
    print("Welcome to the Sudoku Solver!")
    print("Please enter the Sudoku puzzle row by row, separated by spaces.")
    print("Use 0 to represent empty cells.")
    board = get_sudoku_board_from_user()
    if solve_sudoku(board):
        print("Sudoku puzzle solved successfully:")
        print_board(board)
    else:
        print("No solution exists for the Sudoku puzzle.")

if __name__ == "__main__":
    main()