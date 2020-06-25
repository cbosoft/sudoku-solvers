# sudoku solver, written in python

Run tests with `python test.py`.

# Usage

Use the solver by importing it into a script. For example:

```python
from sudopy import Puzzle

def read_puzzle(path):
    with open(path) as f:
        lines = f.readlines()
    data = [line.split() for line in lines]
    return Puzzle(data)

puzzle = read_puzzle('sudoku.txt')
print(puzzle)
print()

puzzle.solve()
print(puzzle)
```
