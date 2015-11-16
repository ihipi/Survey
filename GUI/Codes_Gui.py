# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Codes.ui'
#
# Created: Mon Oct 19 21:53:48 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from SurveyTools import Tools
import FreeCAD,FreeCADGui, Draft, Part

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Codes definition")
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
        self.pushButton_uneix = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_uneix.setObjectName("pushButton_uneix")
  
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_uneix.setText(QtGui.QApplication.translate("Form", "Uneix codis de linia", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Code Configuration", None, QtGui.QApplication.UnicodeUTF8))
        

        
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.doc = FreeCAD.activeDocument()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.add)
        self.ui.pushButton.clicked.connect(self.remove)
        self.ui.pushButton_uneix.clicked.connect(self.uneix)
        for p in self.doc.getObject("Breaklines").Codis:
            self.ui.llistaCodisLinia.addItem(p)
            
        for p in Tools.selectPointsGroup(codes_dict=True):
            if p not in  self.doc.getObject("Breaklines").Codis:
                
                self.ui.llistaCodis.addItem(unicode(p))
            
    def add(self):
        llista = self.ui.llistaCodis
        self.ui.llistaCodisLinia.addItem(self.ui.llistaCodis.takeItem(llista.currentRow()))#llista.currentItem().text()) 
        self.actualitzaCodis()
        
    def remove(self):
        llista = self.ui.llistaCodisLinia
        self.ui.llistaCodis.addItem(self.ui.llistaCodisLinia.takeItem(llista.currentRow()))
        self.actualitzaCodis()

        
    def actualitzaCodis(self):
        llista = self.ui.llistaCodisLinia

        codesList = []
        for i in xrange(llista.count()):
            codesList.append(unicode(str(self.ui.llistaCodisLinia.item(i).text()), 'utf-8'))
        
        resta = list(set(self.doc.getObject("Breaklines").Codis)-set(codesList))
        if len(resta)>0:
            for c in resta:
                self.doc.getObject(c).removeObjectsFromDocument()
                self.doc.removeObject(c)
            
        self.doc.getObject("Breaklines").Codis = codesList     
        
    def uneix(self): 
        linies = set(self.doc.getObject("Breaklines").Codis)
        print linies
        breaklines = dict()
        linenum = dict()
        for i in linies:
            breaklines[i]= dict()
            linenum[i]=0
        
        print Tools.selectPointsGroup()
        for p in Tools.selectPointsGroup():
            print p.Label+"_"+p.Codi
            print breaklines
            
            if p.Inici:
                key = str(p.Codi)

                print 'codi amb " I"', key
                if key in linies:
                    print 'nova linia'
                    
                    
                    print key
                    linenum[key]= linenum[key]+1

                    breaklines[key][key+'_'+str(linenum[key])]=[p]
                
            elif p.Codi in linies:
                key = unicode(p.Codi)
                if len(breaklines[key])==0:
                    print 'nova linia sense " I"'
                    breaklines[key][key+'_'+str(linenum[key])]=[p]
                
                else:
                    print 'linia existent'
                
                    breaklines[key][p.Codi+'_'+str(linenum[key])].append(p)
        
        
        breakline_group = self.doc.getObject("Breaklines")
        for codi, linia in breaklines.iteritems():
            exists =False
            for codigrup in breakline_group.Group:
                print '161', codigrup.Label,codi
                if codigrup.Label == codi:
                    k_grup = codigrup
                    exists = True
            if not exists:
                k_grup = breakline_group.newObject("App::DocumentObjectGroupPython",str(codi))
                #k_grup.addProperty("App::PropertyLinkList","Linia","Definition",'llista els punts de la linia').Linia = []
            print '169',exists
            
            for nom, punts in linia.iteritems():
                print '172',nom, punts
                l=[]
                l_prop = []
                # crear llista de tuplas de (X,Y,Z)
                for punt in punts:
                    l_prop.append(punt) 
                    l.append((punt.X,punt.Y,punt.Z))
                    
                    
                    
                linia_exists = False
                print l
                for lin in k_grup.Group:
                    print '185',lin.Label,nom
                    if lin.Label == nom:
                        linia_exists=True
                print linia_exists
                
                if not linia_exists:
                    wire=Draft.makeWire(l,closed=False,face=False,support=None)   # create the wire open
                    wire.Label = nom  
                    k_grup.addObject(wire)                    
                
                
                
                

#                 if nom not in self.doc.getObjectsByLabel(nom) :
#                     print 'if'
# 
#                     wire=Draft.makeWire(l,closed=False,face=False,support=None)   # create the wire open
#                     wire.Label = nom  
#                     k_grup.addObject(wire)
#                     #k_grup.Linia= l_prop
#             
#                 else:
#                     wire=Draft.makeWire(l,closed=False,face=False,support=None)   # create the wire open
#                     wire.Label = nom  
#                     self.doc.getObject(nom).addObject(wire)
#                     print 'else'
                
    
def Codes_Gui(parent=None):
    mySW = MainWindow(Tools.getMainWindow())
    mySW.show()
    
    
