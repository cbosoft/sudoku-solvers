import sys

from sudopy import generate_puzzle, solve_puzzle

def test():
    puzzle = generate_puzzle()
    solved = solve_puzzle(puzzle)

    if puzzle.complete():
        print('pass')
    else:
        print('fail')
        sys.exit(1)
