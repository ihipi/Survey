import FreeCADGui
class Codis():
    """My new command"""
 
    def GetResources(self):
        return {'Pixmap'  : ":/icons/Punt.svg", # the name of a svg file available in the resources
                'Accel' : "", # a default shortcut (optional)
                'MenuText': "Codis",
                'ToolTip' : "crea un punt"}
 
    def Activated(self):
        "Do something here"
        from GUI import Codes_Gui
        Codes_Gui.Codes_Gui()
        return
 
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
 
FreeCADGui.addCommand('Codis',Codis())