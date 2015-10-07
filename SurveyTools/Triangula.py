'''
Created on 4 oct. 2015

@author: albert
'''
import FreeCADGui
import easygui
import FreeCAD
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
        import Base, numpy, scipy, FreeCADGui, easygui, Draft
        from scipy.spatial import Delaunay
        import matplotlib.pyplot as plt
        
        sel = FreeCADGui.Selection.getSelection()
        
        if str(type(sel[0])) == "<type 'App.DocumentObjectGroup'>":
            grup_llista = sel[0].OutList
            print grup_llista
            if grup_llista[1].Tipus == "Punt" : 
                llistaPunts=[]
                for p in grup_llista:
                    llistaPunts.append([p.X,p.Y,p.Z])
                    print (p.Label,p.Codi,p.X,p.Y,p.Z)
                
                points = numpy.array(llistaPunts)
                tri = Delaunay(points)
                for t in points[tri.simplices]:
                    triangle =[]
                    print 't',t
                    for p in t:
                        x,y,z = p
                        triangle.append(FreeCAD.Vector(x,y,z))
                        print 'p',p
                    Draft.makeWire(triangle,closed=True,face=True,support=None)   # create the wire open
   
                        
                       # create the wire open
                    
                    
            return
        else:   
            easygui.msgbox('Necessites triar un grup de punts', 'Instruccions')

        
        return
 
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
 
FreeCADGui.addCommand('Triangula',Triangula())