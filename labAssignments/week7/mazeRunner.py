"""
File:   mazeRunner.py
Author: Sebastian Ševčík (s.sevcik@student.rug.nl)

Description:
    Reads a maze from input, one row per line, ending at an empty line. The
    maze contains walls, dots (".") and Pac-Man ("@"). Prints the maximum
    number of dots Pac-Man can eat in a single path, moving up, down, left or
    right and never visiting the same dot twice.
"""

def build_maze():
    maze = []
    while True:
        line = input()
        if line == "":
            break
        maze.append(list(line))
    return maze


def PacManStartLocation(maze):
    for xcoord, row in enumerate(maze):
        for ycoord, col in enumerate(row):
            if col == "@":
                return (xcoord, ycoord)
            

def longestRun(maze, pacLocation):
    best = 0
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for move in moves:
        newX, newY = pacLocation[0] + move[0], pacLocation[1] + move[1]
        if 0 <= newX < len(maze) and 0 <= newY < len(maze[newX]) and maze[newX][newY] == ".":
            newMaze = [row[:] for row in maze]
            newMaze[newX][newY] = " "
            best = max(best, 1 + longestRun(newMaze, (newX, newY)))
    return best


def main():
    maze = build_maze()
    coordinates = PacManStartLocation(maze)
    print(longestRun(maze, coordinates))


main()