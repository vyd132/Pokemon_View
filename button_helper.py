from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget,QGraphicsScene,QGraphicsPixmapItem,QPushButton,QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QSize,Signal,QObject
import ui_imageMainform,requests,json,QtPixmapUtils
from io import BytesIO

class ButtonHelper(QObject):
    TYPE_LIST='List'
    TYPE_IMG='IMG'
    TYPE_NONE='Nothing'
    image_clicked=Signal()
    list_clicked=Signal(list,list)




    def __init__(self,button:QPushButton,type):
        QObject.__init__(self)
        self.type=type
        self.button=button
        self.button.clicked.connect(self.on_clicked)
        self.parent=None


    def set_list(self,list_img,parent=None):
        self.type = self.TYPE_LIST
        self.obj=list_img
        self.parent=parent

    def set_img(self,img):
        self.type = self.TYPE_IMG
        self.obj=img

    def set_none(self):
        self.type = self.TYPE_NONE
        self.obj=None


    def on_clicked(self):
        if self.type==self.TYPE_LIST:
            self.list_clicked.emit(self.obj,self.parent)
        if self.type==self.TYPE_IMG:
            self.image_clicked.emit()
        if self.type==self.TYPE_NONE:
            pass
