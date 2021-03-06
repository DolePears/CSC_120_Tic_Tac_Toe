# Dawson Pridgen
# 11/21/21
# CSC-120-Tic-Tac-Toe lab


board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def main():
    print_board()

    game_on = True

    while game_on:

        print("It is player 1's turn.")

        while not place_mark(1, input("What row would you like to place a mark at"), input(
                "What column would you like to place a mark at")):

            if place_mark(1, input("What row would you like to place a mark at"), input(
                    "What column would you like to place a mark at")):
                break

        print_board()

        if check_win(1):
            break

        if check_draw():
            print("The game has ended in a draw!")
            break

        print("It is player 2's turn.")

        while not place_mark(2, input("What row would you like to place a mark at"), input(
                "What column would you like to place a mark at")):

            if place_mark(2, input("What row would you like to place a mark at"), input(
                    "What column would you like to place a mark at")):
                break

        print_board()

        if check_win(2):
            break

    # This is for unit testing

    # print_board()
    # check_mark(1, 1)
    # if check_mark(1, 1):
    # print("True")
    # place_mark(1, 1, 1)
    # print_board()
    # place_mark(2, 1, 2)
    # print_board()
    # place_mark(1, 1, 1)
    # print_board()
    # place_mark(1, 0, 1)
    # print_board()
    # place_mark(1, 2, 1)
    # print_board()
    # check_win(1)
    # check_win(2)


def print_board():
    for row in board:
        print(row)
    print()


def check_mark(row, col):
    try:
        if row == -1 or col == -1:
            return False
        elif board[int(row)][int(col)] == '-':
            return True
        else:
            return False
    except IndexError:
        return False


def place_mark(player_id, row, col):
    row = int(row) - 1
    col = int(col) - 1
    if player_id == 1:
        if check_mark(int(row), int(col)):
            board[int(row)][int(col)] = "X"
            return True
        elif not check_mark(int(row), int(col)):
            print("That space is not available")
            return False

    elif player_id == 2:
        if check_mark(int(row), int(col)):
            board[int(row)][int(col)] = "O"
            return True
        elif not check_mark(int(row), int(col)):
            print("That space is not available")
            return False


def check_win(player_id):
    if player_id == 1:
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
            print("Player 1 wins!")
            return True
        elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
            print("Player 1 wins!")
            return True
        elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            print("Player 1 wins!")
            return True
        elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
            print("Player 1 wins!")
            return True
        elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
            print("Player 1 wins!")
            return True
        elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
            print("Player 1 wins!")
            return True
        elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            print("Player 1 wins!")
            return True
        elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            print("Player 1 wins!")
            return True
        else:
            return False

    if player_id == 2:
        if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
            print("Player 2 wins!")
            return True
        elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
            print("Player 2 wins!")
            return True
        elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
            print("Player 2 wins!")
            return True
        elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
            print("Player 2 wins!")
            return True
        elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
            print("Player 2 wins!")
            return True
        elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
            print("Player 2 wins!")
            return True
        elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            print("Player 2 wins!")
            return True
        elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
            print("Player 2 wins!")
            return True
        else:
            return False

def check_draw():
    if '-' in board[0] or '-' in board[1] or '-' in board[2]:
        return False

    else:
        return True


main()
