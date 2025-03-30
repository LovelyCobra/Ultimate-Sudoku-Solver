import os, sys, time, itertools, copy
from print import *
from cobraprint import *

def digit9_separator(integer):
    container = []
    i = 1
    while i < 10:
        container.append(integer % 10)
        integer = int(integer/10)
        i += 1
    container.reverse()
    return container

def is_valid(brd, r, c, val):
	for i in range(9):
		if brd[r][i] == val:
			return False
		
	for j in range(9):
		if brd[j][c] == val:
			return False
			
	start_r = r // 3 * 3
	start_c = c//3 * 3
	
	for k in range(start_r, start_r + 3):
		for l in range(start_c, start_c + 3):
			if brd[k][l] == val:
				return False
	return True

def valid_guesses(brd, r, c):
	vlgs = [guess for guess in range(1, 10) if is_valid(brd, r, c, guess)]
	return vlgs
	
global counter
global count
global round
	
def filling_singles(brd, colm):
	global counter
	global count
	global round
	counter = 0
	for r in range(9):
		for c in range(9):
			if brd[r][c] == 0:
				vgs = valid_guesses(brd, r, c)
				if len(vgs) == 1:
					brd[r][c] = vgs[0]
					colm[r][c] = "\033[91m"
					counter += 1
					os.system('cls' if os.name == 'nt' else 'clear')
					print("Pre-filling with iteration:")
					print_board(brd, colm)
					print(f"Values found: \033[91m{count + counter}\033[0m")
					print(f"Round: \033[94m{round + 1}\033[0m")
					time.sleep(0.5)
			
def finding_hidden_singles(brd, r, c):
	vgs = valid_guesses(brd, r, c)
	vgs_row = [ ]
	vgs_column = []
	vgs_square = []
	
	for colm in range(9):
		if colm != c and brd[r][colm] == 0:
			for val in valid_guesses(brd, r, colm):
				if val not in vgs_row:
					vgs_row.append(val)
					
	for row in range(9):
		if row != r and brd[row][c] == 0:
			for val in valid_guesses(brd, row, c):
				if val not in vgs_column:
					vgs_column.append(val)
					
	start_r = r // 3 * 3
	start_c = c//3 * 3
	
	for row in range(start_r, start_r + 3):
		for colm in range(start_c, start_c + 3):
			if [row, colm] != [r, c] and brd[row][colm] == 0:
				for val in valid_guesses(brd, row, colm):
					if val not in vgs_square:
						vgs_square.append(val)
				
	for n in vgs:
					if n not in vgs_row or n not in vgs_column or n not in vgs_square:
						return n
	
	return None
					
					
def filling_hidden_singles(brd, colm):
	global counter
	global count
	global round
	for r in range(9):
		for c in range(9):
			temp = finding_hidden_singles(brd, r, c)
			if temp != None and brd[r][c] == 0:
				brd[r][c] = temp
				colm[r][c] = "\033[91m"
				counter += 1
				os.system('cls' if os.name == 'nt' else 'clear')
				print("Pre-filling with iteration:")
				print_board(brd, colm)
				print(f"Values found: \033[91m{count + counter}\033[0m")
				print(f"Round: \033[94m{round + 1}\033[0m")
				time.sleep(0.5)

def pre_filling(brd, colm):
	global counter
	global count
	global round
	count = 0
	round = 0
	color_matrix = []
	filling_singles(brd, colm)
	filling_hidden_singles(brd, colm)
	count += counter
	round += 1
	
	while counter != 0:
		filling_singles(brd, colm)
		filling_hidden_singles(brd, colm)
		count += counter
		round += 1
		
	return [count, round]
		
	
					
def first_empty(brd):
		for r in range(9):
			for c in range(9):
				if brd[r][c] == 0:
					return r, c
				
		return None, None
					
global guess_count
guess_count = 0

def is_solvable(brd, colm, shift=0):
		global guess_count
		
		row, column = first_empty(brd)
		if row is None:
			return True
		
		for val in range(1, 10):
			if is_valid(brd, row, column, val):
				brd[row][column] = val
				colm[row][column] = "\033[91m"
				guess_count += 1
					
				if is_solvable(brd, colm):
					return True
				
			brd[row][column] = 0
		return False

switch = True		
def show_spinner():
    spinner = itertools.cycle(['-', '\\', '|', '/'])  # Spinner characters
    while True:
        if switch:
            sys.stdout.write(f'\rSolving the rest of the sudoku by recursion: \033[91m{next(spinner)}\033[0m, Elapsed time: \033[92m{int(time.time() - start_time)}\033[0m seconds, Guesses made: \033[94m{guess_count}\033[0m') # \r returns the cursor to the beginning of the line
        else:
            sys.stdout.write(f'\rNow solving the sudoku by recursion only: \033[91m{next(spinner)}\033[0m, Elapsed time: \033[92m{int(time.time() - start_time)}\033[0m seconds, Guesses made: \033[94m{guess_count}\033[0m')
        sys.stdout.flush()  # Flush to ensure output is shown immediately
        time.sleep(0.05)  # Pause for a brief moment		
     
		
if __name__ == '__main__':
    import threading
    os.system('cls' if os.name == 'nt' else 'clear')
    
    board = input("\nInput the initial board as a string on nine nine-digit numbers separated by ', ':\n")
    with open("sudoku_container.txt", "a") as file:
        file.write(board)
        file.write("\n")
        
    start_time = time.time()
    board = board.split(", ")
    board = list(map(int, board))
    board_transformed = list(map(digit9_separator, board))
    brd_copy = copy.deepcopy(board_transformed)
    colors = [["" for elem in range(9)] for row in range(9)]
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Initial Board:")
    print_board(board_transformed, colors)
    time.sleep(3)
    
    print("Pre-filling with iteration:")
    holder = pre_filling(board_transformed, colors)
    
    with open("sudoku_container.txt", "a") as file:
        file.write(f"{holder[0]} values, {holder[1]-1} rounds, ")
        # file.write("\n")
    
    row, column = first_empty(board_transformed)
    if row is None:
        print(f"\nFor this sudoku the iteration was all that was needed to solve it completely.\nAltogether \033[91m{holder[0]}\033[0m empty cells were filled during \033[94m{holder[1]-1}\033[0m rounds of the two iterative methods.\n")
        with open("sudoku_container.txt", "a") as file:
            file.write(f"guesses 0\n")
    else:
        print(f"{cur_pos_abs(17, 1)}\nIteration found \033[92m{holder[0]}\033[0m values during \033[96m{holder[1]-1}\033[0m rounds.\n")
        
        spinner_thread = threading.Thread(target=show_spinner)
        spinner_thread.daemon = True
        spinner_thread.start()
        
        answer = is_solvable(board_transformed, colors)
        sys.stdout.write('\rTask completed!                                 \n')
        
        with open("sudoku_container.txt", "a") as file:
            file.write(f"guesses {guess_count}/")
        
        if answer is True:
            print(f"\n{cur_pos_abs(18, 1)}Final Solution:")
            print_board(board_transformed, colors)
            print(f"Number of guesses made: \033[94m{guess_count}\033[0m.\n")
        else:
            print(f"{cur_pos_abs(17, 1)}This particular sudoku doesn't have a solution.\nNumber of guesses made: \033[94m{guess_count}\033[0m.\n")
    
    start_time = time.time()
    guess_count = 0
    switch = False
    
    spinner_thread = threading.Thread(target=show_spinner)
    spinner_thread.daemon = True
    spinner_thread.start()
    is_solvable(brd_copy, colors, 33)
    sys.stdout.write(f'\rWhen solving the sudoku with recursion only, the number of guesses needed was: \033[94m{guess_count}\033[0m                                  \n')
    with open("sudoku_container.txt", "a") as file:
        file.write(f"{guess_count}\n")
 
