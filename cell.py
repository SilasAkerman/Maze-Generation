import pygame

class Cell:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size

        self.coords = [row, col]
        self.x = col*size
        self.y = row*size

        self.walls = [True, True, True, True] # top, rigth, bottom, left
        self.visited = False
        self.backtracked = False

    def display(self, win):
        if self.walls[0]:
            pygame.draw.line(win, (255, 255, 255), (self.x, self.y), (self.x+self.size, self.y))
        if self.walls[1]:
            pygame.draw.line(win, (255, 255, 255), (self.x+self.size, self.y), (self.x+self.size, self.y+self.size))
        if self.walls[2]:
            pygame.draw.line(win, (255, 255, 255), (self.x+self.size, self.y+self.size), (self.x, self.y+self.size))
        if self.walls[3]:
            pygame.draw.line(win, (255, 255, 255), (self.x, self.y+self.size), (self.x, self.y))

    def destroy_wall(self, wall_index):
        self.walls[wall_index] = False