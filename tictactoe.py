board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    display_board()
    while(game_still_going):
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won the game ")
    else:
        print("It's a tie !!!")

def handle_turn(player):
    print(player + "'s turn")
    pos = input("Choose a position from 0-9: ")

    valid = False
    while not valid:
        while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pos = input("Choose a position from 0-9: ")

        pos = int(pos) - 1

        if board[pos] == "-":
            valid = True
        else:
            print("You can't got there. Go again")

    board[pos] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner

    row_winner = check_rows()
    cloumn_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif cloumn_winner:
        winner = cloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_going = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None

def check_columns():
    global game_still_going

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        game_still_going = False

    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    else:
        return None

def check_diagonals():
    global game_still_going

    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"

    if dia1 or dia2:
        game_still_going = False

    if dia1:
        return board[0]
    elif dia2:
        return board[2]
    else:
        return None


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"



play_game()