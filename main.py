from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt
import sys
import numpy as np

from cell import Cell
from editor import Editor
from sudoku_factory import create_puzzle
from util import row_col_select, is_puzzle_incomplete


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 0, 1000, 700)
        self.font_size = "40px"
        self.highlighted_indices = []
        self.selected_cell = None
        self.selected_number = None
        self.cell_checked = False

        self.load_puzzle_ui()


    def load_puzzle_ui(self):
        # Cleanup old puzzle if reloading
        old_widget = self.centralWidget()
        if old_widget:
            old_widget.deleteLater()

        # 🧠 Clear stale references
        self.selected_cell = None
        self.highlighted_indices = []

         
        challenge, solution =  create_puzzle()
        self.solution = np.array(solution).flatten()

        self.all_cells = []
        col_g = QVBoxLayout()
        col_g.setAlignment(Qt.AlignmentFlag.AlignCenter)

        count = 0
        for row in challenge:
            row_g = QHBoxLayout()
            row_g.setAlignment(Qt.AlignmentFlag.AlignCenter)
            for value in row:
                text = value if value else " "
                cell = Cell(text, count, self.handle_cell_click)
                cell.setStyleSheet(f"font-size:{self.font_size}; background-color:#333;")
                self.all_cells.append(cell)
                row_g.addWidget(cell)
                count += 1
            col_g.addLayout(row_g)

        grid_widget = QWidget()
        grid_widget.setLayout(col_g)

        editor = Editor(self.handle_editor_click)

        central_layout = QVBoxLayout()
        central_layout.addWidget(grid_widget)
        central_layout.addWidget(editor)

        central_widget = QWidget()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)


    def handle_cell_click(self, cell):
        # Reset previous selection
        if self.selected_cell and self.selected_cell.text().strip() == "":
            self.selected_cell.setStyleSheet(
                f"font-size:{self.font_size}; background-color:#333;"
            )

        self.selected_cell = cell

        # Highlight newly selected cell
        if cell.text().strip() == "":
            cell.setStyleSheet(
                f"border:1px solid gray; font-size:{self.font_size}; background-color:#333;"
            )

        # Highlight related cells
        index = self.selected_cell.index
        row_indices, col_indices, block_indices = row_col_select(index)
        self.highlight_cells(row_indices + col_indices + block_indices)

        # Check puzzle completion
        if not is_puzzle_incomplete(self.all_cells):
            self.load_puzzle_ui()

    def handle_editor_click(self, number):
        if self.selected_cell:
            self.selected_number = str(number)
            correct_value = str(self.solution[self.selected_cell.index])
            if self.selected_number == correct_value:
                self.cell_checked = True
                self.selected_cell.setText(self.selected_number)
                self.selected_cell.setStyleSheet(
                    f"border:1px solid gray; font-size:{self.font_size}; background-color:#333;"
                )
                self.selected_cell.setCheckable(False)

    def highlight_cells(self, new_indices):
        for i in self.highlighted_indices:
            cell = self.all_cells[i]
            if cell.text().strip() == "":
                cell.setStyleSheet(
                    f"background-color: #333; font-size:{self.font_size};")
            else:
                cell.setStyleSheet(
                    f"font-size:{self.font_size}; background-color:#333;")

        for i in new_indices:
            cell = self.all_cells[i]
            cell.setStyleSheet(
                f"background-color: #555; font-size:{self.font_size};")

        self.highlighted_indices = new_indices


# Run the app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
