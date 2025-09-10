from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt

class PokList(QAbstractListModel):
    def rowCount(self,parent=None):
        return 10
    def data(self,index:QModelIndex,role:int):
        if role!=Qt.ItemDataRole.DisplayRole:
            return None
        return 0