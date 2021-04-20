import sys
#Trying to retrieve Current Configuration and Current Objects



# Don't think it is necessary
class ICESymMainWindow():
    def __init__(self, case_name = None, case_dir = None, case_type = None):
       
        # array of ints. Every int represents the number of objects in scene 
        # (in the same order as the tree)
        self.number_of_objects = [0, 0, 0, 0, 0, 0]
        # dictionary with objects
        self.objects = {}
        self.objects['Valves']           = []
        self.objects['Tubes']            = []
        self.objects['Atmospheres']      = []
        self.objects['Junctions']        = []
        self.objects['Cylinders']        = []
        self.objects['Tanks']            = []
        
        self.configure_default = {}
        # self.configure_default['Valves'] = configure_default_valve
        # self.configure_default['Tubes']  = configure_default_tube

        
        
        # widgets de cada tab
        self.cw     = None
        self.ppw    = None
        self.ltw    = None
        
        self.current_tab_widget_index = 0
        
        self.case_name  = case_name
        self.case_dir   = case_dir
    
        self.open_data()
       
        return

    def open_data(self):
        externalData = __import__('cases.compBiCyl')
        self.cleanObjects()
        # self.drawGrid( self.view.sceneRect() )

        self.current_configuration = externalData.compBiCyl.Simulator
        self.objects['Valves']           = externalData.compBiCyl.Valves
        self.objects['Tubes']            = externalData.compBiCyl.Tubes
        self.objects['Atmospheres']      = externalData.compBiCyl.Atmospheres
        self.objects['Junctions']        = externalData.compBiCyl.Junctions
        self.objects['Cylinders']        = externalData.compBiCyl.Cylinders
        self.objects['Tanks']            = externalData.compBiCyl.Tanks


        # self.drawObjects('Cylinders',   externalData.Cylinders)
        # self.drawObjects('Tanks',       externalData.Tanks)
        # self.drawObjects('Junctions',   externalData.Junctions)
        # self.drawObjects('Tubes',       externalData.Tubes)
        # self.drawObjects('Valves',      externalData.Valves)
        # self.drawObjects('Atmospheres', externalData.Atmospheres)
        
        # self.drawAllConnections()
        # self.set_configuration_run_and_postProcess_widgets()
        
  
        return

    def cleanObjects(self):
        for ikey in self.objects.keys():
            self.objects[ikey] = []
        # self.scene.clear()
        # self.scene_items = []
        # self.scene_connections = []
        self.number_of_objects = [0, 0, 0, 0, 0, 0]        
        # for itype in TREE_POSITION.keys():
        #     # tree_item = self.ui.componentsTreeWidget.topLevelItem(TREE_POSITION[itype])
        #     while tree_item.childCount():
        #         it = tree_item.child(0)
        #         tree_item.removeChild(it)
        #         del it
        return



###################################################################################################

TestObject = ICESymMainWindow()
TestObject.open_data()