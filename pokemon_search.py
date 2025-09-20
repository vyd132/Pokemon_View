from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QRect


class PokemonSearch():
    def __init__(self,parent:QWidget):

        self.text=QtWidgets.QTextEdit(parent)
        self.text.setObjectName(u"pok_search")
        self.text.setGeometry(QRect(500, 100, 251, 31))


