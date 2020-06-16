from sudopy.solver import solve_puzzle

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
        return solve_puzzle(self)


    def __str__(self):
        return '\n'.join([' '.join([str(c) for c in row]) for row in self.data])


    def __getitem__(self, k):
        assert isinstance(k, tuple)
        assert len(k) == 2
        i, j = k
        return self.data[i][j]


    def __setitem__(self, k, v):
        assert isinstance(k, tuple)
        assert len(k) == 2
        i, j = k
        self.data[i][j] = v
