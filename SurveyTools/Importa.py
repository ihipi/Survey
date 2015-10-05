'''
Created on 4 oct. 2015

@author: albert
'''
import FreeCAD,FreeCADGui
class Importa():
    """My new command"""
 
    def GetResources(self):
        return {"Pixmap"  : """
             /* XPM */
             static const char *test_icon[]={
             "16 16 2 1",
             "a c #000000",
             ". c None",
             "................",
             "................",
             "..############..",
             "..############..",
             "..############..",
             "......####......",
             "......####......",
             "......####......",
             "......####......",
             "......####......",
             "......####......",
             "......####......",
             "......####......",
             "......####......",
             "................",
             "................"};
             """,
                'Accel' : "", # a default shortcut (optional)
                'MenuText': "Importa",
                'ToolTip' : "Iporta un fitxer de punts"}
 
    def Activated(self):
        "Do something here"
        import Base, easygui, Draft, Importa_Gui
        
        
        ###################################################################################################
        '''
        from PySide import QtGui, QtCore
        # create new Tab in ComboView
        app = QtGui.qApp
        FCmw = App.activeWindow() # the active qt window, = the freecad window since we are inside it
        myNewFreeCADWidget = QtGui.QDockWidget() # create a new dckwidget
        myNewFreeCADWidget.ui = Importa_Gui.Importa_Dialog() # load the Ui script
        myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
        FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window

        ###############################################################################
        
        mw = Base.getMainWindow()
        tab = Base.getComboView(Base.getMainWindow())
        tab2=QtGui.QDialog()
        tab.addTab(Importa_Gui.Importa_Dialog().setupUi(tab2),"A Special Tab")
        
        #uic.loadUi("/importa.ui",tab2)
        tab2.show()
        
        
        #tab.removeTab(2)
        '''
        ##############################################################################333
        
        fitxer = easygui.fileopenbox('Tria un fitxer de punts (nom, x, y, z, codi)',default="/home/albert/.FreeCAD/Mod/Survey/puntos.PUN")                     # path and name of file.txt
        
        grup =  easygui.enterbox('tria un nom de grup')
        doc = FreeCAD.activeDocument()
        grp = doc.addObject("App::DocumentObjectGroup", grup )
        
        grp_punts  = grp.newObject("App::DocumentObjectGroup","Punts")

        grp_linies = grp.newObject("App::DocumentObjectGroup","Linies")
        
        file = open(fitxer, "r")                                  # open the file read
        X=Y=Z = 0.0
        codis = []
        code_list = []
        linies = {}
        inc = 0
        for linia in file:
           
            if linia[-1] == '\n':
                linia = linia[:-1]
            coordinates = linia.split('\t')
            N,X,Y,Z,C = coordinates  
            N = str(N)
            C = str(C) 
            
            
                     
            p = Base.crearPunt(str(N),float(X),float(Y),float(Z),C)         # create points (uncomment for use)
            
            grp_punts.addObject(p)
            
            punt_codis = C.split(',')
            
            for c in punt_codis:   
                codi_l=c.split(' ')
                codi_l = codi_l[0]+str(inc) 
                                                   #repassem el llistat de codis del punt
                '''
                if ' I' in c:                                           #si un dels codis avaba en '' I''
                    if codi_l in linies.keys():                                  
                                               #comprobem que no existeixi una linia ja creada
                        inc = inc +1                                    #en cas affirmatiu pujem el contador de linia    
                        codi_l = codi_l[0]+str(inc)
                    linies[codi_l]=[FreeCAD.Vector(float(X),float(Y),float(Z))]              # agreguem el punt a la llista de punt del seu codi
                    
                else:
                '''
                if codi_l not in linies.keys():
                    linies[codi_l]=[FreeCAD.Vector(float(X),float(Y),float(Z))]
                else:
                    for k, v in linies.items():
                        print k,v     
                                                                        # Si hi ha un codi linia l'agreguem a la seva llista
                        if codi_l == k:
                            
                            v.append(FreeCAD.Vector(float(X),float(Y),float(Z)))
                print c, codi_l  
            # separate the coordinates

        print linies
            
        if easygui.ynbox("Voleu crear les linies de rotura?"):
            for k,v in linies.items():
                l=[]
                for punt in v:
                    l.append(punt)
              
                wire=Draft.makeWire(l,closed=False,face=False,support=None)   # create the wire open
                wire.Label = k
                grp_linies.addObject(wire)
        #print codis, code_list
        file.close()
        return
 
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
 
FreeCADGui.addCommand('Importa',Importa())