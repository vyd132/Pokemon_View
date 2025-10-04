from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt,QAbstractTableModel
import requests,json,ui_mainwindow,random


class PokList(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        a = requests.get('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1302')
        self.pok_dict = json.loads(a.content)
        self.pok_list=self.pok_dict['results']
    def rowCount(self,parent=None):
        return len(self.pok_list)

    def columnCount(self,parent=None):
        return 2


    def data(self,index:QModelIndex,role:int):
        if role!=Qt.ItemDataRole.DisplayRole:
            return None
        if index.column()==0:
            return self.pok_list[index.row()]['name']
        if index.column()==1:
            return self.pok_list[index.row()]['url']

