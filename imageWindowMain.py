from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget,QGraphicsScene,QGraphicsPixmapItem,QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QSize
import ui_imageMainform,requests,json,QtPixmapUtils
from io import BytesIO

class Image_Mian_Window():
    def __init__(self,parent:QWidget,image):
        self.a=QWidget(parent)
        self.b=ui_imageMainform.Ui_Form()
        self.b.setupUi(self.a)
        self.a.show()
        self.button_image(self.b.Button1,image)



    def button_image(self,button:QPushButton,image):
       image=image.scaled(button.size())
       button.setIcon(image)
       button.setIconSize(button.size())
       print(button.size())
