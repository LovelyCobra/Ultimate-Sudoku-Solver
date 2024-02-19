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
	return [guess for guess in range(1, 10) if is_valid(brd, r, c, guess)]


global counter

def filling_singles(brd):
	global counter
	counter = 0
	for r in range(9):
		for c in range(9):
			if brd[r][c] == 0:
				vgs = valid_guesses(brd, r, c)
				if len(vgs) == 1:
					brd[r][c] = vgs[0]
					counter += 1
					print (f"Cell [{r}, {c}] filled with SINGLE ...{vgs[0]}. Guess no. {counter}.")
#					os.system('cls' if os.name == 'nt' else 'clear')
#					print("Pre-filling with iteration:")
#					pr.print_board(brd)
#					time.sleep(0.2)

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
			if row != r and col != c and brd[row][col] == 0:
				for val in valid_guesses(brd, row, col):
					if val not in vgs_square:
						vgs_square.append(val)
	if r == 0 and c == 5:
				print(f"Valid guesses for:\nRow: {vgs_row}\nColumn: {vgs_column}\nSquare: {vgs_square}\nValid guesses for the cell [0, 3]: {valid_guesses(brd, 0, 3)}")

	absentees = []
	for n in vgs:
					if n not in vgs_row or n not in vgs_column or n not in vgs_square:
						absentees.append(n)
	if len(absentees) == 1:
		return absentees[0]
	return None


def filling_hidden_singles(brd):
	global counter

	for r in range(9):
		for c in range(9):
			if finding_hidden_singles(brd, r, c) != None and brd[r][c] == 0:
				brd[r][c] = finding_hidden_singles(brd, r, c)
				counter += 1
				print (f"Cell [{r}, {c}] filled with HID-SIN ...{brd[r][c]}. Guess no. {counter}.")
#				os.system('cls' if os.name == 'nt' else 'clear')
#				print("Pre-filling with iteration:")
#				pr.print_board(brd)
#				time.sleep(0.2)

def pre_filling(brd):
	global counter
	count = 0
	round = 0
	print(f"Round {round + 1}:\n")
	filling_singles(brd)
	filling_hidden_singles(brd)
	count += counter
	round += 1

	while counter != 0 and round < 10:
		print(f"Round {round + 1}:\n")
		filling_singles(brd)
		filling_hidden_singles(brd)
		count += counter
		round += 1

	return [count, round]


if __name__ == '__main__':

    board = "785000006, 000300058, 000080120, 020009003, 008000900, 600400010, 073020000, 150006000, 900000875"
    board = board.split(", ")
    board = list(map(int, board))
    brd = list(map(digit9_separator, board))

    print("Initial Board:")
    pr.print_board(brd)
    time.sleep(3)



    print("Pre-filling with iteration:")
    holder = pre_filling(brd)
    print(f"\nIteration found {holder[0]} values during {holder[1] - 1} rounds.\n")
    pr.print_board(brd)

    #row, column = first_empty(brd)
#    if row is None:
#    	print(f"\nFor this sudoku the iteration was all that was needed to solve it completly.\nAltogether {holder[0]} emty cells were filled during {holder[1] - 1} rounds of the two iterative methods.")
#
#    else:
#    	print(f"\nIteration found {holder[0]} values during {holder[1] - 1} rounds.\n")
#
#    	print("\nSolving the rest of the sudoku by recursion:\n")
#    	answer = is_solvable(brd)
#    	if answer is True:
#    	 	print("\nFinal Solution:")
#    	 	pr.print_board(brd)
#    	 	print(f"Number of guesses made: {guess_count}.\n")
#    	else:
#    	 	print(f"This particular sudoku doesn't have a solution.\nNumber of guesses made: {guess_count}.\n")

#Boards:
	#Extreme:
		#"600009000, 080000500, 200300000, 050000408, 900600000, 000200700, 300000060, 000070000, 000040000"
		#"000000000, 000000825, 476000000, 600029007, 003000000, 000500096, 007003000, 008050900, 020000048"
		#"060900000, 500000020, 000060000, 000500906, 807000000, 000000400, 000007083, 002040000, 090000000" 15 minutes, 37 mil guesses

	#Expert:
		#"100000390, 000600000, 900008000, 000001000, 000000780, 307950600, 062800000, 050004000, 000007106"
		#"785000006, 000300058, 000080120, 020009003, 008000900, 600400010, 073020000, 150006000, 900000875" ???
		#"000100000, 590000046, 080700500, 000802000, 006000008, 000005600, 007000020, 639000000, 008004009"

	#Hard:
		#"052000010, 004026090, 186000003, 000907000, 069302184, 000018709, 008640907, 013270845, 090000000"
		#"000007008, 050064190, 340912000, 000091260, 064508000, 700600900, 605430871, 839006000, 001000009"

	#Medium:
		#"000803000, 357000000, 002910506, 509684002, 060001450, 840025697, 005069003, 108000700, 600500009"
