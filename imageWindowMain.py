from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget,QGraphicsScene,QGraphicsPixmapItem,QPushButton,QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QSize
import ui_imageMainform,requests,json,QtPixmapUtils,button_helper
from button_helper import ButtonHelper
from io import BytesIO

class Image_Mian_Window():
    def __init__(self,parent:QWidget,images):
        self.a=QWidget(parent)
        self.b=ui_imageMainform.Ui_Form()
        self.b.setupUi(self.a)
        self.a.show()
        self.a.setWindowFlags(Qt.WindowType.Window|Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.connectors = []
        self.button_size_block(images)





    def button_image(self,button:QPushButton,image:QPixmap):
        image=image.scaled(button.contentsRect().width()-20,button.contentsRect().height()-20,Qt.AspectRatioMode.KeepAspectRatio)

        button.setIcon(image)
        button.setIconSize(image.size())



    def button_size_block(self,images):
        for button_num in range(1,10):
            button=f'Button{button_num}'
            if not hasattr(self.b,button):
                continue
            a:QPushButton=getattr(self.b,button)
            a.setMinimumSize(189,189)
            a.setMaximumSize(189,189)
            a.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)

            bh=ButtonHelper(a,ButtonHelper.TYPE_NONE)
            self.connectors.append(bh)

            if button_num>len(images):
                a.setIcon(QPixmap())
                bh.set_none()
                continue

            if isinstance(images[button_num-1],QPixmap):
                self.button_image(a, images[button_num - 1])
                bh.set_img(images[button_num-1])

            elif isinstance(images[button_num-1],list):
                img=QPixmap()
                img.load('folder.png')
                self.button_image(a, img)
                bh.set_list(images[button_num-1])









