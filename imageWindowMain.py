from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget,QGraphicsScene,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import ui_widget,requests,json,QtPixmapUtils
from io import BytesIO

class Image_Mian_Window():
    def __init__(self,parent:QWidget):
        self.a=QWidget(parent)
        self.b=ui_widget.Ui_Form()
        self.b.setupUi(self.a)