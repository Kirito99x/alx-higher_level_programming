#!/usr/bin/python3
def is_safe(board, row, col, n):
    # Check if there is a queen in the same row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_queen_coordinates(board, n):
    queen_coordinates = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queen_coordinates.append([i, j])
    return queen_coordinates

def solve_nqueens_util(board, col, n, solutions):
    if col == n:
        solutions.append(print_queen_coordinates(board, n))
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        return []

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    result = solve_nqueens(N)

    if result:
        for solution in result:
            print(solution)
    else:
        print("No solution found.")
