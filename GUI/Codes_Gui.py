# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Codes.ui'
#
# Created: Mon Oct 19 21:53:48 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from SurveyTools.Tools import selectPointsGroup

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(793, 494)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 771, 471))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 771, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.llistaCodis = QtGui.QListWidget(self.verticalLayoutWidget)
        self.llistaCodis.setObjectName("llistaCodis")
        self.horizontalLayout.addWidget(self.llistaCodis)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.llistaCodisLinia = QtGui.QListWidget(self.verticalLayoutWidget)
        self.llistaCodisLinia.setObjectName("llistaCodisLinia")
        self.horizontalLayout.addWidget(self.llistaCodisLinia)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox = QtGui.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(-1, -1, 771, 201))
        self.groupBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Code Configuration", None, QtGui.QApplication.UnicodeUTF8))

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Codes_Gui, self)
        from SurveyTools.Tools import selectPointsGroup
        for p in selectPointsGroup():
            self.ui.llistaCodis.addItem(p.Codi)
        self.ui =Ui_Form()
        self.ui.setupUi(self)
        

def Codes_Gui(parent=None):
    mySW = MainWindow(parent)
    mySW.show()
    
    
