class Puzzle:

    def __init__(self, data):

        # data should be a 9x9 list of lists of int
        assert len(data) == 9
        for r in data:
            assert len(r) == 9
            for i in r:
                assert isinstance(i, int)
                assert 0 <= i <= 9

        self.data = data

    def complete(self):

        for col in self.data:
            if sum(col) != 45:
                return False

        transposed_data = list(zip(*self.data))
        for row in transposed_data:
            if sum(row) != 45:
                return False
