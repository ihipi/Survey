'''
Created on 17 oct. 2015

@author: albert
'''
import FreeCADGui, FreeCAD
class NewProject():
    """Creates a new project structure"""
 
    def GetResources(self):
        return {'Pixmap'  : ":/icons/newProject.svg", # the name of a svg file available in the resources
                'Accel' : "", # a default shortcut (optional)
                'MenuText': "New project",
                'ToolTip' : "crea l'estructura d'un project Survey"}
 
    def Activated(self):
        "Do something here"
        
        creaProjecte('Projecte')
        return
 
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
    
    
class CarpetaProjecte():
    "objecte superficie"
    def __init__(self, obj,name='nom', tipus='tipus'):
        #adding the object properties
        obj.Label = str(name)                
        obj.addProperty("App::PropertyString","Tipus","Propietats","Descripcio").Tipus = tipus
        if tipus == "breaklines":
            obj.addProperty("App::PropertyStringList","Codis","Propietats","LLista de codis existents").Tipus = []
        self.Type=tipus
        mode = 1
        obj.setEditorMode("Tipus", mode)
        obj.setEditorMode("Label", mode)
        obj.Proxy= self
        
        

    def __getstate__(self):
        return self.Type

    def __setstate__(self,state):
        if state:
            self.Type = state  
            
    def execute(self, obj):
        pass
        
    def onChanged(self, obj, prop):
        if prop == 'Label' or prop== 'Name':
            obj.Label = obj.Tipus
            
        elif prop == "Codis":
            obj.Codis = prop

def creaCarpetaProjecte(name='nom', tipus='Tipus', doc = None):
    '''
    Check if a group with designed name exists or create one 
    and return it 
    '''
    
    if doc == None:
        doc = FreeCAD.activeDocument()

    obj = doc.addObject("App::DocumentObjectGroupPython", name )
    
    CarpetaProjecte(obj,name,tipus)
    
    return obj

def creaProjecte(name='Projecte'):
    '''
    Crea l'estructura basica de projecte
    '''
    FreeCADGui.activateWorkbench("Survey")

    # setting a new document to hold the tests
    if not FreeCAD.ActiveDocument:
        FreeCAD.newDocument("SurveyProject")
        FreeCAD.setActiveDocument("SurveyProject")
    
    doc = FreeCAD.activeDocument()
    creaCarpetaProjecte('Punts', 'Punts', doc)
    creaCarpetaProjecte('Breaklines', 'Breaklines', doc)
    creaCarpetaProjecte('Surfaces', 'Surfaces', doc)
    creaCarpetaProjecte('Alignment', 'Alignments', doc)
    
    return doc




 
FreeCADGui.addCommand('New project',NewProject())







    
