from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget,QGraphicsScene,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import ui_widget,requests,json,QtPixmapUtils,imageWindowMain
from io import BytesIO
from folder_helper import Folder


class Pok_Widget():
    def __init__(self,parent:QWidget):
        self.a=QWidget(parent)
        self.b=ui_widget.Ui_Form()
        self.b.setupUi(self.a)
        self.b.imageButton.clicked.connect(self.image_window_show)
        self.window:imageWindowMain.Image_Mian_Window=None



    def widget_change(self,obj):
        self.a.show()
        pok_dict=requests.get(obj)
        pok_dict = json.loads(pok_dict.content)
        self.b.pokName.setText(pok_dict['name'])
        self.b.pokHP.setText(f"HP {self.stats_view(pok_dict['stats'],'hp')}")
        self.b.attack.setText(f"Атака {self.stats_view(pok_dict['stats'],'attack')}")
        self.b.defense.setText(f"Защита {self.stats_view(pok_dict['stats'],'defense')}")
        self.b.speed.setText(f"Скорость {self.stats_view(pok_dict['stats'],'speed')}")
        self.b.weight.setText(f"Вес {pok_dict['weight']}")
        self.b.height.setText(f"Рост {pok_dict['height']}")

        self.b.graphicsView.setScene(self.scene_create(pok_dict['sprites']['front_default']))
        # self.b.graphicsView.setSceneRect(0,0,self.b.graphicsView.sceneRect().width(),self.b.graphicsView.sceneRect().height())
        self.b.graphicsView.fitInView(self.b.graphicsView.sceneRect(),Qt.AspectRatioMode.KeepAspectRatio)
        image_list=self.image_list_create(pok_dict['sprites'])
        self.folder=Folder(image_list)
        if self.window is not None:
            self.window.button_image_prep(self.folder)


        print(obj)

    def stats_view(self,stats,el):
        for stat in stats:
            if stat['stat']['name']==el:
                return stat['base_stat']

    def scene_create(self,url):
        pixmap=self.pixmap_create(url)

        item = QGraphicsPixmapItem(pixmap)

        scene = QGraphicsScene()
        scene.addItem(item)
        return scene

    @staticmethod
    def pixmap_create(url):
        image_cont = requests.get(url)
        image = BytesIO(image_cont.content).read()

        pixmap = QPixmap()
        pixmap.loadFromData(image)
        pixmap = QtPixmapUtils.crop_transparent_area(pixmap)

        return pixmap

    def image_window_show(self):
        if self.window!=None:
            self.window.a.show()
            self.window.a.activateWindow()
            return
        self.window=imageWindowMain.Image_Mian_Window(None,self.folder)
        self.window.a.show()


    def image_list_create(self,image_dict:dict):
        images_list=[]
        for value in image_dict.values():
            if isinstance(value,str) :
                images_list.append(self.pixmap_create(value))
            elif isinstance(value,dict):
                images_list.append(self.image_list_create(value))
        # images_list=list(map(self.pixmap_create,images_list))
        return images_list





