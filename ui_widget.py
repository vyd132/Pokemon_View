# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(431, 548)
        self.pokName = QLabel(Form)
        self.pokName.setObjectName(u"pokName")
        self.pokName.setGeometry(QRect(0, 0, 431, 31))
        font = QFont()
        font.setPointSize(18)
        self.pokName.setFont(font)
        self.pokHP = QLabel(Form)
        self.pokHP.setObjectName(u"pokHP")
        self.pokHP.setGeometry(QRect(0, 35, 431, 41))
        self.pokHP.setFont(font)
        self.height = QLabel(Form)
        self.height.setObjectName(u"height")
        self.height.setGeometry(QRect(0, 80, 431, 31))
        self.height.setFont(font)
        self.weight = QLabel(Form)
        self.weight.setObjectName(u"weight")
        self.weight.setGeometry(QRect(0, 120, 431, 31))
        self.weight.setFont(font)
        self.speed = QLabel(Form)
        self.speed.setObjectName(u"speed")
        self.speed.setGeometry(QRect(0, 240, 431, 31))
        self.speed.setFont(font)
        self.attack = QLabel(Form)
        self.attack.setObjectName(u"attack")
        self.attack.setGeometry(QRect(0, 160, 431, 31))
        self.attack.setFont(font)
        self.defense = QLabel(Form)
        self.defense.setObjectName(u"defense")
        self.defense.setGeometry(QRect(0, 200, 431, 31))
        self.defense.setFont(font)
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(170, 30, 256, 192))
        self.imageButton = QPushButton(Form)
        self.imageButton.setObjectName(u"imageButton")
        self.imageButton.setGeometry(QRect(190, 240, 221, 41))
        font1 = QFont()
        font1.setPointSize(15)
        self.imageButton.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pokName.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.pokHP.setText(QCoreApplication.translate("Form", u"HP", None))
        self.height.setText(QCoreApplication.translate("Form", u"\u0420\u043e\u0441\u0442", None))
        self.weight.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0441", None))
        self.speed.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.attack.setText(QCoreApplication.translate("Form", u"\u0410\u0442\u0430\u043a\u0430", None))
        self.defense.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0449\u0438\u0442\u0430", None))
        self.imageButton.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u0435 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438", None))
    # retranslateUi

