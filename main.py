import sys 
import os
sys.path.append(os.path.abspath(r"D:\.olege\TicTacToe"))
from game import *

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def formatgrid(matrix, opt=None, cls=True):
    if cls:
        clear_screen()
    m = matrix
    print(f"{m[0]}|{m[1]}|{m[2]}    1 2 3")
    print("-----")
    print(f"{m[3]}|{m[4]}|{m[5]}    4 5 6")
    print("-----")
    print(f"{m[6]}|{m[7]}|{m[8]}    7 8 9")
    if opt != None:
        print(opt)

if __name__ == "__main__":
    board = TicTacToe()
    while True:
        formatgrid(board.matrix, cls=False)
        while board.status in ["X", "O"]:
            choice = int(input(board.status + "'s move: "))
            print(chk1 := board.place(choice))
            if (chk2 := board.check()) != "NO":
                print(chk2)
            formatgrid(board.matrix, chk1 + chk2)
        print("Resetting")
        board.reset()
	
