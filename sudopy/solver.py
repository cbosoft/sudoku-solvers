from copy import deepcopy
from time import sleep


def next_rc(row, col):
    col += 1
    if col >= 9:
        col -= 9
        row += 1
    return row, col


