from numpy import zeros, ndarray

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = zeros((6, 7))
    return board


def input_column(board: ndarray, turn: bool):
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


def drop_piece(board: ndarray, col: int, turn: bool):
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = 1 if turn else 2
            break

    return row


def check_win(board: ndarray, row: int, col: int, turn: bool):
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

    return False, None


board = create_board()

turn, game_over = True, False
winner = None

while not game_over:
    print(board)

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


if winner:
    print(f"Player {winner} wins!")
else:
    print("Tie game")
