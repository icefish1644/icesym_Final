import os
import logging
import matplotlib.pyplot as plt
import cases.compBiCyl
from numpy import loadtxt, take, array, append, trapz
import numpy as np

from units import UNITS, CONVERSIONS
from utils import PLOT_ARGUMENTS
from utils import dir_size

from GeneralAttributes import GeneralAttributes

COMPONENTS_DICT = {}
COMPONENTS_DICT['Cylinders'] = 'cyl'
COMPONENTS_DICT['Tubes'] = 'tube'
COMPONENTS_DICT['Tanks'] = 'tank'
COMPONENTS_DICT['Junctions'] = 'junc'
COMPONENTS_DICT['Globals'] = 'global'

TANKEXTRA_LINES = {}
TANKEXTRA_LINES['Mass Flow Rate']                   =  0
TANKEXTRA_LINES['Enthalpy Flow Rate']               =  1
TANKEXTRA_LINES['Mass']                             = -2
TANKEXTRA_LINES['Convective Heat-Transfer Rate']    = -1

CYLEXTRA_LINES = {}
CYLEXTRA_LINES['Convective Heat-Transfer Coeff']        = [1,0]
CYLEXTRA_LINES['Radiactive Heat-Transfer Coeff']        = [1,1]
CYLEXTRA_LINES['Convective Heat-Transfer Rate']         = [1,2]
CYLEXTRA_LINES['Radiactive Heat-Transfer Rate']         = [1,3]
CYLEXTRA_LINES['Burned Mass Fraction']                  = [2,0]
CYLEXTRA_LINES['Burned Mass Fraction Rate']             = [2,1]
CYLEXTRA_LINES['Mass Flow Rate trought Intake Port']    = [3,0]
CYLEXTRA_LINES['Mass Flow Rate trought Exhaust Port']   = [3,1]
CYLEXTRA_LINES['Volume']                                = [3,2]
# Line [3,3] is for the variable Vdot, it is not plotted. (See fortran code)
CYLEXTRA_LINES['Mass of Fuel']                          = [3,4]
CYLEXTRA_LINES['Mass of Air']                           = [3,5]
CYLEXTRA_LINES['Mass of Residual Gas']                  = [3,6]
CYLEXTRA_LINES['Total Heat-Transfer Rate']              = [3,7]
CYLEXTRA_LINES['Fuel Chemical Energy Release']          = [3,8]
CYLEXTRA_LINES['Torque']                                = [3,9]

# Required in archive_to_open to verify which txt file to open

LISTNDOFA   = ['Density', 'Velocity', 'Pressure']
LISTNDOFB   = ['Density', 'Pressure','Temperature']

# Only if test file contain cyl_extras
CYLEXTRAS   = ['Convective Heat-Transfer Coeff','Radiactive Heat-Transfer Coeff',\
               'Convective Heat-Transfer Rate','Radiactive Heat-Transfer Rate','Burned Mass Fraction',\
               'Burned Mass Fraction Rate','Mass Flow Rate trought Intake Port','Mass Flow Rate trought Exhaust Port',\
               'Volume','Mass of Fuel','Mass of Air', 'Mass of Residual Gas','Total Heat-Transfer Rate',\
               'Fuel Chemical Energy Release', 'Torque']

# Only if test file contain tank_extras
TANKEXTRAS  = ['Mass Flow Rate','Enthalpy Flow Rate','Mass','Convective Heat-Transfer Rate']

# Finding use case

GLOBALS = ['Power Indicated','Power Effective','Torque Indicated','Torque Effective',\
           'IMEP per Cylinder','IMEP Global','FMEP per Cylinder','FMEP Global', \
           'BMEP per Cylinder','BMEP Global','SFC Indicated','SFC Effective','Mechanical Efficiency',\
           'Volumetric Efficiency per Cylinder','Volumetric Efficiency Global',\
           'Fuel Conversion Efficiency Indicated','Fuel Conversion Efficiency Effective']

# Specify which engine type

engine = "compBiCyl"

class TestPlotPower():
    def __init__(self):
        self.open_archives  = {}
        self.current_run_dir = os.path.dirname(os.path.realpath(__file__)) + "/" + engine
        print(self.current_run_dir)
        self.plot_type = 0
        self.ga = None
        self.run_attributes = {}
        self.run_attributes['rpms_folder_sizes'] = {}
        self.extras_x_var = 1
        self.not_check_cycle = False
        self.normal_x_var = 2
        # self.run_attributes = {
        #     'rpms_folder_sizes': {},
        #     'rpms': [],
        #     'final_times': []
        # }

        self.current_objects = {}
        self.current_objects['Valves']           = []
        self.current_objects['Tubes']            = []
        self.current_objects['Atmospheres']      = []
        self.current_objects['Junctions']        = []
        self.current_objects['Cylinders']        = []
        self.current_objects['Tanks']            = []
        self.open_data()
        self.change_attributes(self.run_attributes, self.current_objects)
        (run_attributes,irpm_missing) = self.load_current_attributes()
        self.run_attributes = run_attributes

        self.set_restrictions()
        return

  # Plot RPM for GLOBALS >> Power Indicated and SFC Indicated
    def open_data(self):
        externalData = __import__('cases.compBiCyl')
        # self.cleanObjects()
        # self.drawGrid( self.view.sceneRect() )

        self.current_configuration = externalData.compBiCyl.Simulator
        self.current_objects['Valves']           = externalData.compBiCyl.Valves
        self.current_objects['Tubes']            = externalData.compBiCyl.Tubes
        self.current_objects['Atmospheres']      = externalData.compBiCyl.Atmospheres
        self.current_objects['Junctions']        = externalData.compBiCyl.Junctions
        self.current_objects['Cylinders']        = externalData.compBiCyl.Cylinders
        self.current_objects['Tanks']            = externalData.compBiCyl.Tanks
        print(self.current_configuration)
        return


    def change_attributes(self, run_attributes, current_objects):
        self.run_attributes = run_attributes
        self.current_objects = current_objects
        # self.set_rpms_and_cycles()
        if self.ga:
            self.ga.change_attributes(self.run_attributes,self.current_objects['Cylinders'],\
                                      self.current_objects['Atmospheres'][0].object['state_ini'][0] )
        # self.choose_component('Cylinders')
        return

    def set_restrictions(self):
       
        self.ga = GeneralAttributes(self.run_attributes, self.read_normal_txt, \
                                        self.read_extras_txt, self.current_objects['Cylinders'], \
                                        self.current_objects['Atmospheres'][0]['state_ini'][0], self.current_run_dir)
        # if self.plot_type in (1,3):
        #     self.ui.cycles.setEnabled(False)
        # if self.plot_type == 2:
        #     self.ui.rpms.setEnabled(False)

        # self.xlabel             = PLOT_ARGUMENTS[self.plot_type]['xlabel']
        # self.xunits             = PLOT_ARGUMENTS[self.plot_type]['xunits']
        # self.not_check_cycle    = PLOT_ARGUMENTS[self.plot_type]['ncheck_cycle']
        # self.normal_x_var       = PLOT_ARGUMENTS[self.plot_type]['normal_x_var']
        # self.extras_x_var       = PLOT_ARGUMENTS[self.plot_type]['extras_x_var']

        # self.ui.title.setText(PLOT_ARGUMENTS[self.plot_type]['title'])
        # self.ui.legend.setText(PLOT_ARGUMENTS[self.plot_type]['legend'])
        return
    
    def load_current_attributes(self):
        # Attributes for getMasses of GeneralAttributes
        for icylinder in self.current_objects['Cylinders']:
            try:
                angleClose  = np.rad2deg(icylinder['intake_valves'][0]['angle_VC'])
                Q_fuel      = icylinder['fuel']['Q_fuel']
            except:
                angleClose  = 220.0
                Q_fuel      = 44300000.0
            icylinder['angleClose']  = angleClose
            icylinder['Q_fuel']      = Q_fuel

        # Attributes for PlotWidgets
        irpm_missing = []
        run_attributes = {}
        run_attributes['rpms']              = []
        run_attributes['final_times']       = []
        run_attributes['rpms_folder_sizes'] = {}

        calculated_rpms = [int(f.replace('RPM_','')) for f in os.listdir(self.current_run_dir) if 'RPM_' in f]

        # First, include the calculated ones
        for irpm in calculated_rpms:
            # This ones are not be changed by current simulation
            if irpm not in self.current_configuration['rpms']:
                self.current_configuration['rpms'].append(irpm)
        # Of the "set" one, check the ones that are not calculated
        for irpm in self.current_configuration['rpms']:
            rpm_folder = os.path.join(self.current_run_dir,"RPM_%s"%irpm)
            if not os.path.isdir(rpm_folder):
                irpm_missing.append(irpm)
                continue
            current_dir_size = dir_size(rpm_folder)
            # check if the size of the calculated ones changed, so run_attributes must change
            if not irpm in self.run_attributes['rpms_folder_sizes'].keys():
                run_attributes['rpms_folder_sizes'][irpm] = current_dir_size
            else:
                old_dir_size = self.run_attributes['rpms_folder_sizes'][irpm]
                run_attributes['rpms_folder_sizes'][irpm] = current_dir_size if \
                current_dir_size > old_dir_size else old_dir_size

            run_attributes['rpms'].append(irpm)
        
        # Order the rpms, because maybe the user simulates 1000-3000 and then 4000
        # If the list is not ordered, we can get [4000,1000,2000,3000]
        list.sort(run_attributes['rpms'])
        
        for irpm in run_attributes['rpms']:
            final_time = (60.0/irpm)*self.current_configuration['ncycles']*(self.current_configuration['nstroke'])/2.0
            run_attributes['final_times'].append(final_time)

        run_attributes['nstroke'] = self.current_configuration['nstroke']
        run_attributes['ncycles'] = self.current_configuration['ncycles']
        return (run_attributes,irpm_missing)
    
    # REQUIRED TO READ TXT FILES 
    def get_open_archives(self):
        return self.open_archives

    def set_open_archives(self,archive,data):
        self.open_archives[archive] = data
        return
    
    # Choose which Cylinder from here
    def archive_to_open(self, variable, rpm_folder, component):
        if variable in LISTNDOFA or variable in LISTNDOFB:
            # archive = os.path.join(rpm_folder,COMPONENTS_DICT[component]+"_"+str(self.current_index_element)+".txt")
            archive = os.path.join(rpm_folder,COMPONENTS_DICT[component]+"_0.txt")
            extras = False
        elif variable in CYLEXTRAS_DICT[self.plot_type] or variable in TANKEXTRAS:
            # archive = os.path.join(rpm_folder,COMPONENTS_DICT[component]+"_extras_"+str(self.current_index_element)+".txt")
            archive = os.path.join(rpm_folder,COMPONENTS_DICT[component]+"_extras_0.txt")
            extras = True
        return (archive,extras)

    def loadextratxt(self, archive, offset):
        with open(archive, "r") as f:
            all_data = [list(map(float,x.split())) for x in f.readlines()]
        A = array([])
        A = append(A,all_data)
        return A

    def read_extras_txt(self, archive, icycle, variable, component, unit):
        offset = 4 if component=='Cylinders' else 2
        variable_line = CYLEXTRA_LINES[variable][0] if component=='Cylinders' else 1
        variable_col = CYLEXTRA_LINES[variable][1] if component=='Cylinders' else TANKEXTRA_LINES[variable]
        scale, operation = CONVERSIONS[unit]
        
        open_archives = self.get_open_archives()
        if archive not in open_archives.keys():
            A = self.loadextratxt(archive, offset)
            self.set_open_archives(archive,A)
        else:
            A = open_archives[archive]

        # The cylinder extras repeats a pattern every four lines.
        # First line: cycle, angle, time
        # Second, third, fourth line: several variables 
        # The tank extras repeats a pattern every 2 lines.
        # First line: cycle, angle, time, ntubes
        # Second line: Mass Flow Rate (tubes), Enthalpy Flow Rate (tubes), luego dos mas

        if component=='Tanks':
            ntubes = A[0][3]
            TANKEXTRA_LINES['Enthalpy Flow Rate'] = int(ntubes)
            variable_col = TANKEXTRA_LINES[variable]
        ndata = A.shape[0]
        print(ndata)
        data = [[ A[i][self.extras_x_var], operation(A[i+variable_line][variable_col], scale) ] \
                for i in range(0,ndata,offset) if (int(A[i][0])==int(icycle) or self.not_check_cycle)]
        
        try:
            assert(len(data) != 0)
        except:
            handle_exception('Cannot find data in %s archive for %s cycle'%(archive,icycle))
        return data
    
    def read_normal_txt(self, archive, node, icycle, variable_index, unit):
        open_archives = self.get_open_archives()
        # Node, cycle, angle, time .. variables
        if archive not in open_archives.keys():
            A = loadtxt(archive)
            self.set_open_archives(archive,A)
        else:
            A = open_archives[archive]


        scale, operation = CONVERSIONS[unit]
        A_node_filtered = A[A[:,0] == node]
        A_node_and_cycle_filtered = A_node_filtered if self.not_check_cycle \
        else A_node_filtered[A_node_filtered[:,1] == int(icycle)]
        data = take(A_node_and_cycle_filtered, [self.normal_x_var,4+variable_index], axis=1)
        for idata in data:
            idata[1] = operation(idata[1], scale)

        try:
            assert(len(data) != 0)
        except:
            handle_exception('Cannot find data in %s archive for %s cycle'%(archive,icycle))
        return data

    # REQUIRED TO READ TXT FILES

    def trapz_data(self, data):
        value = (data[0][1]+data[-1][1])/2.0
        y = [el[1] for el in data]
        x = [el[0] for el in data]
        y.insert(0,value)
        x.insert(0,0.0)
        max_angle = 720.0 if max(x)>370.0 else 360.0
#        max_angle = 720.0 if x[-1]>370.0 else 360.0 # bug gui vieja
        x.append(max_angle)
        y.append(value)
        res = trapz(y,x)
        res = res/max_angle
        return res

    def plot_rpm(self, plot_attributes):
        datas = []
        legends = []
        if plot_attributes['component']=='Globals':
            for icycle in plot_attributes['selected_cycles']:
                [data,legend] = self.ga.return_calculated_variable(plot_attributes['variable'],int(icycle),\
                                                                plot_attributes['label'],plot_attributes['units'])
                datas.append(data)
                legends.append(legend)
            # flat the lists
            datas = [y for x in datas for y in x]
            legends = [y for x in legends for y in x]
        else:
            # plot_attributes['node'] = int(self.ui.node.currentText())
            for icycle in plot_attributes['selected_cycles']:
                data_icycle = []
                for irpm in plot_attributes['selected_rpms']:
                    rpm_folder = os.path.join(self.current_run_dir,"RPM_%s"%irpm)
                    (archive, extras) = self.archive_to_open(plot_attributes['variable'],rpm_folder,plot_attributes['component'])
                    try:
                        if extras:
                            data = self.read_extras_txt(archive,icycle,plot_attributes['variable'],plot_attributes['component'],plot_attributes['units'])
                        else:
                            data = self.read_normal_txt(archive,plot_attributes['node'],icycle,plot_attributes['variable_index'],plot_attributes['units'])
                        res = self.trapz_data(data)
                        data = [irpm,res]
                        data_icycle.append(data)
                        # from exception_handling import CURRENT_EXCEPTION
                        # assert(not CURRENT_EXCEPTION)
                    except:
                        handle_exception('Error opening archive %s. Cannot plot this selections'%archive)
                        return
                datas.append(data_icycle)
                legends.append(plot_attributes['label']+"_Cycle_"+str(icycle))
                
        return (datas,legends)


class TestPlotClass():
    def __init__(self):
        self.open_archives  = {}
        self.current_run_dir = os.path.dirname(os.path.realpath(__file__)) + "/" + engine
        self.plot_type = 0
        self.not_check_cycle    = PLOT_ARGUMENTS[self.plot_type]['ncheck_cycle']
        self.normal_x_var       = PLOT_ARGUMENTS[self.plot_type]['normal_x_var']
       
    def get_open_archives(self):
        return self.open_archives

    def set_open_archives(self,archive,data):
        self.open_archives[archive] = data
        return
    
    # Choose which Cylinder from here

    def archive_to_open(self, variable, rpm_folder, component):
        if variable in LISTNDOFA or variable in LISTNDOFB:
            # archive = os.path.join(rpm_folder,COMPONENTS_DICT[component]+"_"+str(self.current_index_element)+".txt")
            archive = os.path.join(rpm_folder,COMPONENTS_DICT[component]+"_0.txt")
            extras = False
        elif variable in CYLEXTRAS_DICT[self.plot_type] or variable in TANKEXTRAS:
            # archive = os.path.join(rpm_folder,COMPONENTS_DICT[component]+"_extras_"+str(self.current_index_element)+".txt")
            archive = os.path.join(rpm_folder,COMPONENTS_DICT[component]+"_extras_0.txt")
            extras = True
        return (archive,extras)

    def loadextratxt(self, archive, offset):
        with open(archive, "r") as f:
            all_data = [list(map(float,x.split())) for x in f.readlines()]
        A = array([])
        A = append(A,all_data)
        return A

    def read_extras_txt(self, archive, icycle, variable, component, unit):
        offset = 4 if component=='Cylinders' else 2
        variable_line = CYLEXTRA_LINES[variable][0] if component=='Cylinders' else 1
        variable_col = CYLEXTRA_LINES[variable][1] if component=='Cylinders' else TANKEXTRA_LINES[variable]
        scale, operation = CONVERSIONS[unit]
        
        open_archives = self.get_open_archives()
        if archive not in open_archives.keys():
            A = self.loadextratxt(archive, offset)
            self.set_open_archives(archive,A)
        else:
            A = open_archives[archive]

        # The cylinder extras repeats a pattern every four lines.
        # First line: cycle, angle, time
        # Second, third, fourth line: several variables 
        # The tank extras repeats a pattern every 2 lines.
        # First line: cycle, angle, time, ntubes
        # Second line: Mass Flow Rate (tubes), Enthalpy Flow Rate (tubes), luego dos mas

        if component=='Tanks':
            ntubes = A[0][3]
            TANKEXTRA_LINES['Enthalpy Flow Rate'] = int(ntubes)
            variable_col = TANKEXTRA_LINES[variable]
        ndata = A.shape[0]
        data = [[ A[i][self.extras_x_var], operation(A[i+variable_line][variable_col], scale) ] \
                for i in range(0,ndata,offset) if (int(A[i][0])==int(icycle) or self.not_check_cycle)]
        
        try:
            assert(len(data) != 0)
        except:
            handle_exception('Cannot find data in %s archive for %s cycle'%(archive,icycle))
        return data
    
    def read_normal_txt(self, archive, node, icycle, variable_index, unit):
        open_archives = self.get_open_archives()
        # Node, cycle, angle, time .. variables
        if archive not in open_archives.keys():
            A = loadtxt(archive)
            self.set_open_archives(archive,A)
        else:
            A = open_archives[archive]


        scale, operation = CONVERSIONS[unit]
        A_node_filtered = A[A[:,0] == node]
        A_node_and_cycle_filtered = A_node_filtered if self.not_check_cycle \
        else A_node_filtered[A_node_filtered[:,1] == int(icycle)]
        data = take(A_node_and_cycle_filtered, [self.normal_x_var,4+variable_index], axis=1)
        for idata in data:
            idata[1] = operation(idata[1], scale)

        try:
            assert(len(data) != 0)
        except:
            handle_exception('Cannot find data in %s archive for %s cycle'%(archive,icycle))
        return data

    def plot_angle_or_time(self, plot_attributes):
        datas = []
        legends = []
        
        for irpm in plot_attributes['selected_rpms']:
            rpm_folder = os.path.join(self.current_run_dir,"RPM_%s"%irpm) #retrieve rpm folders
            for icycle in plot_attributes['selected_cycles']: 
                (archive, extras) = self.archive_to_open(plot_attributes['variable'],rpm_folder,plot_attributes['component'])
                try:
                    if extras:
                        data = self.read_extras_txt(archive,icycle,plot_attributes['variable'],plot_attributes['component'],plot_attributes['units'])
                    else:
                        data = self.read_normal_txt(archive,plot_attributes['node'],icycle,plot_attributes['variable_index'],plot_attributes['units'])
                    datas.append(data)
                    legends.append(plot_attributes['label']+"_RPM_"+str(irpm)+"_Cycle_"+str(icycle))
                    # from exception_handling import CURRENT_EXCEPTION
                    # assert(not CURRENT_EXCEPTION)
                except Exception as e:
                    # handle_exception('Error opening archive %s. Cannot plot this selections'%archive)
                    logging.exception('')
                    return
        return (datas,legends)

   











# Able to change between Density [0], Pressure [1] and Temperature [2] using variable index

plotAttributes = {
    'component': 'Cylinders',
    'variable': 'Temperature',
    'selected_cycles': [1, 2],
    'label': 'WTF IS LABEL', # might not be required if only for legend purposes
    'selected_rpms': [1000],
    'variable_index': 2,
    'title': 'WTF IS TITLE',
    'figure_number': 0,
    'units': 'C',
    'node': 0
}

plotAttributes2 = {
    'component': 'Cylinders',
    'variable': 'Pressure',
    'selected_cycles': [1, 2],
    'label': 'WTF IS LABEL',
    'selected_rpms': [1000],
    'variable_index': 1,
    'title': 'WTF IS TITLE',
    'figure_number': 0,
    'units': 'MPa',
    'node': 0
}

plotAttributes_power = {
    'component': 'Globals',
    'variable': 'Power Indicated',
    'selected_cycles': [1, 2],
    'label': 'WTF IS LABEL',
    'selected_rpms': [1000, 1200, 1400, 1600, 1800],
    'variable_index': 0,
    'title': 'WTF IS TITLE',
    'figure_number': 0,
    'units': 'W',
    'node': 0
}

plotAttributes_power2 = {
    'component': 'Globals',
    'variable': 'Power Indicated',
    'selected_cycles': [1, 2],
    'label': 'UNKNOWN LABEL',
    'selected_rpms': [1000, 2000, 3000, 4000, 5000, 6000],
    'variable_index': 0,
    'title': 'UNKNOWN TITLE',
    'figure_number': 0,
    'units': 'W',
    'node': 0
}

# Plotting SFC Indicated for multicyl4TSI

plotAttributes_SFC = {
    'component': 'Globals',
    'variable': 'SFC Indicated',
    'selected_cycles': [5],
    'label': 'UNKNOWN LABEL',
    'selected_rpms': [1000, 2000, 3000, 4000, 5000, 6000],
    'variable_index': 10,
    'title': 'UNKNOWN TITLE',
    'figure_number': 0,
    'units': 'g/(kW.h)',
    'node': 0
}

plotAttributes_power = {
    'component': 'Globals',
    'variable': 'Power Indicated',
    'selected_cycles': [5],
    'label': 'UNKNOWN LABEL',
    'selected_rpms': [1000, 2000, 3000, 4000, 5000, 6000],
    'variable_index': 0,
    'title': 'UNKNOWN TITLE',
    'figure_number': 1,
    'units': 'W',
    'node': 0
}

plotAttributes_IMEP = {
    'component': 'Globals',
    'variable': 'IMEP Global',
    'selected_cycles': [1,2],
    'label': 'UNKNOWN LABEL',
    'selected_rpms': [1000, 2000, 3000, 4000, 5000, 6000],
    'variable_index': 5,
    'title': 'UNKNOWN TITLE',
    'figure_number': 1,
    'units': 'Pa',
    'node': 0
}

plotAttributes_FMEP = {
    'component': 'Globals',
    'variable': 'FMEP Global',
    'selected_cycles': [1,2],
    'label': 'UNKNOWN LABEL',
    'selected_rpms': [1000, 2000, 3000, 4000, 5000, 6000],
    'variable_index': 7,
    'title': 'UNKNOWN TITLE',
    'figure_number': 1,
    'units': 'Pa',
    'node': 0
}

plotAttributes_BMEP = {
    'component': 'Globals',
    'variable': 'BMEP Global',
    'selected_cycles': [1,2],
    'label': 'UNKNOWN LABEL',
    'selected_rpms': [1000, 2000, 3000, 4000, 5000, 6000],
    'variable_index': 9,
    'title': 'UNKNOWN TITLE',
    'figure_number': 1,
    'units': 'Pa',
    'node': 0
}

plotAttributes_torque = {
    'component': 'Globals',
    'variable': 'Torque Indicated',
    'selected_cycles': [1,2],
    'label': 'UNKNOWN LABEL',
    'selected_rpms': [1000, 2000, 3000, 4000, 5000, 6000],
    'variable_index': 2,
    'title': 'UNKNOWN TITLE',
    'figure_number': 1,
    'units': 'N.m',
    'node': 0
}

# compBiCyl

plotAttributes_pressure = {
    'component': 'Cylinders',
    'variable': 'Pressure',
    'selected_cycles': [3],
    'label': 'WTF IS LABEL',
    'selected_rpms': [1000, 1200, 1400, 1600, 1800, 2000],
    'variable_index': 1,
    'title': 'WTF IS TITLE',
    'figure_number': 0,
    'units': 'Pa',
    'node': 0
}

plotAttributes_density = {
    'component': 'Cylinders',
    'variable': 'Density',
    'selected_cycles': [3],
    'label': 'WTF IS LABEL',
    'selected_rpms': [1000, 1200, 1400, 1600, 1800, 2000],
    'variable_index': 0,
    'title': 'WTF IS TITLE',
    'figure_number': 0,
    'units': 'kg/m^3',
    'node': 0
}

plotAttributes_temp = {
    'component': 'Cylinders',
    'variable': 'Temperature',
    'selected_cycles': [3],
    'label': 'WTF IS LABEL',
    'selected_rpms': [1000, 1200, 1400, 1600, 1800, 2000],
    'variable_index': 2,
    'title': 'WTF IS TITLE',
    'figure_number': 0,
    'units': 'K',
    'node': 0
}

# 2strokes20cyl

# plotAttributes_pressure = {
#     'component': 'Cylinders',
#     'variable': 'Pressure',
#     'selected_cycles': [20],
#     'label': 'WTF IS LABEL',
#     'selected_rpms': [600],
#     'variable_index': 1,
#     'title': 'WTF IS TITLE',
#     'figure_number': 0,
#     'units': 'Pa',
#     'node': 0
# }

# plotAttributes_density = {
#     'component': 'Cylinders',
#     'variable': 'Density',
#     'selected_cycles': [20],
#     'label': 'WTF IS LABEL',
#     'selected_rpms': [600],
#     'variable_index': 0,
#     'title': 'WTF IS TITLE',
#     'figure_number': 0,
#     'units': 'kg/m^3',
#     'node': 0
# }

# plotAttributes_temp = {
#     'component': 'Cylinders',
#     'variable': 'Temperature',
#     'selected_cycles': [20],
#     'label': 'WTF IS LABEL',
#     'selected_rpms': [600],
#     'variable_index': 2,
#     'title': 'WTF IS TITLE',
#     'figure_number': 0,
#     'units': 'K',
#     'node': 0
# }




testPlotObj = TestPlotClass()
testPlotPower = TestPlotPower()
# plotData, legends = testPlotObj.plot_angle_or_time(plotAttributes)
# plotData, legends = testPlotObj.plot_angle_or_time(plotAttributes2)
# plotData, legends = testPlotPower.plot_rpm(plotAttributes_SFC)
# plotData2, legends2 = testPlotPower.plot_rpm(plotAttributes_power)

# plotData, legends = testPlotObj.plot_angle_or_time(plotAttributes_pressure)
# plotData2, legends2 = testPlotObj.plot_angle_or_time(plotAttributes_density)
# plotData3, legends3 = testPlotObj.plot_angle_or_time(plotAttributes_temp)

plotData, legends = testPlotPower.plot_rpm(plotAttributes_IMEP)
plotData2, legends2 = testPlotPower.plot_rpm(plotAttributes_FMEP)
plotData3, legends3 = testPlotPower.plot_rpm(plotAttributes_BMEP)
plotData4, legends4 = testPlotPower.plot_rpm(plotAttributes_torque)


x = plotData[0] # Indexing to retrieve first cycle data 
y = plotData2[0]
z = plotData3[0]
a = plotData4[0]


# For plotting Pressure, Temperature, Density
# xaxis = x[:,0]
# yaxis = x[:,1]
print(x)
print(y)
print(z)
# For separating x and y - axis

xaxis = [i[0] for i in x]
yaxis =  [i[1] for i in x]

xaxis2 = [i[0] for i in y]
yaxis2 =  [i[1] for i in y]

xaxis3 = [i[0] for i in z]
yaxis3 =  [i[1] for i in z]

xaxis4 = [i[0] for i in a]
yaxis4 =  [i[1] for i in a]


# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# print(x)
# print(y)
# plot1 = plt.figure(1)
# plt.plot(xaxis, yaxis, label = 'SFC Indicated')
# plt.xlabel('Speed (rpm)')
# plt.ylabel('SFC Indicated (g/(kW.h)')
# plt.grid()

# Power Plotting

# plot1 = plt.figure(1)
# plt.plot(xaxis, yaxis, label = 'Power Indicated')
# plt.xlabel('Speed (rpm)')
# plt.ylabel('Power Indicated (W)')
# plt.grid()

# plot2 = plt.figure(2)
# plt.plot(xaxis2, yaxis2, label = 'Power Indicated')
# plt.xlabel('Speed (rpm)')
# plt.ylabel('Power Indicated (W)')
# plt.grid()

# plt.show(block=False)

# compBiCyl

plot1 = plt.figure(1)
plt.plot(xaxis, yaxis, label = 'Pressure')
# plt.xlabel('Crank Angle (Deg)')
plt.title("Indicated Mean Effective Pressure")
plt.xlabel('Speed (rpm)')
plt.ylabel('Pressure (Pa)')
plt.grid()

plot2 = plt.figure(2)
plt.plot(xaxis2, yaxis2, label = 'Pressure')
# plt.xlabel('Crank Angle (Deg)')
plt.title("Friction Mean Effective Pressure")
plt.xlabel('Speed (rpm)')
plt.ylabel('Pressure (Pa)')
plt.grid()

plot3 = plt.figure(3)
plt.plot(xaxis3, yaxis3, label = 'Pressure')
# plt.xlabel('Crank Angle (Deg)')
plt.title("Brake Mean Effective Pressure")
plt.xlabel('Speed (rpm)')
plt.ylabel('Pressure (Pa)')
plt.grid()

plot3 = plt.figure(4)
plt.plot(xaxis4, yaxis4, label = 'Torque')
# plt.xlabel('Crank Angle (Deg)')
plt.title("Torque Indicated")
plt.xlabel('Speed (rpm)')
plt.ylabel('Torque Indicated (N.m)')
plt.grid()

# plot2 = plt.figure(2)
# plt.plot(xaxis2, yaxis2, label = 'Density')
# # plt.xlabel('Crank Angle (Deg)')
# plt.xlabel('Speed (rpm)')
# plt.ylabel('Density (kg/m^2)')
# plt.grid()

# plot2 = plt.figure(3)
# plt.plot(xaxis3, yaxis3, label = 'Temperature')
# # plt.xlabel('Crank Angle (Deg)')
# plt.xlabel('Speed (rpm)')
# plt.ylabel('Temperature (K)')
# plt.grid()

plt.show(block=False)
