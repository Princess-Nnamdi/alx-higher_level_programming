#!/usr/bin/python3
"""Solves the N-queens puzzle.

This script determines all possible solutions
for placing N non-attacking queens on an NxN chessboard.

Usage:
    $ ./nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty cells."""
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(' ')
        board.append(row)
    return board


def board_deepcopy(board):
    """Create a deep copy of a chessboard.

    Args:
        board (list): The chessboard to be copied.

    Returns:
        list: A new chessboard representing the deep copy.
    """
    return [row[:] for row in board]


def get_solution(board):
    """Return the list of queens' coordinates from a solved chessboard.

    Args:
        board (list): The solved chessboard.

    Returns:
        list: A list of lists containing the coordinates of queens.
    """
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_unavailable_cells(board, row, col):
    """Mark spots on the chessboard where non-attacking queens can't be placed.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    # Mark all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark all backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    # Mark all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve the N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.

    Returns:
        list: A list of lists representing solutions.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            mark_unavailable_cells(tmp_board, row, c)
            solutions = recursive_solve(tmp_board,
                                        row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
