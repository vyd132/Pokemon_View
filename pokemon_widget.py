from PySide6.QtWidgets import QApplication,QMainWindow,QCompleter,QWidget
import ui_widget



class Pok_Widget(QWidget,ui_widget.Ui_Form):
    def __init__(self,parent:QWidget):
        QWidget.__init__(self,parent)
        self.setupUi(self)


    def widget_change(self,obj):

        self.show()
        self.pokName.setText('123')
        print(obj)
