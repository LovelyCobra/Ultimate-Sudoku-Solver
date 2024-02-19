import os
import sys
import time
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
	
def filling_singles(brd):
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
					counter += 1
					os.system('cls' if os.name == 'nt' else 'clear')
					print("Pre-filling with iteration:")
					pr.print_board(brd)
					print(f"Values found: {count + counter}")
					print(f"Round: {round + 1}")
					time.sleep(0.2)
			
def finding_hidden_singles(brd, r, c):
	vgs = valid_guesses(brd, r, c)
	vgs_row = [ ]
	vgs_column = []
	vgs_square = []
	
	for col in range(9):
		if col != c and brd[r][col] == 0:
			for val in valid_guesses(brd, r, col):
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
		for col in range(start_c, start_c + 3):
			if [row, col] != [r, c] and brd[row][col] == 0:
				for val in valid_guesses(brd, row, col):
					if val not in vgs_square:
						vgs_square.append(val)
				
	for n in vgs:
					if n not in vgs_row or n not in vgs_column or n not in vgs_square:
						return n
	
	return None
					
					
def filling_hidden_singles(brd):
	global counter
	global count
	global round
	for r in range(9):
		for c in range(9):
			temp = finding_hidden_singles(brd, r, c)
			if temp != None and brd[r][c] == 0:
				brd[r][c] = temp
				counter += 1
				os.system('cls' if os.name == 'nt' else 'clear')
				print("Pre-filling with iteration:")
				pr.print_board(brd)
				print(f"Values found: {count + counter}")
				print(f"Round: {round + 1}")
				time.sleep(0.2)

def pre_filling(brd):
	global counter
	global count
	global round
	count = 0
	round = 0
	filling_singles(brd)
	filling_hidden_singles(brd)
	count += counter
	round += 1
	
	while counter != 0:
		filling_singles(brd)
		filling_hidden_singles(brd)
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

def is_solvable(brd):
		global guess_count
		
		row, column = first_empty(brd)
		if row is None:
			return True
		
		for val in range(1, 10):
			if is_valid(brd, row, column, val):
				brd[row][column] = val
				guess_count += 1
					
				if is_solvable(brd):
					return True
				
			brd[row][column] = 0
		return False
				
     
		
if __name__ == '__main__':
    
    board = "060900000, 500000020, 000060000, 000500906, 807000000, 000000400, 000007083, 002040000, 090000000"
    board = board.split(", ")
    board = list(map(int, board))
    brd = list(map(digit9_separator, board))

    print("Initial Board:")
    pr.print_board(brd)
    time.sleep(3)
    
    
    
    print("Pre-filling with iteration:")
    holder = pre_filling(brd)
    
    row, column = first_empty(brd)
    if row is None:
    	print(f"\nFor this sudoku the iteration was all that was needed to solve it completly.\nAltogether {holder[0]} emty cells were filled during {holder[1] - 1} rounds of the two iterative methods.")
    	
    else:
    	print(f"\nIteration found {holder[0]} values during {holder[1] - 1} rounds.\n")
    	
    	print("\nSolving the rest of the sudoku by recursion:\n")
    	answer = is_solvable(brd)
    	if answer is True:
    	 	print("\nFinal Solution:")
    	 	pr.print_board(brd)
    	 	print(f"Number of guesses made: {guess_count}.\n")
    	else:
    	 	print(f"This particular sudoku doesn't have a solution.\nNumber of guesses made: {guess_count}.\n")		
			
#Boards:
	#Extreme:
		#"367000000, 000900500, 000000000, 000030087, 400500000, 090000000, 908000400, 000076000, 000002000"
		#"705000000, 000420000, 800000000, 500068000, 300000400, 000900600, 090600000, 000000057, 000000080"
		#"270000009, 000400600, 008000000, 000020010, 084000000, 506000000, 000600800, 300070000, 090000000"
	###"000000001, 000001000, 001000050, 000000003, 000200800, 203000000, 000102400, 060070002, 002008000"
		#"060200000, 000090070, 050000400, 800000030, 000504000, 000600000, 200000905, 007080000, 000000600"
		#"600009000, 080000500, 200300000, 050000408, 900600000, 000200700, 300000060, 000070000, 000040000"
		#"000000000, 000000825, 476000000, 600029007, 003000000, 000500096, 007003000, 008050900, 020000048"
		#"060900000, 500000020, 000060000, 000500906, 807000000, 000000400, 000007083, 002040000, 090000000" 15 minutes, 37 mil guesses
		
	#Expert:
		#"000000010, 060709000, 870450600, 000023704, 000905000, 609810000, 007092046, 000508020, 090000000"
		#"405000086, 080000090, 000040200, 061200704, 000407000, 807006930, 006080000, 020000070, 790000608"
		#"047300009, 050000104, 900005000, 000080602, 520000081, 706090000, 000800006, 805000010, 100009570"
		#"100000390, 000600000, 900008000, 000001000, 000000780, 307950600, 062800000, 050004000, 000007106" Iteration: 41 values, 7 rounds
		#"785000006, 000300058, 000080120, 020009003, 008000900, 600400010, 073020000, 150006000, 900000875" Iteration enough
		#"000100000, 590000046, 080700500, 000802000, 006000008, 000005600, 007000020, 639000000, 008004009" Iteration 22 values, 4 rounds
	    #"900007260, 060410000, 021000000, 090706000, 500104006, 000905020, 000000980, 000048030, 084600005" Iteration enough, 53 values, 5 rounds
	
	#Hard:
		#"052000010, 004026090, 186000003, 000907000, 069302184, 000018709, 008640907, 013270845, 090000000"
		#"000007008, 050064190, 340912000, 000091260, 064508000, 700600900, 605430871, 839006000, 001000009"

	#Medium:
		#"000803000, 357000000, 002910506, 509684002, 060001450, 840025697, 005069003, 108000700, 600500009"