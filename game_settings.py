from random import *

class GameSettings:
    def __init__(self):
        self.done = False
        self.matrix = []

    def iteration_list(self, list_name):
        for row in list_name:
            print("".join(str(row)))

    def new_game(self, n):
        for i in range(n):
            self.matrix.append([0] * n)
        return self.matrix

    def add_two(self, mat):
        a=randint(0,len(mat)-1)
        b=randint(0,len(mat)-1)
        while(mat[a][b]!=0):
            a=randint(0,len(mat)-1)
            b=randint(0,len(mat)-1)
        mat[a][b]=2
        return mat

    def reverse(self, mat):
        new=[]
        for i in range(len(mat)):
            new.append([])
            for j in range(len(mat[0])):
                new[i].append(mat[i][len(mat[0])-j-1])
        return new

    def transpose(self, mat):
        new=[]
        for i in range(len(mat[0])):
            new.append([])
            for j in range(len(mat)):
                new[i].append(mat[j][i])
        return new

    def cover_up(self, mat):
        new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range(4):
            count=0
            for j in range(4):
                if mat[i][j]!=0:
                    new[i][count]=mat[i][j]
                    if j!=count:
                        self.done=True
                    count+=1
        return (new,self.done)

    def merge(self, mat):
        for i in range(4):
             for j in range(3):
                 if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                     mat[i][j]*=2
                     mat[i][j+1]=0
                     self.done=True
        return (mat,self.done)


    def up(self, game):
            print("up")
            # return matrix after shifting up
            game = self.transpose(game)
            game, self.done = self.cover_up(game)
            temp = self.merge(game)
            game=temp[0]
            self.done=self.done or temp[1]
            game = self.cover_up(game)[0]
            game = self.transpose(game)
            return game

    def down(self, game):
            print("down")
            game = self.reverse(self.transpose(game))
            game, self.done = self.cover_up(game)
            temp = self.merge(game)
            game=temp[0]
            self.done=self.done or temp[1]
            game = self.cover_up(game)[0]
            game = self.transpose(self.reverse(game))
            return game

    def left(self, game):
            print("left")
            # return matrix after shifting left
            game, self.done = self.cover_up(game)
            temp = self.merge(game)
            game = temp[0]
            self.done = self.done or temp[1]
            game = self.cover_up(game)[0]
            return game

    def right(self, game):
            print("right")
            # return matrix after shifting right
            game = self.reverse(game)
            game, self.done = self.cover_up(game)
            temp = self.merge(game)
            game = temp[0]
            self.done = self.done or temp[1]
            game = self.cover_up(game)[0]
            game = self.reverse(game)
            return game