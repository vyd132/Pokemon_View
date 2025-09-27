from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt
import requests,json,ui_mainwindow,random


class PokList(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)
        a = requests.get('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1302')
        self.pok_dict = json.loads(a.content)
        self.pok_list=self.pok_dict['results']
    def rowCount(self,parent=None):
        return len(self.pok_list)
    def data(self,index:QModelIndex,role:int):
        if role!=Qt.ItemDataRole.DisplayRole:
            return None
        return self.pok_list[index.row()]['name']
