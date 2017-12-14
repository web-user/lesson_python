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
        self.new_number = []

    def init_matrix(self):
        self.matrix = self.new_game(GRID_LEN)
        self.matrix = self.add_two(self.matrix)
        self.matrix = self.add_two(self.matrix)

    def update_grid_cells(self, matrix_list):
        self.matrix = matrix_list
        self.matrix = self.add_two(self.matrix)
        return self.matrix

def get():
    inkey = GetCh()

    gamegrid = Game()

    while(1):
        key = inkey()
        if key != '' :break
    if key == '\x1b[A':
        gamegrid.iteration_list(gamegrid.update_grid_cells(gamegrid.up(gamegrid.matrix)))
        print("up")
    elif key == '\x1b[B':
        gamegrid.iteration_list(gamegrid.update_grid_cells(gamegrid.down(gamegrid.matrix)))
        print("down")
    elif key == '\x1b[C':
        gamegrid.iteration_list(gamegrid.update_grid_cells(gamegrid.right(gamegrid.matrix)))
    elif key == '\x1b[D':
        # start_game.move_set(board, 'left')
        gamegrid.iteration_list(gamegrid.update_grid_cells(gamegrid.left(gamegrid.matrix)))
        # print("left")
    else:
        print("not an arrow key!")
        exit()


def main():
    for i in range(0,20):
        get()

if __name__=='__main__':
    main()

