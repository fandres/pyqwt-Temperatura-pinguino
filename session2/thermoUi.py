# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thermo.ui'
#
# Created: Sat Mar 29 17:07:35 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(211, 208)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.qwt_Thermo = QwtThermo(self.layoutWidget)
        self.qwt_Thermo.setEnabled(False)
        brush = QtGui.QBrush(QtGui.QColor(177, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.qwt_Thermo.setAlarmBrush(brush)
        self.qwt_Thermo.setAlarmLevel(30.0)
        self.qwt_Thermo.setScalePosition(QwtThermo.LeftScale)
        self.qwt_Thermo.setBorderWidth(1)
        self.qwt_Thermo.setMaxValue(100.0)
        self.qwt_Thermo.setPipeWidth(15)
        self.qwt_Thermo.setObjectName(_fromUtf8("qwt_Thermo"))
        self.horizontalLayout.addWidget(self.qwt_Thermo)
        self.frame = QtGui.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layoutWidget1 = QtGui.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 76, 88))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lcdNumber_1 = QtGui.QLCDNumber(self.layoutWidget1)
        self.lcdNumber_1.setObjectName(_fromUtf8("lcdNumber_1"))
        self.verticalLayout.addWidget(self.lcdNumber_1)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lcdNumber_2 = QtGui.QLCDNumber(self.layoutWidget1)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.verticalLayout.addWidget(self.lcdNumber_2)
        self.boton_conectar = QtGui.QPushButton(self.frame)
        self.boton_conectar.setGeometry(QtCore.QRect(10, 130, 99, 23))
        self.boton_conectar.setObjectName(_fromUtf8("boton_conectar"))
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Pinguino-PyQt-Qwt  [Temperatura]", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Termometro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Diferencia", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_conectar.setText(QtGui.QApplication.translate("Form", "Conectar", None, QtGui.QApplication.UnicodeUTF8))

#from qwt_thermo import QwtThermo
from PyQt4.Qwt5.Qwt import QwtThermo