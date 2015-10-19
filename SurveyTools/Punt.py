import FreeCADGui
class Punt_Gui():
    """My new command"""
 
    def GetResources(self):
        return {'Pixmap'  : ":/icons/Punt.svg", # the name of a svg file available in the resources
                'Accel' : "", # a default shortcut (optional)
                'MenuText': "Punt",
                'ToolTip' : "crea un punt"}
 
    def Activated(self):
        "Do something here"
        from SurveyTools import Tools
        Tools.crearPunt('name', 5, 5, 5, 'Code')
        return
 
    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True
 
FreeCADGui.addCommand('Crear punt',Punt_Gui())