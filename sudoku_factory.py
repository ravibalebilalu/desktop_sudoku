from sudoku import Sudoku
import random


def create_puzzle():
    seed = random.randint(1, 99999) 
    puzzle = Sudoku(width=3,seed=seed).difficulty(.1)
    challenge = puzzle.board
    solution = puzzle.solve().board
    print("new puzzle created")
    return challenge ,solution


 