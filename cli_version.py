import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((6, 7))
    return board


def input_column(board, turn: bool):
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


def drop_piece(board, col: int, turn: bool):
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = 1 if turn else 2
            break

    return row


def check_win(board, row: int, col: int, turn: bool):
    win_play = 1 if turn else 2

    # Single Row (Left): C <= 3
    if col >= 3:
        pass

    # Single Row (Right): C >= 3
    if col <= 3:
        pass

    if row <= 2:
        # Single Column: R <= 2
        for i in range(1, 4):
            if board[row + i][col] != win_play:
                break
        else:
            return True, win_play

        # TL to BR: C <= 3 & R <= 2
        if col <= 3:
            pass

        # TR to BL: C >= 3 & R <= 2
        if col >= 3:
            pass
    else:
        # BL to TR: C <= 3 & R >= 3
        if col <= 3:
            pass

        # BR to TL: C >= 3 & R >= 3
        if col >= 3:
            pass

    return False, win_play


game_over = False
ct = 0
board = create_board()
turn = True

winner = None

while not game_over:
    column = input_column(board, turn)

    row = drop_piece(board, column, turn)

    game_over, winner = check_win(board, row, column, turn)

    turn = not turn

    print(board, row, column, game_over, winner)

    if ct == 10:
        game_over = True

    ct += 1

print(f"Player {winner} wins!")
