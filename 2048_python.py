import sys
import tty
import termios
from random import randint
from game_settings import *


GRID_LEN = 4

class GetCh:
    def __init__(self):
        self.key = ''

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def set_key(self):
        while 1:
            self.key = self.get_key()
            if self.key != '' :break
        return self.key


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

def main():
    inkey = GetCh()
    gamegrid = Game()

    while True:
        item_key = inkey.set_key()
        if item_key == '\x1b[A':
            gamegrid.iteration_list(gamegrid.update_grid_cells(gamegrid.up(gamegrid.matrix)))
            print("up")
        elif item_key == '\x1b[B':
            gamegrid.iteration_list(gamegrid.update_grid_cells(gamegrid.down(gamegrid.matrix)))
            print("down")
        elif item_key == '\x1b[C':
            gamegrid.iteration_list(gamegrid.update_grid_cells(gamegrid.right(gamegrid.matrix)))
        elif item_key == '\x1b[D':
            # start_game.move_set(board, 'left')
            gamegrid.iteration_list(gamegrid.update_grid_cells(gamegrid.left(gamegrid.matrix)))
            # print("left")
        else:
            print("not an arrow key!")
            exit()

if __name__=='__main__':
    main()

