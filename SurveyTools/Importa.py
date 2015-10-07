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
        codis = {}
        linies = []
        for linia in file:
           
            if linia[-1] == '\n':
                linia = linia[:-1]
            coordinates = linia.split('\t')
            N,X,Y,Z,C = coordinates  
            N = str(N)
            C = str(C).strip() 
            
            
                     
            p = Base.crearPunt(str(N),float(X),float(Y),float(Z),C)         # create points (uncomment for use)
            
            grp_punts.addObject(p)
            
            
            codi_l = C.split(' ')
            
            codi_clean = str(codi_l[0])
            codi_base = codi_clean+'_'
            print '#############################'
            print len(codi_l[0]),codi_clean,len(codi_clean)
            if len(codi_l)>1:
                if   'I' in codi_l[1]:
                    print 'inici d linia amb "I":\n'
                    
                     
                    if codi_base in codis.keys():
                        print "Ja existeix: ",codi_base
                        codis[codi_base]= codis[codi_base]+1

                        linies.append([codi_base+str(codis[codi_base]),[FreeCAD.Vector(float(X),float(Y),float(Z))]])
                    
                    else:
                        print 'linia nova' + codi_clean[0]
                        codis[codi_base]= 0

                        linies.append([codi_base+str(codis[codi_base]),[FreeCAD.Vector(float(X),float(Y),float(Z))]])
                else:
                    if codi_base in codis.keys():
                        for lin in linies:
                            lin_code = lin[0]
                            print codi_base , lin_code[:len(codi_base)]
                            if codi_base == lin_code[:len(codi_base)]:
        
                                print 'punt de la linia: '+ lin_code,lin[1]
                                
                                lin[1].append(FreeCAD.Vector(float(X),float(Y),float(Z)))
                            else:
                                print 'punt sense linia',codi_base
                      
            else:
                
                if codi_base in codis.keys():
                    for lin in linies:
                        lin_code = lin[0]
                        print codi_base , lin_code[:len(codi_base)]
                        if codi_base == lin_code[:len(codi_base)]:
    
                            print 'punt de la linia: '+ lin_code,lin[1]
                            
                            lin[1].append(FreeCAD.Vector(float(X),float(Y),float(Z)))
                        else:
                            print 'punt sense linia',codi_base
                            
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