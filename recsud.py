from pprint import pprint
import time
import os
import sys
import print as pr

def digit9_separator(integer):
    container = []
    i = 1
    while i < 10:
        container.append(integer % 10)
        integer = int(integer/10)
        i += 1
    container.reverse()
    return container

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


def find_next_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None, None

def is_valid(puzzle, guess, row, col):

    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True
global c
c = 0

def solve_sudoku(puzzle):
    global c

    row, col = find_next_empty(puzzle)


    if row is None:
        return True


    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):

            puzzle[row][col] = guess
            c = c + 1
            if c % 100000 == 0:
            	os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            	print(c)
            	pprint(puzzle)




            if solve_sudoku(puzzle):
                return True


        puzzle[row][col] = 0


    return False

if __name__ == '__main__':
    example_board = "002015038, 900000000, 000000020, 000000000, 050267000, 780000004, 005390000, 009800600, 000000970"
    board = example_board.split(", ")
    board = list(map(int, board))
    brd = list(map(digit9_separator, board))
    pr.print_board(brd)
    time.sleep(3)

    #[
#        [6, 9, 7,  8, 1, 0,  2, 5, 0 ],
#        [0, 8, 2,  0, 5, 0,  9, 0, 0 ],
#        [5, 0, 3,  0, 2, 9,  0, 8, 6 ],

#        [0, 0, 4,  2, 0, 0,  0, 3, 5 ],
#        [0, 2, 0,  3, 0, 5,  0, 0, 0 ],
#        [3, 6, 5,  0, 0, 7,  8, 2, 0 ],

#        [2, 0, 0,  5, 0, 0,  0, 0, 1 ],
#        [0, 0, 9,  0, 0, 0,  5, 4, 2 ],
#        [0, 5, 0,  0, 7, 2,  3, 0, 8 ]
#    ]

    print(solve_sudoku(brd))

    pr.print_board(brd)
