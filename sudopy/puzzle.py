from copy import deepcopy
from time import sleep


class InvalidMove(Exception):
    '''Invalid move in sudoku'''


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

    def next_rc(self, row, col):
        col += 1
        if col >= 9:
            col -= 9
            row += 1
        return row, col



    def solve(self, row=0, col=0):
        puzzle = deepcopy(self)
    
        # space is not blank; skip
        if puzzle[row,col] != 0:
            return puzzle.solve(*puzzle.next_rc(row, col))
    
        print(puzzle)
        print(row, col)
        print()
        #sleep(1)
    
        # iter is oob: finished
        if row == 9:
            self.data = puzzle.data
    
        for i in range(9):
            print('trying', i+1, '@', row, col)
            try:
                puzzle[row,col] = i+1
            except InvalidMove:
                continue

            if p := puzzle.solve(*puzzle.next_rc(row, col)):
                return p
            else:
                print('continuing from', i+1, '@', row, col)
    
        print('nothing left to do')
        print(puzzle)
        print(row, col)
        print()
        return False


    def __str__(self):
        return '\n'.join([' '.join([str(c) if c > 0 else '-' for c in row]) for row in self.data])


    def __getitem__(self, k):
        assert isinstance(k, tuple)
        assert len(k) == 2
        i, j = k
        return self.data[i][j]


    def check_valid_move(self, row, col, v):

        for i in range(9):
            if self[i, col] == v:
                print('incol',v,i,col)
                return False
            if self[row, i] == v:
                print('inrow')
                return False

        sq_row, sq_col = int((row)//3)*3, int((col)//3)*3
        for i in range(sq_row, sq_row+3):
            for j in range(sq_col, sq_col+3):
                if self[i,j] == v:
                    print('insq', i, j, row,col, sq_row, sq_col)
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
