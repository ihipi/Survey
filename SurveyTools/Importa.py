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
        
        def index_codis(llista, codi):
            ind =[]
            for i,c in enumerate(llista):
                c_clean = c[0].split('_')
                if c_clean == codi:
                    ind.append(i)
            return ind

      
        fitxer = easygui.fileopenbox('Tria un fitxer de punts (nom, x, y, z, codi)',default="/home/albert/.FreeCAD/Mod/Survey/puntos.PUN")                     # path and name of file.txt
        
        grup =  easygui.enterbox('tria un nom de grup')
        doc = FreeCAD.activeDocument()
        grp = doc.addObject("App::DocumentObjectGroup", grup )
        
        grp_punts  = grp.newObject("App::DocumentObjectGroup","Punts")

        
        file = open(fitxer, "r")                                  # open the file read
        X=Y=Z = 0.0
        codis = []
        code_list = []
        linies = []
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
            
            cs = C.split(',')
            
            for codi in cs:
                codi_clean = codi.split(' ')
                if len(codi_clean) > 1:
                    print 'inici d linia:-----'+codi_clean[0]+'<-----\n'
                    if   'I' in codi_clean[1]:
                        print 'inici d linia amb "I":\n'
                        ind = index_codis(linies,codi_clean[0] )
                        print ind
                        if ind:
                            print "Ja existeix: ",ind[-1]
                            num = int(linies[ind[-1]][0].split('_')[-1]) + 1
    
                            linies.append([codi_clean[0]+'_'+str(num),[FreeCAD.Vector(float(X),float(Y),float(Z))]])
                        
                        else:
                            print 'linia nova' + codi_clean[0]
                            linies.append([codi_clean[0]+'_0',[FreeCAD.Vector(float(X),float(Y),float(Z))]])
                        
                else:
                    
                    for i in range(len(linies)-1, -1, -1):
                            
                        lin_clean = linies[i][0].split('_')
                        if lin_clean[0] == codi_clean[0]:
    
                            print 'punt de linia'
                            linies[i][1].append(FreeCAD.Vector(float(X),float(Y),float(Z)))
                    else:
                        print 'punt sense linia'
                            
                    # separate the coordinates

        print linies
            
        if easygui.ynbox("Voleu crear les linies de rotura?"):
            grp_linies = grp.newObject("App::DocumentObjectGroup","Linies")

            for k in linies:
                l=[]
                for punt in k[1]:
                    l.append(punt)
              
                wire=Draft.makeWire(l,closed=False,face=False,support=None)   # create the wire open
                wire.Label = k[0]
                grp_linies.addObject(wire)
        #print codis, code_list
        file.close()
        return
 
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
 
FreeCADGui.addCommand('Importa',Importa())