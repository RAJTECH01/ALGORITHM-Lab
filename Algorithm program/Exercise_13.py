def is_safe(board, row, col, n):
    # Check if there is any queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col, n):
    if col == n:
        # All queens have been placed successfully
        return True
    for row in range(n):
        if is_safe(board, row, col, n):
            # Place the queen in the current cell
            board[row][col] = 1
            # Recur to place the rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True
            # Backtrack and remove the queen from the current cell
            board[row][col] = 0
    return False

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def n_queens(n):
    # Initialize the board
    board = [[0 for j in range(n)] for i in range(n)]
    if not solve_n_queens(board, 0, n):
        print("Solution does not exist.")
        return False
    print("Solution:")
    print_board(board, n)
    return True

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    n_queens(n)
