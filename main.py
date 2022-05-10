# 井字遊戲
"""
1.井字版
2.使用者輸入數字1~9來代表位置, 另外注意, 如果位置已經有了輸入，要求使用者重新輸入。
3.確認贏家。水平垂直及對角線,如果符號相同，就贏。
"""

# 創建井字版

from itertools import count
from re import T


board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],



]

def print_board(board):
    for row in board:
        for slot in row:
            print(f'{slot}  ', end='')
        print()                        #換行用

user = True

def quit(user_input):  # 離開遊戲
    if user_input.lower() == "q":
        print("Thanks for playing ! ")
        return True
    else:
        return False

def check_input(user_input):  # 確認使用者輸入資訊是否為數字或是否超過1~9
    # ckeck if its a number
    if not isnum(user_input):
        print("This is not a valid number !")
        return False
    user_input = int(user_input)
    #check if its  1-9
    if not bounds(user_input):
        return False
    return True

def isnum(user_input):  # 確認輸入是否為數字
    if not user_input.isnumeric():
        return False
    else:
        return True

def bounds(user_input): # 確認輸入是否超過1~9這個範圍
    if user_input > 9 or user_input < 1 :
        print("this is number is out of bounds !")
        return False
    else:
        return True

def coordinates(user_input): # 將使用輸入的數字，轉化為board的座標
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(user_input % 3)
    return (row, col)

def istaken(coords, board): # 確認位置是否已有值
    row = coords[0]
    col = coords[1]
    if board[row][col] != "_":
        print("this position is already taken.")
        return True
    else:
        return False

def add_to_board(coords, board, active_user): # 將xo放入清單中
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user): # ox交換
    if user:
        return "x"
    else:
        return "o"


def iswin(user, board):
    if check_row(user, board): 
        return True
    if check_col(user, board):
        return True
    return False

def check_row(user, board):
    for row in  board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False



while True:
    active_user = current_user(user)
    print_board(board)
    user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit :")
    if quit(user_input) :
        break
    if not check_input(user_input):
        print("Please try again !")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again !")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f'{active_user.upper()} won !' )
        print_board(board)
        break
    user = not user
    