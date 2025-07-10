from PySide6.QtWidgets import QWidget,QHBoxLayout,QPushButton
from cell import Cell
from PySide6.QtCore import Qt

class Editor(QWidget):
    def __init__(self,number_clicked_handler):
        super().__init__()

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        for num in "123456789":
            button = QPushButton(num)
            button.setFixedSize(50, 50)
            button.setStyleSheet("font-size:40px;")
            button.clicked.connect(lambda _, n=num: number_clicked_handler(n))
            layout.addWidget(button)
             
        self.setLayout(layout)

    def editor_clicked(self,value):
        return value
        
         

    
