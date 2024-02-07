#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def initialize_board(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    board = [[' '] * n for _ in range(n)]
    return board


def copy_board(board):
    """Return a deepcopy of a chessboard."""
    return [row[:] for row in board]


def get_queen_positions(board):
    """Return the list of lists representation of a solved chessboard."""
    return ([[r, c] for r in range(len(board)) for c in range(len(board))
            if board[r][c] == "Q"])


def mark_attacked_positions(board, row, col):
    """Mark positions on the board attacked by a queen."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_n_queens(board, row, placed_queens, all_solutions):
    """Recursively solve an N-queens puzzle."""
    if placed_queens == len(board):
        all_solutions.append(get_queen_positions(board))
        return all_solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = copy_board(board)
            temp_board[row][c] = "Q"
            mark_attacked_positions(temp_board, row, c)
            all_solutions = solve_n_queens(temp_board, row + 1,
                                           placed_queens + 1, all_solutions)

    return all_solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_board(int(sys.argv[1]))
    solutions = solve_n_queens(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
