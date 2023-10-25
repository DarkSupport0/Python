import random

def enter_move(board):
    move = int(input("Введи клітину для ходу: "))
    while ((move < 1 or move > 9) or
    (board[int((move - 1) / 3)][int((move - 1) % 3)] == "O" or board[int((move - 1) / 3)][int((move - 1) % 3)] == "X")):
        if move < 1 or move > 9:
            print("Такої клітини не існує")
            move = int(input("Введи клітину для ходу: "))
        elif board[int((move - 1) / 3)][int((move - 1) % 3)] == "O" or board[int((move - 1) / 3)][
            int((move - 1) % 3)] == "X":
            print("Ця клітина зайнята")
            move = int(input("Введи клітину для ходу: "))
    board[int((move - 1) / 3)][int((move - 1) % 3)] = "O"

def bot_move(board):
    botmove = random.randrange(1, 10)
    while (board[int((botmove - 1) / 3)][int((botmove - 1) % 3)] == "O" or board[int((botmove - 1) / 3)][
        int((botmove - 1) % 3)] == "X"):
        botmove = random.randrange(1, 10)
    board[int((botmove - 1) / 3)][int((botmove - 1) % 3)] = "X"

def victory_for(board, game):
    if ((board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or
            (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O") or
            (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or
            (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or
            (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or
            (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or
            (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or
            (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O")):
        print("Гравець переміг")
        game = False
    if ((board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or
            (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") or
            (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or
            (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or
            (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or
            (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or
            (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or
            (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X")):
        print("Комп'ютер переміг")
        game = False
    return game

def draw_for(board, game):
    if ((type(board[0][0]) == str) and
            (type(board[0][1]) == str) and
            (type(board[0][2]) == str) and
            (type(board[1][0]) == str) and
            (type(board[1][1]) == str) and
            (type(board[1][2]) == str) and
            (type(board[2][0]) == str) and
            (type(board[2][1]) == str) and
            (type(board[2][2]) == str)):
        print("Нічия")
        game = False
    return game

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


game = True
board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
while game == True:
    display_board(board)
    enter_move(board)
    game = victory_for(board, game)
    if game == False:
        break
    bot_move(board)
    game = victory_for(board, game)
    if game == False:
        break
    game = draw_for(board, game)
display_board(board)
