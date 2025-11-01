from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget,QGraphicsScene,QGraphicsPixmapItem,QPushButton,QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QSize
import ui_imageMainform,requests,json,QtPixmapUtils,button_helper
from folder_helper import Folder
from button_helper import ButtonHelper
from io import BytesIO

class Image_Mian_Window():
    def __init__(self,parent:QWidget,images):
        self.a=QWidget(parent)
        self.b=ui_imageMainform.Ui_Form()
        self.b.setupUi(self.a)
        self.a.show()
        self.a.setWindowFlags(Qt.WindowType.Window|Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.buttons = []
        self._button_prop()
        self.button_image_prep(images)





    def button_image(self,button:QPushButton,image:QPixmap):
        image=image.scaled(button.contentsRect().width()-20,button.contentsRect().height()-20,Qt.AspectRatioMode.KeepAspectRatio)

        button.setIcon(image)
        button.setIconSize(image.size())



    def button_image_prep(self,folder:Folder):
        for button_num in range(len(self.buttons)):
            bh:ButtonHelper=self.buttons[button_num]


            if button_num>len(folder.images)-1:
                img_pixmap = QPixmap()
                img_pixmap.load('folder.png')
                button_num=button_num-len(folder.images)
                if button_num>len(folder.children)-1:
                    img_pixmap = QPixmap()
                    self.button_image(bh.button,img_pixmap)
                    bh.set_none()
                    continue
                self.button_image(bh.button, img_pixmap)
                bh.set_list(folder.children[button_num])
                continue

            img = folder.images[button_num]

            self.button_image(bh.button, img)
            bh.set_img(img)

        if folder.parent is None:
            return
        img_pixmap = QPixmap()
        img_pixmap.load('folder_up.png')
        self.button_image(self.buttons[8].button, img_pixmap)
        self.buttons[8].set_list(folder.parent)



    def _button_prop(self):
        for button_num in range(1,10):
            button=f'Button{button_num}'
            if not hasattr(self.b,button):
                continue
            a:QPushButton=getattr(self.b,button)
            a.setMinimumSize(189,189)
            a.setMaximumSize(189,189)
            a.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)

            bh=ButtonHelper(a,ButtonHelper.TYPE_NONE)
            bh.image_clicked.connect(lambda: print('work'))
            bh.list_clicked.connect(self.button_image_prep)
            self.buttons.append(bh)








