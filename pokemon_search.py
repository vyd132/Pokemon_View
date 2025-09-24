from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget,QCompleter,QApplication
from PySide6.QtCore import QRect,QEvent,QObject,QSortFilterProxyModel,Qt
from PySide6.QtGui import QColor

class PokemonSearch(QObject):
    def __init__(self,parent:QWidget,l:QWidget,objects_list):
        QObject.__init__(self)
        self.sort = QSortFilterProxyModel()
        self.sort.setSourceModel(objects_list)
        self.sort.sort(0)
        self.text=QtWidgets.QTextEdit(parent)
        self.text.setObjectName(u"pok_search")
        self.l=l
        rect = l.geometry()
        self.l.installEventFilter(self)
        self.text.installEventFilter(self)
        self.text.setGeometry(QRect(rect.right()-100,rect.top(), 100, 30))
        self.text.setStyleSheet("""
            background-color: lightyellow;
            border: 2px solid red;
            border-radius: 5px;
        """)
        self.text.hide()
        self.text.textChanged.connect(self.filter)
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress:
            print("Пользователь начал печатать")
            self.text.show()
            self.text.setFocus()
            QApplication.sendEvent(self.text,event)
        if event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Escape:
            self.text.hide()
            self.text.setText('')
        return super().eventFilter(obj, event)
    def filter(self):
        self.sort.setFilterFixedString(self.text.toPlainText())
        return self.sort





