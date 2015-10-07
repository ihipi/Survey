'''
Created on 4 oct. 2015

@author: albert
'''
import FreeCADGui
import easygui
class Triangula():
    """My new command"""
 
    def GetResources(self):
        return {'Pixmap'  : """
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
             "..####..........",
             "....####........",
             ".......####.....",
             "..........####..",
             "..........####..",
             "..........####..",
             "..############..",
             "..############..",
             "..############..",
             "................",
             "................"};
             """, # the name of a svg file available in the resources
                'Accel' : "", # a default shortcut (optional)
                'MenuText': "Triangula",
                'ToolTip' : "crea una malla de triangles"}
 
    def Activated(self):
        "Do something here"
        import Base, numpy, scipy, FreeCADGui, easygui
        from scipy.spatial import Delaunay
        
        sel = FreeCADGui.Selection.getSelection()
        
        if str(type(sel[0])) == "<type 'App.DocumentObjectGroup'>":
            grup_llista = sel[0].OutList
            if grup_llista[1].Tipus == "Punt" : 
                for p in grup_llista:
                    print (p.Label,p.Codi,p.X,p.Y,p.Z)
                    return
        else:   
            easygui.msgbox('Necessites triar un grup de punts', 'Instruccions')

        
        return
 
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
 
FreeCADGui.addCommand('Triangula',Triangula())