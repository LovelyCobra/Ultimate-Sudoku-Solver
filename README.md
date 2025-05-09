# Ultimate-Sudoku-Solver
Solving any Sudoku puzzle using both iteration and recursion with visualisation in CLI.

The program uses two simple iterative methods first. These are sufficient to completely solve all Sudoku puzzles on the easy, medium, hard and expert levels of difficulty (determined mainly by how many empty cells any given Sudoku puzzle contains, the expert level usually requiring to fill around 53 or 54 empty cells). Visualisation allows a user to watch as the empty cells are being filled. At the end the programe says how many empty cells have been filled during how many rounds.

When iteration isn't sufficient, the program then proceeds to apply the standard recursion with backtracking. Visualisation is not used for this part since it could prolong the execution to an unacceptable level. At the end the user can see how many trial guesses the recursive method had to make to complete the puzzle.

Then the program proceeds to solve the same sudoku again, this time using only the recursion. The trial guesses are counted again and the user then can compare the two numbers to see how much the initial iterative methods shortened the subsequent recursion when compared to just trial and error approach of mere recursion method.

### The two iterative methods are:
1. overt singles: iterating over all empty cells while checking the sets of possible guesses for any of them. If the set of possible guesses for any empty cell contains only one value, then that guess is placed there.
2. hidden singles: iterating over all allowed guesses for any empty cell and checking which of the values is only present there and not in any other set of allowed guesses for empty cells either on the same row, or the same column or the same 3x3-square.

TThese two methods are performed repeatedly as long as any of them finds at least one new valid guess. Only when there is no more new valid guess that these methods can find, the program proceeds with the recursion in the case the puzzle is not yet completely solved. Even in such a case the initial iteration reduces the number of trial guesses the recursion has to make as much as nine hundred times (that's the record, see the second sudoku puzzle recorded at the sudoku_container.txt; more commonly the shortening is at the level 3 or 4 times).

The main code is in **sudoku.py**. It uses a separate modul called **print.py** for visual side of the program and **cobraprint.py** for visualy appealing printing. All the previously used and solved sudoku puzzles are stored in **sudoku_container.txt** file, together with number of rounds and guesses needed to solved every puzzle.

### Have fun!
