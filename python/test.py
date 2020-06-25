import sys
from glob import glob

from sudopy import Puzzle, InvalidMove

def read_puzzles(puzzles_pattern):
    puzzles_paths = glob(puzzles_pattern)
    rv = list()
    for path in puzzles_paths:
        with open(path) as f:
            lines = f.readlines()
        cells = list()
        for line in lines:
            line = line.strip()
            if not line or '-' in line:
                continue
            if '=' in line:
                line = line[:line.index('=')]
            line = line.replace('|', '')
            cells.append([int(c) for c in line.split()])
        cells = cells[:9]
        rv.append(cells)
    return rv


def test_completion_check(puzzles, solutions):
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


def test_solver(puzzles):
    name = 'Solver test'

    for i, puzzle in enumerate(puzzles):
        puzzle = Puzzle(puzzles[0])

        try:
            puzzle.solve()
        except Exception as e:
            print(puzzle)
            print(f'{name} failed: solver fails to find solution ({i}).')
            raise


        if not puzzle.complete():
            print(puzzle)
            print(f'{name} failed: solver fails to find solution ({i}).')
            print(Puzzle(solutions[i]))
            sys.exit(1)

    print(f'{name} passed.')


if __name__ == '__main__':
    puzzles = read_puzzles('../puzzles/*.txt')
    solutions = read_puzzles('../solutions/*.txt')

    test_completion_check(puzzles, solutions)
    test_valid_move_check()
    test_solver(puzzles)
