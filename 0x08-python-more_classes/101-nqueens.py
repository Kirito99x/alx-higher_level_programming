#!/usr/bin/python3
def is_safe(board, row, col, n):
    """
    Check if placing a queen at the specified position is safe.

    Args:
        board (list): The chessboard represented as a 2D list.
        row (int): The row index to check.
        col (int): The column index to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
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
    """
    Get the coordinates of queens on the chessboard.

    Args:
        board (list): The chessboard represented as a 2D list.
        n (int): The size of the chessboard.

    Returns:
        list: A list of queen coordinates as tuples (row, column).
    """
    queen_coordinates = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queen_coordinates.append((i, j))
    return queen_coordinates

def solve_nqueens_util(board, col, n, solutions):
    """
    Recursively find and record solutions to the N-Queens problem.

    Args:
        board (list): The chessboard represented as a 2D list.
        col (int): The current column being considered.
        n (int): The size of the chessboard.
        solutions (list): A list to store the found solutions.
    """
    if col == n:
        solutions.append(print_queen_coordinates(board, n))
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0

def solve_nqueens(n):
    """
    Solve the N-Queens problem and return the solutions.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of solutions, where each solution is a list of queen coordinates.
    """
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
