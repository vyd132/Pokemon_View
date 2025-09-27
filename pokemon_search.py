from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QCompleter, QApplication,QListView
from PySide6.QtCore import QRect, QEvent, QObject, QSortFilterProxyModel, Qt



class PokemonSearch(QObject):
    def __init__(self, l: QListView):
        QObject.__init__(self)
        self.sort = QSortFilterProxyModel()
        self.sort.setSourceModel(l.model())
        self.sort.sort(0)
        self.text = QtWidgets.QTextEdit(l)
        # self.text.setObjectName(u"")
        self.l = l
        rect = l.geometry()
        self.l.installEventFilter(self)
        self.text.installEventFilter(self)
        self.text.setGeometry(QRect(rect.width()-100, 0, 100, 30))
        self.text.setStyleSheet("""
            background-color: lightyellow;
            border: 2px solid red;
            border-radius: 5px;
        """)
        self.text.hide()
        self.text.textChanged.connect(self.filter)
        self.l.setModel(self.sort)

    def eventFilter(self, obj: QWidget, event):
        if event.type() != QEvent.Type.KeyPress:
            return super().eventFilter(obj, event)
        print(obj,event)
        if obj is self.l:
            return self.eventFliter_list(event)
        if obj is self.text:
            return self.eventFliter_text(event)


    def eventFliter_list(self,event):
        self.text.show()
        self.text.setFocus()
        QApplication.sendEvent(self.text, event)
        return True

    def eventFliter_text(self,event):
        if event.key() == Qt.Key.Key_Escape:
            self.text.hide()
            self.text.setText('')
        else:
            self.text.show()
            return super().eventFilter(self.text, event)
        return True



    def filter(self):
        self.sort.setFilterFixedString(self.text.toPlainText())

