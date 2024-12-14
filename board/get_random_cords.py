import random
from .board import board


def one():
    row_i = random.randint(0, 3)
    col_i = random.randint(0, 3)
    return [row_i, col_i]


def two():
    pair1 = one()
    pair2 = one()
    while pair1 == pair2:
        pair2 = one()

    return [pair1, pair2]


def get_blank():
    blanks = [
        (i, j) for i, row in enumerate(board) for j, col in enumerate(row) if col == 0
    ]
    return random.choice(blanks) if blanks else None
