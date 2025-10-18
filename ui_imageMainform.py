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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Button1 = QPushButton(Form)
        self.Button1.setObjectName(u"Button1")
        sizePolicy.setHeightForWidth(self.Button1.sizePolicy().hasHeightForWidth())
        self.Button1.setSizePolicy(sizePolicy)
        self.Button1.setMinimumSize(QSize(189, 189))
        self.Button1.setMaximumSize(QSize(189, 189))
        self.Button1.setBaseSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.Button1)

        self.Button4 = QPushButton(Form)
        self.Button4.setObjectName(u"Button4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Button4.sizePolicy().hasHeightForWidth())
        self.Button4.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.Button4)

        self.Button7 = QPushButton(Form)
        self.Button7.setObjectName(u"Button7")
        sizePolicy1.setHeightForWidth(self.Button7.sizePolicy().hasHeightForWidth())
        self.Button7.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.Button7)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Button2 = QPushButton(Form)
        self.Button2.setObjectName(u"Button2")
        sizePolicy1.setHeightForWidth(self.Button2.sizePolicy().hasHeightForWidth())
        self.Button2.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.Button2)

        self.Button5 = QPushButton(Form)
        self.Button5.setObjectName(u"Button5")
        sizePolicy1.setHeightForWidth(self.Button5.sizePolicy().hasHeightForWidth())
        self.Button5.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.Button5)

        self.Button8 = QPushButton(Form)
        self.Button8.setObjectName(u"Button8")
        sizePolicy1.setHeightForWidth(self.Button8.sizePolicy().hasHeightForWidth())
        self.Button8.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.Button8)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Button3 = QPushButton(Form)
        self.Button3.setObjectName(u"Button3")
        sizePolicy1.setHeightForWidth(self.Button3.sizePolicy().hasHeightForWidth())
        self.Button3.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.Button3)

        self.Button6 = QPushButton(Form)
        self.Button6.setObjectName(u"Button6")
        sizePolicy1.setHeightForWidth(self.Button6.sizePolicy().hasHeightForWidth())
        self.Button6.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.Button6)

        self.Button9 = QPushButton(Form)
        self.Button9.setObjectName(u"Button9")
        sizePolicy1.setHeightForWidth(self.Button9.sizePolicy().hasHeightForWidth())
        self.Button9.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.Button9)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Button1.setText("")
        self.Button4.setText("")
        self.Button7.setText("")
        self.Button2.setText("")
        self.Button5.setText("")
        self.Button8.setText("")
        self.Button3.setText("")
        self.Button6.setText("")
        self.Button9.setText("")
    # retranslateUi

