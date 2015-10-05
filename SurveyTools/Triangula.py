'''
Created on 4 oct. 2015

@author: albert
'''
import FreeCADGui
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
        import Base
        Base.crearPunt('name', 5, 5, 5, 'Code')
        return
 
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
 
FreeCADGui.addCommand('Triangula',Triangula())