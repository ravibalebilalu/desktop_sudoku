from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout,QPushButton
from PySide6.QtCore import Qt

class Cell(QPushButton):
    def __init__(self,value,index=None,click_handler=None):
        self.value = value
        self.index = index
        super().__init__()
        self.setFixedSize(70,70)
        self.setText(str(self.value))
        self.clicked.connect(self.on_click)
        self.click_handler = click_handler


    def on_click(self):
        if self.click_handler:
            self.click_handler(self)
         
       
         
        


         
         
