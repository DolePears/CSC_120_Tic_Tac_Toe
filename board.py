# Dawson Pridgen
# 11/21/21
# CSC-120-Tic-Tac-Toe lab


board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def main():
    print_board()
    check_mark(1, 1)
    if check_mark(1, 1):
        print("True")
    place_mark(1, 1, 1)
    print_board()
    place_mark(2, 1, 2)
    print_board()
    place_mark(1, 1, 1)
    print_board()
    place_mark(1, 0, 1)
    print_board()
    place_mark(1, 2, 1)
    print_board()
    check_win(1)
    check_win(2)


def print_board():
    for row in board:
        print(row)
    print()


def check_mark(row, col):
    if board[row][col] == '-':
        return True
    else:
        return False


def place_mark(player_id, row, col):
    if player_id == 1:
        if check_mark(row, col):
            board[row][col] = "X"

        elif not check_mark(row, col):
            print("That space is not available")

    elif player_id == 2:
        if check_mark(row, col):
            board[row][col] = "O"

        elif not check_mark(row, col):
            print("That space is not available")


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

main()
