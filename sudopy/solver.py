from copy import deepcopy
from time import sleep


def next_rc(row, col):
    col += 1
    if col >= 9:
        col -= 9
        row += 1
    return row, col


def check_valid_move(puzzle, row, col, v):

    for i in range(9):
        if puzzle[i, col] == v:
            return False
        if puzzle[row, i] == v:
            return False

    sq_row, sq_col = int(row//3), int(col//3)
    for i in range(sq_row, sq_row+3):
        for j in range(sq_col, sq_col+3):
            if puzzle[i,j] == v:
                return False

    return True


def solve_puzzle(puzzle, row=0, col=0):
    puzzle = deepcopy(puzzle)

    # space is not blank; skip
    if puzzle[row,col] != 0:
        return solve_puzzle(puzzle, *next_rc(row, col))

    print(puzzle)
    print(row, col)
    print()
    sleep(1)

    # iter is oob: finished
    if row == 9:
        return puzzle

    for i in range(9):
        print('trying', i+1, '@', row, col)
        if not check_valid_move(puzzle, row, col, i+1):
            continue
        puzzle[row,col] = i+1

        if p := solve_puzzle(puzzle, *next_rc(row, col)):
            return p
        else:
            print('continuing from', i+1, '@', row, col)

    print('nothing left to do')
    print(puzzle)
    print(row, col)
    print()
    return False



def fact(i):
    if i == 1:
        return 1
    else:
        return fact(i-1)*i
