#Printing Board nicely
def print_board(brd):
    #print("\nBoard:")
    print("┌───────┬───────┬───────┐")
    k = 1
    for r in range(9):
        print(f"│ {brd[r][0]} {brd[r][1]} {brd[r][2]} │ {brd[r][3]} {brd[r][4]} {brd[r][5]} │ {brd[r][6]} {brd[r][7]} {brd[r][8]} │")
        if k == 3 or k == 6:
            print("├───────┼───────┼───────┤")
        elif k == 9:
            print("└───────┴───────┴───────┘")
        k += 1
