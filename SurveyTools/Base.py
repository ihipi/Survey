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


def creaCarpeta(name='nom'):
    '''
    Check if a group with designed name exists or create one 
    and return it 
    '''
    
    
    doc = FreeCAD.activeDocument()
    for obj in doc.Objects:
        if obj.Label == name:
            if  obj.TypeId == 'App::DocumentObjectGroup':
                return obj
    
    grp = doc.addObject("App::DocumentObjectGroup", name )
    return grp

def crearPunt(X=0, Y=0,Z=0, name = "Point",Code = '', size= 5):
    ''' creaPunt(name, x,y,z ,code, size) or 
        creaPunt(Vector,name, code, size)
        create a Point with custom name and code
    '''
    obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython",str(name))   #create a object with your name
    if isinstance(X,FreeCAD.Vector):      # if a Vector is  passed assigns values to x,y,z              
        Z = X.z
        Y = X.y
        X = X.x
    Punt(obj,name, X,Y,Z,Code)              #creates the object
    obj.X = X
    obj.Y = Y
    obj.Z = Z
    
    obj.ViewObject.PointSize = size         # asigns the size point
    obj.ViewObject.Proxy =0
    FreeCAD.ActiveDocument.recompute()
    return obj


class Punt():
    "Punt de topografia"
    def __init__(self, obj,name=None,x=0,y=0,z=0, c=None):
        #adding the object properties
        obj.Label = str(name)                                   
        obj.addProperty("App::PropertyString","Tipus","Propietats","Descripcio").Tipus = 'Punt'
        obj.addProperty("App::PropertyString","Codi","Base","Descripcio").Codi = str(c)
        obj.addProperty("App::PropertyFloat","X","Coordenades","Location").X = x
        obj.addProperty("App::PropertyFloat","Y","Coordenades","Location").Y = y
        obj.addProperty("App::PropertyFloat","Z","Coordenades","Location").Z = z
        
        #hiding the properties Tipus and placement
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
        punt = Part.Vertex(FreeCAD.Vector(obj.X,obj.Y,obj.Z))
        obj.Shape = punt
        
    def onChanged(self, obj, prop):
        pass 
    
    
def creaSuperficie(name='superficie', punts=[],linies=None):
    '''
    crea un objecte superficie
    '''
    doc = FreeCAD.activeDocument()
    obj = doc.addObject('App::DocumentObjectGroupPython',name)
    Superficie(obj, name)
    FreeCAD.ActiveDocument.recompute()
    return obj
    
    
class Superficie():
    "objecte superficie"
    def __init__(self, obj,name='Sup', punts=[],linies=[]):
        #adding the object properties
        obj.Label = str(name)                
        obj.addProperty("App::PropertyString","Tipus","Propietats","Descripcio").Tipus = 'Superficie'
                   
        obj.addProperty("App::PropertyVectorList","Punts","Definition",'llista de pnts').Punts = punts
        obj.addProperty("App::PropertyVectorList","Linies","Definition",'llista de linies').Linies = linies
        obj.addProperty("App::PropertyVectorList","Triangles","Definition",'llista de triangles').Triangles = []
        self.Type='Superficie'
        mode = 2
        obj.setEditorMode("Tipus", mode)
        obj.Proxy= self
        
        

    def __getstate__(self):
        return self.Type

    def __setstate__(self,state):
        if state:
            self.Type = state  
            
    def execute(self, obj):
        pass
        
    def onChanged(self, obj, prop):
        pass 
