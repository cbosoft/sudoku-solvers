import sys

from sudopy import Puzzle, InvalidMove

# http://lipas.uwasa.fi/~timan/sudoku/
puzzles = [
    [
        [0, 4, 0, 0, 0, 0, 1, 7, 9],
        [0, 0, 2, 0, 0, 8, 0, 5, 4],
        [0, 0, 6, 0, 0, 5, 0, 0, 8],
        [0, 8, 0, 0, 7, 0, 9, 1, 0],
        [0, 5, 0, 0, 9, 0, 0, 3, 0],
        [0, 1, 9, 0, 6, 0, 0, 4, 0],
        [3, 0, 0, 4, 0, 0, 7, 0, 0],
        [5, 7, 0, 1, 0, 0, 2, 0, 0],
        [9, 2, 8, 0, 0, 0, 0, 6, 0]
    ]
]

solutions = [
    [
        [8, 4, 5, 6, 3, 2, 1, 7, 9],
        [7, 3, 2, 9, 1, 8, 6, 5, 4],
        [1, 9, 6, 7, 4, 5, 3, 2, 8],
        [6, 8, 3, 5, 7, 4, 9, 1, 2],
        [4, 5, 7, 2, 9, 1, 8, 3, 6],
        [2, 1, 9, 8, 6, 3, 5, 4, 7],
        [3, 6, 1, 4, 2, 9, 7, 8, 5],
        [5, 7, 4, 1, 8, 6, 2, 9, 3],
        [9, 2, 8, 3, 5, 7, 4, 6, 1]
    ]
]

def test_completion_check():
    name = 'Completion check test'
    for i, puzzle in enumerate(puzzles):
        puzzle = Puzzle(puzzle)
        if puzzle.complete():
            print(f'{name} failed: incomplete puzzle marked as complete ({i}).')
            exit(1)

    for i, solution in enumerate(solutions):
        solution = Puzzle(solution)
        if not solution.complete():
            print(f'{name} failed: complete puzzle marked as incomplete ({i}).')
            exit(1)

    print(f'{name} passed.')

def test_valid_move_check():
    name = 'Valid move check test'

    valid_moves = [
            [0, 0, 1, 0, 1, 2],
            [0, 0, 1, 1, 4, 1],
            [2, 2, 1, 0, 3, 1],
        ]

    for r1, c1, v1, r2, c2, v2 in valid_moves:
        puzzle = Puzzle([[0 for i in range(9)] for j in range(9)])
        puzzle[r1,c1] = v1

        try:
            puzzle[r2,c2] = v2
        except InvalidMove:
            print(puzzle)
            print(f'{name} failed: valid move erroneously counted as invalid.')
            exit(1)

    invalid_moves = [
            [0, 0, 1, 0, 8, 1],
            [0, 0, 1, 1, 1, 1],
            [0, 0, 1, 8, 0, 1],
        ]

    for r1, c1, v1, r2, c2, v2 in invalid_moves:
        puzzle = Puzzle([[0 for i in range(9)] for j in range(9)])
        puzzle[0,0] = 1

        try:
            puzzle[1,0] = 1
        except InvalidMove:
            pass
        else:
            print(f'{name} failed: invalid move not recognised.')
            exit(1)
    print(f'{name} passed.')


def test_solver():
    name = 'Solver test'

    for i, puzzle in enumerate(puzzles):
        puzzle = Puzzle(puzzles[0])
        solved = puzzle.solve()

        if not puzzle.complete():
            print(puzzle)
            print(f'{name} failed: solver fails to find solution ({i}).')
            print(Puzzle(solutions[i]))
            sys.exit(1)

    print(f'{name} passed.')

if __name__ == '__main__':
    test_completion_check()
    test_valid_move_check()
    test_solver()
