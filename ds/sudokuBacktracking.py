from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            """
            this will check if we can place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)])

        #place the number d in (row, col) cell
        def place_number(d, row, col ):
            # increase the count by 1 in row and column
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] +=1
            board[row][col] = str(d)

        #remove the number which didn't lead to a solution
        def remove_number(d, row, col):
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        #this function will be called recuseverly to place numbers till the moment we have a solution
        def place_next_numbers(row, col):
            #if we are in the last cell, it shows that we have solution
            if col == N -1 and row == N -1:
                nonlocal sudoku_solved
                sudoku_solved = True
            # not yet the solution
            else:
                #in the case of the end of row go to the next row
                if col == N -1:
                    backtrack(row +1, 0)
                else:
                    backtrack(row, col+1)
            
        def backtrack(row = 0, col =0):
            """
            Backtracking
            """
            #if the cell is empty
            if board[row][col] == '.':
                #iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        #since the single unique solution is promised
                        
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        #box size
        n = 3
        # row size
        N = n * n
        #lambda function to compute box index
        box_index = lambda row, col : (row//n) * n + col // n

        #init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)


        sudoku_solved = False
        backtrack()
