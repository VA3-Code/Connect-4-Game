from numpy import zeros, ndarray, ndenumerate
from numpy.random import random, randint
from colored import Back, Fore, Style
from os import system as terminal
from platform import system as platform
from msvcrt import kbhit, getch
from tqdm import tqdm
from time import sleep

ROW_COUNT = 6
COLUMN_COUNT = 7
SYMBOL = "\u2B24"

BLUE = Back.rgb(0, 85, 150)
HIGHLIGHT = Fore.rgb(60, 165, 195)
SUBHIGHLIGHT = Fore.rgb(65, 180, 135)
RED = Fore.rgb(255, 50, 50)
YELLOW = Fore.rgb(255, 200, 50)
BLACK = Fore.rgb(25, 25, 25)
GREY = Fore.rgb(75, 75, 75)
RESET = Style.reset

LSEP = f"{RESET}  {BLACK}{BLUE}+---+---+---+---+---+---+---+{RESET}"


def display_rules() -> None:
    clear_console()

    for _ in tqdm(range(100), desc="Loading Game"):
        sleep(min(random() / randint(25, 35), 0.035))

    clear_console()
    sleep(0.35)

    print(f"{HIGHLIGHT}The basic rules of the", f"{RED}Connect {YELLOW}Four{RESET}:\n")

    print(
        f"{RED}Connect {YELLOW}Four{RESET} is a {SUBHIGHLIGHT}two-player game{RESET}",
        f"where {SUBHIGHLIGHT}each player takes turns dropping",
        f"colored discs{RESET} into a vertical grid.",
    )

    print(
        f"The grid has {SUBHIGHLIGHT}seven columns and six rows{RESET},",
        f"and the discs fall to the {SUBHIGHLIGHT}lowest available space",
        f"in each column.{RESET}",
    )

    print(
        "The objective of the game is to be the first player to form a",
        f"{SUBHIGHLIGHT}horizontal, vertical, or diagonal line",
        f"of four discs of your own color.{RESET}",
    )

    print(
        f"{SUBHIGHLIGHT}The game ends{RESET} when either player",
        f"{SUBHIGHLIGHT}achieves this goal{RESET}, or when the",
        f"{SUBHIGHLIGHT}grid is full and no more moves are possible.{RESET}",
    )

    print(
        f"{YELLOW}If the grid is full and no one has four discs in a row,",
        f"the game is a tie.{RESET}",
    )

    print(
        f"\n{HIGHLIGHT}How to play this version of the game,",
        f"{RED}Connect {YELLOW}Four{RESET}:\n",
    )

    print(
        f"To {SUBHIGHLIGHT}change column{RESET} for dropping the piece use the",
        f"{HIGHLIGHT}Right and Left Arrow keys or the A and D keys.{RESET}",
    )

    print(
        f"Once you decide to {SUBHIGHLIGHT}drop the piece,",
        f"{HIGHLIGHT}press the enter key.{RESET}",
    )

    print(
        f"\n{RED}Read the rules carefully{SUBHIGHLIGHT},",
        f"once both the players are ready, {YELLOW}press enter or space",
        f"to continue playing the game...{RESET}",
    )

    while True:
        if kbhit() and (getch()[0] == 13 or getch()[0] == 32):
            sleep(0.15)
            break


def clear_console() -> None:
    if platform() == "Windows":
        terminal("cls")

    else:
        terminal("clear")


def display_input_row(board: ndarray, col: int, turn: bool) -> None:
    clear_console()

    print("    ", end="")
    for i in range(7):
        if i == col:
            if turn:
                print(f"{RED}{SYMBOL}{RESET}", end="   ")

            else:
                print(f"{YELLOW}{SYMBOL}{RESET}", end="   ")

        else:
            print(" ", end="   ")

    print(f"\n{GREY}--------------------------------{RESET}")

    display_board(board)


def input_column(board: ndarray, turn: bool) -> int:
    display_input_row(board, 3, turn)
    col = 3

    while True:
        if kbhit():
            key_stroke = getch()[0]

            if key_stroke in [65, 75, 97] and col > 0:
                col -= 1
                display_input_row(board, col, turn)

            elif key_stroke in [68, 77, 100] and col < 6:
                col += 1
                display_input_row(board, col, turn)

            elif key_stroke == 13 or key_stroke == 32:
                display_input_row(board, col, turn)

                if board[0][col] != 0:
                    print("\nColumn already filled, please select another column")
                    continue

                break

    return col


def drop_piece(board: ndarray, col: int, turn: bool) -> int:
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = 1 if turn else 2
            break

    return row


def check_win(board: ndarray, turn: bool) -> (bool, int):
    win_play = 1 if turn else 2

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (
                board[r][c]
                == board[r][c + 1]
                == board[r][c + 2]
                == board[r][c + 3]
                == win_play
            ):
                return True, win_play

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c]
                == board[r + 1][c]
                == board[r + 2][c]
                == board[r + 3][c]
                == win_play
            ):
                return True, win_play

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c]
                == board[r + 1][c + 1]
                == board[r + 2][c + 2]
                == board[r + 3][c + 3]
                == win_play
            ):
                return True, win_play

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (
                board[r][c]
                == board[r - 1][c + 1]
                == board[r - 2][c + 2]
                == board[r - 3][c + 3]
                == win_play
            ):
                return True, win_play

    return False, 0


def display_board(board: ndarray) -> None:
    print("   ", end=f"{GREY}")

    for i in range(1, 8):
        print(f" {i} ", end=" ")

    print(RESET)

    for idx, player in ndenumerate(board):
        r, c = idx

        if c == 0:
            print(LSEP)
            print(f"{GREY}{r + 1} {BLUE}{BLACK}|", end="")

        if player == 1:
            print(
                f"{BLUE}{RED} {SYMBOL} ",
                end=f"{BLACK}|{RESET}",
            )
        elif player == 2:
            print(
                f"{BLUE}{YELLOW} {SYMBOL} ",
                end=f"{BLACK}|{RESET}",
            )
        else:
            print(f"{BLUE}{BLACK} {SYMBOL} ", end=f"|{RESET}")

        if c == 6:
            print()

    print(LSEP)


board = zeros((6, 7), dtype=int)

turn, game_over = True, False
winner = 0

display_rules()

while not game_over:
    for num in board[0]:
        if num == 0:
            break
    else:
        game_over = True
        break

    column = input_column(board, turn)

    row = drop_piece(board, column, turn)

    game_over, winner = check_win(board, turn)

    turn = not turn

clear_console()

display_board(board)

print("\n")

if winner != 0:
    print(f"Player {winner} wins!")
else:
    print("Tie game")

print("\nPress escape to exit...")

while True:
    if kbhit() and getch()[0] in [13, 27, 32]:
        sleep(0.15)
        break
