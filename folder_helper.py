from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget,QGraphicsScene,QGraphicsPixmapItem,QPushButton,QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QSize
import ui_imageMainform,requests,json,QtPixmapUtils,button_helper

from io import BytesIO



class Folder():
    def __init__(self,objects_list,parent=None):
        self.objects_list=objects_list
        self.parent=parent
        self.images=[]
        self.children=[]
        self._children_folder()


    def _children_folder(self):
        for obj in self.objects_list:
            if isinstance(obj,QPixmap):
                self.images.append(obj)
            elif len(obj)!=0:
                child=Folder(obj, self)
                if not child._is_empty():
                    self.children.append(child)




    def _is_empty(self):
        return len(self.images)==0 and len(self.children)==0




