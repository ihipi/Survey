'''
Created on 4 oct. 2015

@author: albert
'''
import FreeCADGui, icons_rc
import easygui
import FreeCAD
class Triangula():
    """My new command"""
 
    def GetResources(self):
        return {'Pixmap'  : ":/icons/Triangula.svg", # the name of a svg file available in the resources
                'Accel' : "", # a default shortcut (optional)
                'MenuText': "Triangula",
                'ToolTip' : "crea una malla de triangles"}
 
    def Activated(self):
        "Do something here"
        import numpy, scipy, FreeCADGui, easygui, Draft
        from SurveyTools import Tools
        from scipy.spatial import Delaunay
        import matplotlib.pyplot as plt
        
        #aconsegueix la seleccio de freecad
        
        
        
        sel = FreeCADGui.Selection.getSelection() #comprova si la seleccio es un grup
        if sel[0].InList[0].Tipus == "Punts":
            #grup_llista=[]
            #for i in range(len(sel)-1):
            #    grup_llista.append(sel[i].OutList)    #llista d'objectes del grup
            #print grup_llista
            #comprova que el primer objecte sigui un Punt (Survey)
            if sel[0][0].Tipus == "Punt" :
                tri_grp  = Tools.creaSuperficie(easygui.enterbox('tria un nom de superficie'))   
 
                llistaPunts_z=[]
                llistaPunts = []
                #agrega els punts del grup a la llista
                for p in grup_llista:
                    llistaPunts_z.append([p.X,p.Y,p.Z])
                    llistaPunts.append([p.X,p.Y])
                    print (p.Label,p.Codi,p.X,p.Y,p.Z)
                points = numpy.array(llistaPunts)
                tri = Delaunay(points)
                pointsZ = numpy.array(llistaPunts_z)
                triZ = Delaunay(pointsZ)

                print llistaPunts,llistaPunts_z
                for t in points[tri.simplices]:
                    triangle =[]
                    print 't',t
                    for p in t:
                        for pun in llistaPunts_z:
                            if pun[0]== p[0] and pun[1]== p[1]:
                                
                                print 'for t in pointZ(tri.simplices)/forp in t', p
                                x,y,z = pun
                                triangle.append(FreeCAD.Vector(x,y,z))
                        print 'p',p
                    Draft.makeWire(triangle,closed=True,face=True,support=None)   # create the wire open
                    
                        
                    # create the wire open
                    
                    
                return
        
            else:   
                easygui.msgbox('Necessites triar un grup de punts', 'Instruccions')

        else:   
            easygui.msgbox('Necessites triar un grup de punts', 'Instruccions')

        
        return
 
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
 
FreeCADGui.addCommand('Triangula',Triangula())