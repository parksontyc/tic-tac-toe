# 井字遊戲
"""
1.井字版
2.使用者輸入數字1~9來代表位置, 另外注意, 如果位置已經有了輸入，要求使用者重新輸入。
3.確認贏家。水平垂直及對角線,如果符號相同，就贏。
"""

# 創建井字版

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

print_board(board)

def quit(user_input):
    if user_input.lower() == "q":
        print("Thanks for playing ! ")
        return True
    else:
        return False

def check_input(user_input):
    # ckeck if its a number
    if not isnum(user_input):
        print("This is not a valid number !")
        return False
    user_input = int(user_input)
    if not bounds(user_input):
        return False
    return True

    #check if its  1-9

def isnum(user_input):
    if not user_input.isnumeric():
        return False
    else:
        return True

def bounds(user_input):
    if user_input > 9 or user_input < 1 :
        print("this is number is out of bounds !")
        return False
    else:
        return True

while True:
    user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit :")
    if quit(user_input) :
        break
    if not check_input(user_input):
        print("Please try again !")
        continue