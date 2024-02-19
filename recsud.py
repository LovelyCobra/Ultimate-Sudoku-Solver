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
            c += 1
            if c % 1 == 0:
            	os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            	print(c)
            	pr.print_board(brd)
            	time.sleep(0.1)                   	                       
            if solve_sudoku(puzzle):
                return True  
        
        puzzle[row][col] = 0
    
    return False

if __name__ == '__main__':
    example_board = "029804000, 001070000, 800001050, 050006039, 000705000, 190300060, 080900001, 000080700, 000507390"
    board = example_board.split(", ")
    board = list(map(int, board))
    brd = list(map(digit9_separator, board))
    pr.print_board(brd)
    time.sleep(3)
    
   # global c
    print(solve_sudoku(brd))
    
    pr.print_board(brd)
    print(f"Number of guesses: {c}")
    
    #000046000, 900000080, 000070000, 200000605, 050800000, 000000700, 097000000, 000500030, 406000000
    # 700000040, 000180000, 000000090, 050000208, 080000600, 000009000, 309700000, 000060500, 004000000
   # 060900000, 500000020, 000060000, 000500906, 807000000, 000000400, 000007083, 002040000, 090000000
   #002904506, 700000200, 000050090, 009100000, 000000680, 400009030, 076000000, 000200008, 100080000
   #Extreme:
   	#200064000, 000900700, 800050000, 090300000, 000000062, 000000084, 000700100, 000080000, 600000000
   #	367000000, 000900500, 000000000, 000030087, 400500000, 090000000, 908000400, 000076000, 000002000
   	#705000000, 000420000, 800000000, 500068000, 300000400, 000900600, 090600000, 000000057, 000000080
   	#060200000, 000090070, 050000400, 800000030, 000504000, 000600000, 200000905, 007080000, 000000600

	#Expert:
		#029804000, 001070000, 800001050, 050006039, 000705000, 190300060, 080900001, 000080700, 000507390
		#008006040, 500009700, 062000019, 000038000, 800901005, 000670000, 640000250, 009500006, 050800900
		#060800302, 000070060, 700900018, 005340000, 600000003, 000097800, 240003007, 070060000, 109002030
	#	000000010, 060709000, 870450600, 000023704, 000905000, 609810000, 007092046, 000508020, 090000000
		#405000086, 080000090, 000040200, 061200704, 000407000, 807006930, 006080000, 020000070, 790000608
