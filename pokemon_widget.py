from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget
import ui_widget,requests,json



class Pok_Widget():
    def __init__(self,parent:QWidget):
        self.a=QWidget(parent)
        self.b=ui_widget.Ui_Form()
        self.b.setupUi(self.a)


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
        print(obj)

    def stats_view(self,stats,el):
        for stat in stats:
            if stat['stat']['name']==el:
                return stat['base_stat']

