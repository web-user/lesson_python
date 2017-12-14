import sys
import tty
import termios
from random import randint
from game_settings import *

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


class Game(GameSettings):
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


def get():
    inkey = GetCh()

    # start_game = Game()

    gamegrid = Game()

    print(gamegrid.new_number)

    # board = gamegrid.generate_next()

    # for row in gamegrid.matrix:
        # print("".join(str(row)))


    # board = []

    # for x in range(4):
    #     board.append(["X"] * 4)

    # start_game.set_random_number(board)

    while(1):
        key = inkey()
        if key != '' :break
    if key == '\x1b[A':
        gamegrid.iteration_list(gamegrid.up(gamegrid.matrix))
        print("up")
    elif key == '\x1b[B':
        gamegrid.iteration_list(gamegrid.down(gamegrid.matrix))
        print("down")
    elif key == '\x1b[C':
        gamegrid.iteration_list(gamegrid.right(gamegrid.matrix))
    elif key == '\x1b[D':
        # start_game.move_set(board, 'left')
        gamegrid.iteration_list(gamegrid.left(gamegrid.matrix))
        # print("left")
    else:
        print("not an arrow key!")
        exit()

    # for row in board:
    #     print(" ".join(row))

def main():
    for i in range(0,20):
        get()

if __name__=='__main__':
    main()

