'''
Created on 3 oct. 2015

@author: albert
'''
import FreeCAD
from PySide import QtGui,QtCore


def getMainWindow():
    "returns the main window"
    # using QtGui.qApp.activeWindow() isn't very reliable because if another
    # widget than the mainwindow is active (e.g. a dialog) the wrong widget is
    # returned
    toplevel = QtGui.qApp.topLevelWidgets()
    for i in toplevel:
        if i.metaObject().className() == "Gui::MainWindow":
            return i
    raise Exception("No main window found")

def getComboView(mw):
    dw=mw.findChildren(QtGui.QDockWidget)
    for i in dw:
        if str(i.objectName()) == "Combo View":
            return i.findChild(QtGui.QTabWidget)
        elif str(i.objectName()) == "Python Console":
            return i.findChild(QtGui.QTabWidget)
    raise Exception ("No tab widget found")


def crearPunt(name = "Point",X=0, Y=0,Z=0, Code = ''):
    ''' makePoint(x,y,z ,[color(r,g,b),point_size]) or
        makePoint(Vector,color(r,g,b),point_size]) -
        creates a Point in the current document.
        example usage: 
        p1 = makePoint()
        p1.ViewObject.Visibility= False # make it invisible
        p1.ViewObject.Visibility= True  # make it visible
        p1 = makePoint(-1,0,0) #make a point at -1,0,0
        p1 = makePoint(1,0,0,(1,0,0)) # color = red
        p1.X = 1 #move it in x
        p1.ViewObject.PointColor =(0.0,0.0,1.0) #change the color-make sure values are floats
    '''
    obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython",str(name))
    if isinstance(X,FreeCAD.Vector):
        Z = X.z
        Y = X.y
        X = X.x
    Punt(obj,name, X,Y,Z,Code)
    obj.X = X
    obj.Y = Y
    obj.Z = Z
    
    obj.ViewObject.PointSize = 5.00
    obj.ViewObject.Proxy =0
    FreeCAD.ActiveDocument.recompute()
    return obj

class Punt():
    "The Draft Point object"
    def __init__(self, obj,name=None,x=0,y=0,z=0, c=None):
        obj.Label = str(name)
        obj.addProperty("App::PropertyString","Tipus","Propietats","Descripcio").Tipus = 'Punt'
        obj.addProperty("App::PropertyString","Codi","Base","Descripcio").Codi = str(c)
        obj.addProperty("App::PropertyFloat","X","Coordenades","Location").X = x
        obj.addProperty("App::PropertyFloat","Y","Coordenades","Location").Y = y
        obj.addProperty("App::PropertyFloat","Z","Coordenades","Location").Z = z
        
        
        mode = 2
        obj.setEditorMode('Placement',mode)
        obj.setEditorMode("Tipus", mode)
        obj.Proxy= self
        

    def __getstate__(self):
        return self.Type

    def __setstate__(self,state):
        if state:
            self.Type = state  
            
    def execute(self, obj):
        import Part
        shape = Part.Vertex(FreeCAD.Vector(obj.X,obj.Y,obj.Z))
        obj.Shape = shape
        
    def onChanged(self, obj, prop):
        pass 
