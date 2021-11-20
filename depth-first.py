import pygame
import sys
from cell import Cell
import random

DISPLAY = pygame.display.set_mode((1400, 800))
SPACING = 5

ROWS = DISPLAY.get_height()//SPACING
COLS = DISPLAY.get_width()//SPACING

FPS = 0

def display():
    DISPLAY.fill((0, 0, 0))

    # s = pygame.Surface((SPACING, SPACING))
    # s.set_alpha(200)

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col].backtracked:
                # s.fill((100, 100, 200))
                # DISPLAY.blit(s, (col*SPACING, row*SPACING))
                pygame.draw.rect(DISPLAY, (100, 100, 200), (col*SPACING, row*SPACING, SPACING, SPACING))
            elif grid[row][col].visited:
                # s.fill((200, 100, 200))
                # DISPLAY.blit(s, (col*SPACING, row*SPACING))
                pygame.draw.rect(DISPLAY, (200, 100, 200), (col*SPACING, row*SPACING, SPACING, SPACING))
            grid[row][col].display(DISPLAY)

    # s.fill((100, 200, 100))
    # DISPLAY.blit(s, (current_coords[1]*SPACING, current_coords[0]*SPACING))
    pygame.draw.rect(DISPLAY, (100, 200, 100), (current_coords[1]*SPACING, current_coords[0]*SPACING, SPACING, SPACING))

    pygame.display.update()

def update():
    global grid, current_coords
    if len(stack) > 0:
        current_coords = stack.pop()
        grid[current_coords[0]][current_coords[1]].backtracked = True
        next_coords = get_next_neighbour(current_coords[0], current_coords[1])
        if next_coords:
            stack.append(current_coords)
            grid[current_coords[0]][current_coords[1]].backtracked = False
            destroy_wall_between(current_coords, next_coords)
            current_coords = next_coords
            grid[current_coords[0]][current_coords[1]].visited = True
            stack.append(current_coords)

def destroy_wall_between(current_coords, next_coords):
    if current_coords[1] > next_coords[1]:
        current_wall_index = 3
    elif current_coords[1] < next_coords[1]:
        current_wall_index = 1
    elif current_coords[0] > next_coords[0]:
        current_wall_index = 0
    elif current_coords[0] < next_coords[0]:
        current_wall_index = 2
    grid[current_coords[0]][current_coords[1]].destroy_wall(current_wall_index)
    grid[next_coords[0]][next_coords[1]].destroy_wall((current_wall_index+2) % 4)

def get_next_neighbour(row, col):
    potential_neighbours = ((row+1, col), (row-1, col), (row, col+1), (row, col-1))
    neighbours = []
    for potential in potential_neighbours:
        if not (potential[0] < 0 or potential[0] >= ROWS or potential[1] < 0 or potential[1] >= COLS or grid[potential[0]][potential[1]].visited):
            neighbours.append(potential)
    if len(neighbours) > 0:
        return random.choice(neighbours)

def main():
    global current_coords, stack, grid
    grid = [[Cell(i, j, SPACING) for j in range(COLS)] for i in range(ROWS)]
    stack = []

    Clock = pygame.time.Clock()

    current_coords = [0, 0]
    grid[current_coords[0]][current_coords[1]].visited = True
    stack.append(current_coords)

    while True:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    main()
        update()
        display()



if __name__ == "__main__":
    main()