import pygame
import numpy as np
import pygame.display
import sys
import math

from numpy import zeros, ndarray
from pygame import init, quit, QUIT
from pygame.display import update, set_mode, set_caption, set_icon
from pygame.event import get
from pygame.draw import rect, circle

BLUE = (0, 112, 255)
BLACK = (0, 0, 0)
RED = (237, 27, 36)
YELLOW = (255, 216, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE / 2 - 5)

SCREEN_WIDTH = COLUMN_COUNT * SQUARE_SIZE
SCREEN_HEIGHT = (ROW_COUNT - 1) * SQUARE_SIZE
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


def create_board() -> ndarray:
    board = zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board: ndarray, col: int, turn: bool) -> int:
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = 1 if turn else 2
            break

    return row


def input_column(board: ndarray, turn: bool) -> int:
    while True:
        col = int(
            input(f"Player {1 if turn else 2}: Enter the column between 1 and 7: ")
        )

        if col < 1 or col > 7:
            print("Invalid column!")
            continue

        col -= 1

        if board[0][col] != 0:
            print("Column already filled, please select another column")
            continue

        return col


def check_win(board: ndarray, row: int, col: int, turn: bool) -> (bool, int):
    win_play = 1 if turn else 2

    # Single Row (Right): C >= 3
    if col >= COLUMN_COUNT // 2:
        for i in range(1, 4):
            if board[row][col - i] != win_play:
                break
        else:
            return True, win_play

    # Single Row (Left): C <= 3
    if col <= COLUMN_COUNT // 2:
        for i in range(1, 4):
            if board[row][col + i] != win_play:
                break
        else:
            return True, win_play

    if row < ROW_COUNT // 2:
        # Single Column: R <= 2
        for i in range(1, 4):
            if board[row + i][col] != win_play:
                break
        else:
            return True, win_play

        # TL to BR: C <= 3 & R <= 2
        if col <= COLUMN_COUNT // 2:
            for i in range(1, 4):
                if board[row + i][col + i] != win_play:
                    break
            else:
                return True, win_play

        # TR to BL: C >= 3 & R <= 2
        if col >= COLUMN_COUNT // 2:
            for i in range(1, 4):
                if board[row + i][col - i] != win_play:
                    break
            else:
                return True, win_play
    else:
        # BL to TR: C <= 3 & R >= 3
        if col <= COLUMN_COUNT // 2:
            for i in range(1, 4):
                if board[row - i][col + i] != win_play:
                    break
            else:
                return True, win_play

        # BR to TL: C >= 3 & R >= 3
        if col >= COLUMN_COUNT // 2:
            for i in range(1, 4):
                if board[row - i][col - i] != win_play:
                    break
            else:
                return True, win_play

    return False, 0


board = create_board()

turn, game_over = True, False
winner = 0

# Game Loop
while not game_over:
    for evnt in get():
        if evnt.type == QUIT:
            running = False

    for num in board[0]:
        if num == 0:
            break
    else:
        game_over = True
        break

    column = input_column(board, turn)

    row = drop_piece(board, column, turn)

    game_over, winner = check_win(board, row, column, turn)

    turn = not turn
