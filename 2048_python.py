import sys
import tty
import termios
from random import randint
from logic import *

GRID_LEN = 4

class GetCh:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class Game(LogicGame):
    def set_random_number(self, board):
        for i in range(2):
            guess_row = randint(0, len(board) - 1)
            guess_col = randint(0, len(board[0]) - 1)
            board[guess_col][guess_row] = "2"

    def move_set(self, board, move = ''):
        guess_row = len(board) - 1
        guess_col = len(board[0]) - 1
        for item, number_list in enumerate(board):
                if "2" in number_list:
                    print(board[item])
                    if board[item][-1] == "2":
                        if move == 'left':
                            board[item][0] = '1'
                        elif move == 'right':
                            board[item][-1] = '1'
                    else:
                        board[item][-1] = 'O'


class GameGrid(LogicGame):
    def __init__(self):
        super().__init__()
        self.init_matrix()
        self.update_grid_cells()
        self.new_number = 0

    def gen(self):
        return randint(0, GRID_LEN - 1)

    def init_matrix(self):
        self.matrix = self.new_game(GRID_LEN)

        self.matrix = self.add_two(self.matrix)
        self.matrix = self.add_two(self.matrix)

        # print(self.matrix)

    def update_grid_cells(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = self.matrix[i][j]

    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2




def get():
    inkey = GetCh()

    start_game = Game()

    gamegrid = GameGrid()

    print(gamegrid.new_number)

    # board = gamegrid.generate_next()

    # for row in gamegrid.matrix:
        # print("".join(str(row)))


    board = []

    for x in range(4):
        board.append(["X"] * 4)

    start_game.set_random_number(board)

    while(1):
        k=inkey()
        if k!='':break
    if k=='\x1b[A':
        print("up")
    elif k=='\x1b[B':
        print("down")
    elif k=='\x1b[C':
        print(start_game.right(gamegrid.matrix))
    elif k=='\x1b[D':
        # start_game.move_set(board, 'left')
        print(start_game.left(gamegrid.matrix))
        # print("left")
    elif k == '\x1bQ':
        exit()
    else:
        print("not an arrow key!")
        exit()

    for row in board:
        print(" ".join(row))

def main():
    for i in range(0,20):
        get()

if __name__=='__main__':
    main()

