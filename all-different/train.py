#from tasks.sudoku.rrn import SudokuRecurrentRelationalNet
from rrn import SudokuRecurrentRelationalNet
import trainer

trainer.train(SudokuRecurrentRelationalNet(False))
