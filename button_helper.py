from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget,QGraphicsScene,QGraphicsPixmapItem,QPushButton,QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QSize
import ui_imageMainform,requests,json,QtPixmapUtils
from io import BytesIO

class ButtonHelper():
    TYPE_LIST='List'
    TYPE_IMG='IMG'
    TYPE_NONE='Nothing'


    def __init__(self,button:QPushButton,type):
        self.type=type
        self.button=button
        self.button.clicked.connect(self.on_clicked)


    def set_list(self,list_img):
        self.type = self.TYPE_LIST
        self.obj=list_img

    def set_img(self,img):
        self.type = self.TYPE_IMG
        self.obj=img

    def set_none(self):
        self.type = self.TYPE_NONE
        self.obj=None


    def on_clicked(self):
        if self.type==self.TYPE_LIST:
            print(self.obj)
        if self.type==self.TYPE_IMG:
            print(self.obj)
        if self.type==self.TYPE_NONE:
            pass
