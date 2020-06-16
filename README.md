# sudopy - sudoku solver

A silly-named sudoku puzzle solver. I wanted to try out test driven development
properly, and a sudoku solver seemed a good project to try out too.

Run tests with `python test.py`.

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
