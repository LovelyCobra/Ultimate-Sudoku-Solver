import os, copy

def digit9_separator(integer):
    container = []
    i = 1
    while i < 10:
        container.append(integer % 10)
        integer = int(integer/10)
        i += 1
    container.reverse()
    return container

#Printing Board nicely
def print_board(brd, colors):
    
    print("┌───────┬───────┬───────┐")
    k = 1
    for r in range(9):
        print(f"│ {colors[r][0]}{brd[r][0]}\033[0m {colors[r][1]}{brd[r][1]}\033[0m {colors[r][2]}{brd[r][2]}\033[0m │ {colors[r][3]}{brd[r][3]}\033[0m {colors[r][4]}{brd[r][4]}\033[0m {colors[r][5]}{brd[r][5]}\033[0m │ {colors[r][6]}{brd[r][6]}\033[0m {colors[r][7]}{brd[r][7]}\033[0m {colors[r][8]}{brd[r][8]}\033[0m │")
        if k == 3 or k == 6:
            print("├───────┼───────┼───────┤")
        elif k == 9:
            print("└───────┴───────┴───────┘")
        k += 1

# Transform tables establishing corresponce between rows and columns within sudoku board to coordinates x, y of the terminal screen, to enable printing via ANSI escape codes
x_ = [3, 4, 5, 7, 8, 9, 11, 12, 13]
y_ = [3, 5, 7, 11, 13, 15, 19, 21, 23]


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    
    board = input("\nInput the initial board as a string on nine nine-digit numbers separated by ', ':\n")
    
    board = board.split(", ")
    board = list(map(int, board))
    board = list(map(digit9_separator, board))
    
    print_board(board)
