from copy import deepcopy
from time import sleep


class InvalidMove(Exception):
    '''Invalid move in sudoku'''


def next_rc(row, col):
    col += 1
    if col >= 9:
        col -= 9
        row += 1
    return row, col


def _solve_puzzle(puzzle, row, col):
    '''Solves a sudoku puzzle recursively by backtracking method.'''
    puzzle = deepcopy(puzzle)

    # space is not blank; skip
    if puzzle[row,col] != 0:
        return _solve_puzzle(puzzle, *next_rc(row, col))

    for i in range(9):
        try:
            puzzle[row,col] = i+1
        except InvalidMove:
            continue

        if row == 8 and col == 8:
            return puzzle

        if p := _solve_puzzle(puzzle, *next_rc(row, col)):
            return p

    return False


class Puzzle:

    def __init__(self, data):
        # data should be a 9x9 list of lists of int
        assert isinstance(data, list)
        assert len(data) == 9
        for r in data:
            assert isinstance(r, list)
            assert len(r) == 9
            for i in r:
                assert isinstance(i, int)
                assert 0 <= i <= 9

        self.data = data


    def complete(self):
        columnwise_sums = [0 for i in range(9)]
        rowwise_sums = [0 for i in range(9)]
        for i in range(9):
            for j in range(9):
                c = self[i,j]
                rowwise_sums[i] += c
                columnwise_sums[j] += c
        return all([s == 45 for s in columnwise_sums]) and all([s == 45 for s in rowwise_sums])



    def solve(self):
        solution = _solve_puzzle(self, 0, 0)
        self.data = solution.data


    def __str__(self):
        return '\n'.join([' '.join([str(c) if c > 0 else '-' for c in row]) for row in self.data])


    def __getitem__(self, coord):
        assert isinstance(coord, tuple)
        assert len(coord) == 2
        row, col = coord
        return self.data[row][coord]


    def check_valid_move(self, row, col, v):

        for i in range(9):
            if self[i, col] == v:
                return False
            if self[row, i] == v:
                return False

        sq_row, sq_col = int((row)//3)*3, int((col)//3)*3
        for i in range(sq_row, sq_row+3):
            for j in range(sq_col, sq_col+3):
                if self[i,j] == v:
                    return False

        return True


    def __setitem__(self, coord, value):
        assert isinstance(coord, tuple)
        assert len(coord) == 2
        assert isinstance(value, int)

        row, col = coord
        if not self.check_valid_move(row, col, value):
            raise InvalidMove()

        self.data[row][col] = value
