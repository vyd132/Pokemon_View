from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget,QGraphicsScene,QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import ui_widget,requests,json,QtPixmapUtils,imageWindowMain
from io import BytesIO



class Pok_Widget():
    def __init__(self,parent:QWidget):
        self.a=QWidget(parent)
        self.b=ui_widget.Ui_Form()
        self.b.setupUi(self.a)
        self.b.imageButton.clicked.connect(self.image_window_show)


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

    def pixmap_create(self,url):
        image_cont = requests.get(url)
        image = BytesIO(image_cont.content).read()

        pixmap = QPixmap()
        pixmap.loadFromData(image)
        pixmap = QtPixmapUtils.crop_transparent_area(pixmap)

        return pixmap

    def image_window_show(self):
        image=self.pixmap_create('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png')
        self.window=imageWindowMain.Image_Mian_Window(None,image)
        self.window.a.show()