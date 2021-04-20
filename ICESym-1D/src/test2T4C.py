#### ---- ####
# Archivo generado por SimulatorGUI
# CIMEC - Santa Fe - Argentina 
# Adecuado para levantar desde Interfaz Grafica 
# O para correr desde consola mediante $python main.py 
#### ---- ####

Simulator0 = dict()
Simulator0['dtheta_rpm'] = 1.0
Simulator0['filein_state'] = 'None'
Simulator0['Courant'] = 0.8
Simulator0['heat_flow'] = 1.0
Simulator0['R_gas'] = 287.0
Simulator0['rpms'] = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
Simulator0['calc_engine_data'] = 1
Simulator0['filesave_state'] = 'test2T4C'
Simulator0['viscous_flow'] = 1.0
Simulator0['ncycles'] = 2
Simulator0['folder_name'] = 'test2T4C'
Simulator0['ga'] = 1.4
Simulator0['filesave_spd'] = ''
Simulator0['nsave'] = 5
Simulator0['ig_order'] = [0, 4, 2, 5, 1, 3]
Simulator0['get_state'] = 2
Simulator0['final_times'] = [0.600007, 0.300004, 0.200001, 0.150001, 0.120001, 0.100001]
Simulator0['nappend'] = 50.0
Simulator0['engine_type'] = 0
Simulator0['nstroke'] = 2

Simulator = Simulator0


#--------- Inicializacion de Cylinders

Cylinders = []

Cylinders0 = dict()
Cylinders0['crank_radius'] = 2.66 # "Cylinder stroke [m]"
Cylinders0['type_ig'] = 1   # Ignition Type: 0 = by spark, 1 = by compression.
Cylinders0['ndof'] = 3  # Number of degrees of freedom: Always ndof = 3.
Cylinders0['full_implicit'] = 0.0
Cylinders0['model_ht'] = 1  # Heat transfer calculation model. 3 = Taylor.
Cylinders0['factor_ht'] = 1.0
Cylinders0['piston_area'] = 0.754296396 # Calculate pi * bore^2 / 4
Cylinders0['exhaust_valves'] = []
Cylinders0['ownState'] = 1
Cylinders0['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Mass of fuel, air and waste gases in cylinder
Cylinders0['nnod'] = 3
Cylinders0['label'] = 'cyl0'
# Cylinders0['Q_fuel'] = 44300000.0
Cylinders0['twall'] = [450.0]   # Cylinder wall temperature.
Cylinders0['state_ini'] = [[1.1769, 101330.0, 300.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Cylinders0['nve'] = 1   #Number of exhaust valves per cylinder.
Cylinders0['intake_valves'] = []
Cylinders0['head_chamber_area'] = 0.905155675 # Combustion chamber wall surface
Cylinders0['type_temperature'] = 0
Cylinders0['angleClose'] = 220
Cylinders0['rod_length'] = 1.09858 # Connecting rod length.
Cylinders0['species_model'] = 0
Cylinders0['nvi'] = 1            #Number of intake valves per cylinder
Cylinders0['delta_ca'] = 0.0
Cylinders0['Vol_clearance'] = 0.160514273 # Combustion chamber volume.
Cylinders0['extras'] = 1
Cylinders0['histo'] = [0]
# Cylinders0['position'] = (661, 67)
Cylinders0['Bore'] = 0.98
Cylinders0['scavenge'] = 0.0
#--------- Inicializacion de combustion

combustion0 = dict()
combustion0['phi'] = 1.0
combustion0['a_wiebe'] = 6.02
combustion0['dtheta_comb'] = 1.0471975512
combustion0['combustion_model'] = 1
combustion0['m_wiebe'] = 1.64
combustion0['theta_ig_0'] = 5.8643062867
Cylinders0['combustion'] = combustion0


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel0 = dict()
fuel0['y'] = 2.25
fuel0['hvap_fuel'] = 350000.0
fuel0['Q_fuel'] = 44300000.0
Cylinders0['fuel'] = fuel0


#--------- FIN Inicializacion de fuel





#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders0)

Cylinders1 = dict()
Cylinders1['crank_radius'] = 2.66 # "Cylinder stroke [m]"
Cylinders1['type_ig'] = 1   # Ignition Type: 0 = by spark, 1 = by compression.
Cylinders1['ndof'] = 3  # Number of degrees of freedom: Always ndof = 3.
Cylinders1['full_implicit'] = 0.0
Cylinders1['model_ht'] = 1  # Heat transfer calculation model. 3 = Taylor.
Cylinders1['factor_ht'] = 1.0
Cylinders1['piston_area'] = 0.754296396 # Calculate pi * bore^2 / 4
Cylinders1['exhaust_valves'] = []
Cylinders1['ownState'] = 1
Cylinders1['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Mass of fuel, air and waste gases in cylinder
Cylinders1['nnod'] = 3
Cylinders1['label'] = 'cyl1'
# Cylinders1['Q_fuel'] = 44300000.0
Cylinders1['twall'] = [450.0]   # Cylinder wall temperature.
Cylinders1['state_ini'] = [[1.1769, 101330.0, 300.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Cylinders1['nve'] = 1   #Number of exhaust valves per cylinder.
Cylinders1['intake_valves'] = []
Cylinders1['head_chamber_area'] = 0.905155675 # Combustion chamber wall surface
Cylinders1['type_temperature'] = 0
Cylinders1['angleClose'] = 220
Cylinders1['rod_length'] = 1.09858 # Connecting rod length.
Cylinders1['species_model'] = 0
Cylinders1['nvi'] = 1            #Number of intake valves per cylinder
Cylinders1['delta_ca'] = 0.0
Cylinders1['Vol_clearance'] = 0.160514273 # Combustion chamber volume.
Cylinders1['extras'] = 1
Cylinders1['histo'] = [0]
# Cylinders2['position'] = (661, 67)
Cylinders1['Bore'] = 0.98
Cylinders1['scavenge'] = 0.0

#--------- Inicializacion de combustion

combustion1 = dict()
combustion1['phi'] = 1.0
combustion1['a_wiebe'] = 6.02
combustion1['dtheta_comb'] = 1.0471975512
combustion1['combustion_model'] = 1
combustion1['m_wiebe'] = 1.64
combustion1['theta_ig_0'] = 5.8643062867
Cylinders1['combustion'] = combustion1


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel1 = dict()
fuel1['y'] = 2.25
fuel1['hvap_fuel'] = 350000.0
fuel1['Q_fuel'] = 44300000.0
Cylinders1['fuel'] = fuel1


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection1 = dict()
Cylinders1['injection'] = injection1


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders1)

Cylinders2 = dict()
Cylinders2['crank_radius'] = 2.66 # "Cylinder stroke [m]"
Cylinders2['type_ig'] = 1   # Ignition Type: 0 = by spark, 1 = by compression.
Cylinders2['ndof'] = 3  # Number of degrees of freedom: Always ndof = 3.
Cylinders2['full_implicit'] = 0.0
Cylinders2['model_ht'] = 1  # Heat transfer calculation model. 3 = Taylor.
Cylinders2['factor_ht'] = 1.0
Cylinders2['piston_area'] = 0.754296396 # Calculate pi * bore^2 / 4
Cylinders2['exhaust_valves'] = []
Cylinders2['ownState'] = 1
Cylinders2['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Mass of fuel, air and waste gases in cylinder
Cylinders2['nnod'] = 3
Cylinders2['label'] = 'cyl2'
# Cylinders2['Q_fuel'] = 44300000.0
Cylinders2['twall'] = [450.0]   # Cylinder wall temperature.
Cylinders2['state_ini'] = [[1.1769, 101330.0, 300.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Cylinders2['nve'] = 1   #Number of exhaust valves per cylinder.
Cylinders2['intake_valves'] = []
Cylinders2['head_chamber_area'] = 0.905155675 # Combustion chamber wall surface
Cylinders2['type_temperature'] = 0
Cylinders2['angleClose'] = 220
Cylinders2['rod_length'] = 1.09858 # Connecting rod length.
Cylinders2['species_model'] = 0
Cylinders2['nvi'] = 1            #Number of intake valves per cylinder
Cylinders2['delta_ca'] = 0.0
Cylinders2['Vol_clearance'] = 0.160514273 # Combustion chamber volume.
Cylinders2['extras'] = 1
Cylinders2['histo'] = [0]
# Cylinders2['position'] = (661, 67)
Cylinders2['Bore'] = 0.98
Cylinders2['scavenge'] = 0.0
#--------- Inicializacion de combustion

combustion2 = dict()
combustion2['phi'] = 1.0
combustion2['a_wiebe'] = 6.02
combustion2['dtheta_comb'] = 1.0471975512
combustion2['combustion_model'] = 1
combustion2['m_wiebe'] = 1.64
combustion2['theta_ig_0'] = 5.8643062867
Cylinders2['combustion'] = combustion2


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel2 = dict()
fuel2['y'] = 2.25
fuel2['hvap_fuel'] = 350000.0
fuel2['Q_fuel'] = 44300000.0
Cylinders2['fuel'] = fuel2


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection2 = dict()
Cylinders2['injection'] = injection2


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders2)

Cylinders3 = dict()
Cylinders3['crank_radius'] = 2.66 # "Cylinder stroke [m]"
Cylinders3['type_ig'] = 1   # Ignition Type: 0 = by spark, 1 = by compression.
Cylinders3['ndof'] = 3  # Number of degrees of freedom: Always ndof = 3.
Cylinders3['full_implicit'] = 0.0
Cylinders3['model_ht'] = 1  # Heat transfer calculation model. 3 = Taylor.
Cylinders3['factor_ht'] = 1.0
Cylinders3['piston_area'] = 0.754296396 # Calculate pi * bore^2 / 4
Cylinders3['exhaust_valves'] = []
Cylinders3['ownState'] = 1
Cylinders3['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Mass of fuel, air and waste gases in cylinder
Cylinders3['nnod'] = 3
Cylinders3['label'] = 'cyl3'
# Cylinders2['Q_fuel'] = 44300000.0
Cylinders3['twall'] = [450.0]   # Cylinder wall temperature.
Cylinders3['state_ini'] = [[1.1769, 101330.0, 300.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Cylinders3['nve'] = 1   #Number of exhaust valves per cylinder.
Cylinders3['intake_valves'] = []
Cylinders3['head_chamber_area'] = 0.905155675 # Combustion chamber wall surface
Cylinders3['type_temperature'] = 0
Cylinders3['angleClose'] = 220
Cylinders3['rod_length'] = 1.09858 # Connecting rod length.
Cylinders3['species_model'] = 0
Cylinders3['nvi'] = 1            #Number of intake valves per cylinder
Cylinders3['delta_ca'] = 0.0
Cylinders3['Vol_clearance'] = 0.160514273 # Combustion chamber volume.
Cylinders3['extras'] = 1
Cylinders3['histo'] = [0]
# Cylinders2['position'] = (661, 67)
Cylinders3['Bore'] = 0.98
Cylinders3['scavenge'] = 0.0
Cylinders3['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#--------- Inicializacion de combustion

combustion3 = dict()
combustion3['phi'] = 1.0
combustion3['a_wiebe'] = 6.02
combustion3['dtheta_comb'] = 1.0471975512
combustion3['combustion_model'] = 1
combustion3['m_wiebe'] = 1.64
combustion3['theta_ig_0'] = 5.8643062867
Cylinders3['combustion'] = combustion3


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel3 = dict()
fuel3['y'] = 2.25
fuel3['hvap_fuel'] = 350000.0
fuel3['Q_fuel'] = 44300000.0
Cylinders3['fuel'] = fuel3


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection3 = dict()
Cylinders3['injection'] = injection3


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders3)

Cylinders4 = dict()
Cylinders4['crank_radius'] = 2.66 # "Cylinder stroke [m]"
Cylinders4['type_ig'] = 1   # Ignition Type: 0 = by spark, 1 = by compression.
Cylinders4['ndof'] = 3  # Number of degrees of freedom: Always ndof = 3.
Cylinders4['full_implicit'] = 0.0
Cylinders4['model_ht'] = 1  # Heat transfer calculation model. 3 = Taylor.
Cylinders4['factor_ht'] = 1.0
Cylinders4['piston_area'] = 0.754296396 # Calculate pi * bore^2 / 4
Cylinders4['exhaust_valves'] = []
Cylinders4['ownState'] = 1
Cylinders4['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Mass of fuel, air and waste gases in cylinder
Cylinders4['nnod'] = 3
Cylinders4['label'] = 'cyl4'
# Cylinders2['Q_fuel'] = 44300000.0
Cylinders4['twall'] = [450.0]   # Cylinder wall temperature.
Cylinders4['state_ini'] = [[1.1769, 101330.0, 300.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Cylinders4['nve'] = 1   #Number of exhaust valves per cylinder.
Cylinders4['intake_valves'] = []
Cylinders4['head_chamber_area'] = 0.905155675 # Combustion chamber wall surface
Cylinders4['type_temperature'] = 0
Cylinders4['angleClose'] = 220
Cylinders4['rod_length'] = 1.09858 # Connecting rod length.
Cylinders4['species_model'] = 0
Cylinders4['nvi'] = 1            #Number of intake valves per cylinder
Cylinders4['delta_ca'] = 0.0
Cylinders4['Vol_clearance'] = 0.160514273 # Combustion chamber volume.
Cylinders4['extras'] = 1
Cylinders4['histo'] = [0]
# Cylinders2['position'] = (661, 67)
Cylinders4['Bore'] = 0.98
Cylinders4['scavenge'] = 0.0
Cylinders4['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#--------- Inicializacion de combustion

combustion4 = dict()
combustion4['phi'] = 1.0
combustion4['a_wiebe'] = 6.02
combustion4['dtheta_comb'] = 1.0471975512
combustion4['combustion_model'] = 1
combustion4['m_wiebe'] = 1.64
combustion4['theta_ig_0'] = 5.8643062867
Cylinders4['combustion'] = combustion4


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel4 = dict()
fuel4['y'] = 2.25
fuel4['hvap_fuel'] = 350000.0
fuel4['Q_fuel'] = 44300000.0
Cylinders4['fuel'] = fuel4


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection4 = dict()
Cylinders4['injection'] = injection4


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders4)

Cylinders5 = dict()
Cylinders5['crank_radius'] = 2.66 # "Cylinder stroke [m]"
Cylinders5['type_ig'] = 1   # Ignition Type: 0 = by spark, 1 = by compression.
Cylinders5['ndof'] = 3  # Number of degrees of freedom: Always ndof = 3.
Cylinders5['full_implicit'] = 0.0
Cylinders5['model_ht'] = 1  # Heat transfer calculation model. 3 = Taylor.
Cylinders5['factor_ht'] = 1.0
Cylinders5['piston_area'] = 0.754296396 # Calculate pi * bore^2 / 4
Cylinders5['exhaust_valves'] = []
Cylinders5['ownState'] = 1
Cylinders5['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Mass of fuel, air and waste gases in cylinder
Cylinders5['nnod'] = 3
Cylinders5['label'] = 'cyl5'
# Cylinders2['Q_fuel'] = 44300000.0
Cylinders5['twall'] = [450.0]   # Cylinder wall temperature.
Cylinders5['state_ini'] = [[1.1769, 101330.0, 300.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Cylinders5['nve'] = 1   #Number of exhaust valves per cylinder.
Cylinders5['intake_valves'] = []
Cylinders5['head_chamber_area'] = 0.905155675 # Combustion chamber wall surface
Cylinders5['type_temperature'] = 0
Cylinders5['angleClose'] = 220
Cylinders5['rod_length'] = 1.09858 # Connecting rod length.
Cylinders5['species_model'] = 0
Cylinders5['nvi'] = 1            #Number of intake valves per cylinder
Cylinders5['delta_ca'] = 0.0
Cylinders5['Vol_clearance'] = 0.160514273 # Combustion chamber volume.
Cylinders5['extras'] = 1
Cylinders5['histo'] = [0]
# Cylinders2['position'] = (661, 67)
Cylinders5['Bore'] = 0.98
Cylinders5['scavenge'] = 0.0
Cylinders5['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#--------- Inicializacion de combustion

combustion5 = dict()
combustion5['phi'] = 1.0
combustion5['a_wiebe'] = 6.02
combustion5['dtheta_comb'] = 1.0471975512
combustion5['combustion_model'] = 1
combustion5['m_wiebe'] = 1.64
combustion5['theta_ig_0'] = 5.8643062867
Cylinders5['combustion'] = combustion5


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel5 = dict()
fuel5['y'] = 2.25
fuel5['hvap_fuel'] = 350000.0
fuel5['Q_fuel'] = 44300000.0
Cylinders5['fuel'] = fuel5


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection5 = dict()
Cylinders5['injection'] = injection5


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders5)
#--------- FIN Inicializacion de Cylinders


#--------- Inicializacion de Valves

Valves = []

Valves0 = dict()
Valves0['tube'] = 0
Valves0['Lvmax'] = 0.009
Valves0['ncyl'] = 0
Valves0['label'] = 'ivalve0'
Valves0['angle_VC'] = 3.83972435439
Valves0['histo'] = 0
Valves0['Nval'] = 1
Valves0['Dv'] = 0.035
Valves0['position'] = (529, 67)
Valves0['type_dat'] = 0
Valves0['Cd'] = [[0.0, 0.8], [0.009, 0.8]]
Valves0['type'] = 0
Valves0['typeVal'] = 'int'
Valves0['angle_V0'] = 12.3918376892
Valves0['valve_model'] = 1
Cylinders0['intake_valves'].append(Valves0)


Valves.append(Valves0)

Valves1 = dict()
Valves1['tube'] = 1
Valves1['Lvmax'] = 0.009
Valves1['ncyl'] = 1
Valves1['label'] = 'ivalve1'
Valves1['angle_VC'] = 3.83972435439
Valves1['histo'] = 0
Valves1['Nval'] = 1
Valves1['Dv'] = 0.035
Valves1['position'] = (529, 199)
Valves1['type_dat'] = 0
Valves1['Cd'] = [[0.0, 0.8], [0.009, 0.8]]
Valves1['type'] = 0
Valves1['typeVal'] = 'int'
Valves1['angle_V0'] = 12.3918376892
Valves1['valve_model'] = 1
Cylinders1['intake_valves'].append(Valves1)


Valves.append(Valves1)

Valves2 = dict()
Valves2['tube'] = 2
Valves2['Lvmax'] = 0.009
Valves2['ncyl'] = 2
Valves2['label'] = 'ivalve2'
Valves2['angle_VC'] = 3.83972435439
Valves2['histo'] = 0
Valves2['Nval'] = 1
Valves2['Dv'] = 0.035
Valves2['position'] = (529, 331)
Valves2['type_dat'] = 0
Valves2['Cd'] = [[0.0, 0.8], [0.009, 0.8]]
Valves2['type'] = 0
Valves2['typeVal'] = 'int'
Valves2['angle_V0'] = 12.3918376892
Valves2['valve_model'] = 1
Cylinders2['intake_valves'].append(Valves2)


Valves.append(Valves2)

Valves3 = dict()
Valves3['tube'] = 3
Valves3['Lvmax'] = 0.009
Valves3['ncyl'] = 3
Valves3['label'] = 'ivalve3'
Valves3['angle_VC'] = 3.83972435439
Valves3['histo'] = 0
Valves3['Nval'] = 1
Valves3['Dv'] = 0.035
Valves3['position'] = (529, 463)
Valves3['type_dat'] = 0
Valves3['Cd'] = [[0.0, 0.8], [0.009, 0.8]]
Valves3['type'] = 0
Valves3['typeVal'] = 'int'
Valves3['angle_V0'] = 12.3918376892
Valves3['valve_model'] = 1
Cylinders3['intake_valves'].append(Valves3)


Valves.append(Valves3)

Valves4 = dict()
Valves4['tube'] = 3
Valves4['Lvmax'] = 0.009
Valves4['ncyl'] = 3
Valves4['label'] = 'ivalve4'
Valves4['angle_VC'] = 3.83972435439
Valves4['histo'] = 0
Valves4['Nval'] = 1
Valves4['Dv'] = 0.035
Valves4['position'] = (529, 463)
Valves4['type_dat'] = 0
Valves4['Cd'] = [[0.0, 0.8], [0.009, 0.8]]
Valves4['type'] = 0
Valves4['typeVal'] = 'int'
Valves4['angle_V0'] = 12.3918376892
Valves4['valve_model'] = 1
Cylinders4['intake_valves'].append(Valves4)


Valves.append(Valves4)

Valves5 = dict()
Valves5['tube'] = 3
Valves5['Lvmax'] = 0.009
Valves5['ncyl'] = 3
Valves5['label'] = 'ivalve5'
Valves5['angle_VC'] = 3.83972435439
Valves5['histo'] = 0
Valves5['Nval'] = 1
Valves5['Dv'] = 0.035
Valves5['position'] = (529, 463)
Valves5['type_dat'] = 0
Valves5['Cd'] = [[0.0, 0.8], [0.009, 0.8]]
Valves5['type'] = 0
Valves5['typeVal'] = 'int'
Valves5['angle_V0'] = 12.3918376892
Valves5['valve_model'] = 1
Cylinders5['intake_valves'].append(Valves5)


Valves.append(Valves5)

Valves6 = dict()
Valves6['tube'] = 4
Valves6['Lvmax'] = 0.009
Valves6['ncyl'] = 0
Valves6['label'] = 'evalve0'
Valves6['angle_VC'] = 0.349065850399
Valves6['histo'] = 0
Valves6['Nval'] = 1
Valves6['Dv'] = 0.035
Valves6['position'] = (793, 67)
Valves6['type_dat'] = 0
Valves6['Cd'] = [[0.0, 0.75], [0.009, 0.75]]
Valves6['type'] = 1
Valves6['typeVal'] = 'exh'
Valves6['angle_V0'] = 8.55211333477
Valves6['valve_model'] = 1
Cylinders0['exhaust_valves'].append(Valves6)


Valves.append(Valves6)

Valves7 = dict()
Valves7['tube'] = 5
Valves7['Lvmax'] = 0.009
Valves7['ncyl'] = 1
Valves7['label'] = 'evalve1'
Valves7['angle_VC'] = 0.349065850399
Valves7['histo'] = 0
Valves7['Nval'] = 1
Valves7['Dv'] = 0.035
Valves7['position'] = (793, 199)
Valves7['type_dat'] = 0
Valves7['Cd'] = [[0.0, 0.75], [0.009, 0.75]]
Valves7['type'] = 1
Valves7['typeVal'] = 'exh'
Valves7['angle_V0'] = 8.55211333477
Valves7['valve_model'] = 1
Cylinders1['exhaust_valves'].append(Valves7)


Valves.append(Valves7)

Valves8 = dict()
Valves8['tube'] = 6
Valves8['Lvmax'] = 0.009
Valves8['ncyl'] = 2
Valves8['label'] = 'evalve2'
Valves8['angle_VC'] = 0.349065850399
Valves8['histo'] = 0
Valves8['Nval'] = 1
Valves8['Dv'] = 0.035
Valves8['position'] = (793, 331)
Valves8['type_dat'] = 0
Valves8['Cd'] = [[0.0, 0.75], [0.009, 0.75]]
Valves8['type'] = 1
Valves8['typeVal'] = 'exh'
Valves8['angle_V0'] = 8.55211333477
Valves8['valve_model'] = 1
Cylinders2['exhaust_valves'].append(Valves8)


Valves.append(Valves8)

Valves9 = dict()
Valves9['tube'] = 7
Valves9['Lvmax'] = 0.009
Valves9['ncyl'] = 3
Valves9['label'] = 'evalve3'
Valves9['angle_VC'] = 0.349065850399
Valves9['histo'] = 0
Valves9['Nval'] = 1
Valves9['Dv'] = 0.035
Valves9['position'] = (793, 463)
Valves9['type_dat'] = 0
Valves9['Cd'] = [[0.0, 0.75], [0.009, 0.75]]
Valves9['type'] = 1
Valves9['typeVal'] = 'exh'
Valves9['angle_V0'] = 8.55211333477
Valves9['valve_model'] = 1
Cylinders3['exhaust_valves'].append(Valves9)

Valves.append(Valves9)


Valves10 = dict()
Valves10['tube'] = 7
Valves10['Lvmax'] = 0.009
Valves10['ncyl'] = 3
Valves10['label'] = 'evalve4'
Valves10['angle_VC'] = 0.349065850399
Valves10['histo'] = 0
Valves10['Nval'] = 1
Valves10['Dv'] = 0.035
Valves10['position'] = (793, 463)
Valves10['type_dat'] = 0
Valves10['Cd'] = [[0.0, 0.75], [0.009, 0.75]]
Valves10['type'] = 1
Valves10['typeVal'] = 'exh'
Valves10['angle_V0'] = 8.55211333477
Valves10['valve_model'] = 1
Cylinders4['exhaust_valves'].append(Valves10)


Valves.append(Valves10)

Valves11 = dict()
Valves11['tube'] = 7
Valves11['Lvmax'] = 0.009
Valves11['ncyl'] = 3
Valves11['label'] = 'evalve5'
Valves11['angle_VC'] = 0.349065850399
Valves11['histo'] = 0
Valves11['Nval'] = 1
Valves11['Dv'] = 0.035
Valves11['position'] = (793, 463)
Valves11['type_dat'] = 0
Valves11['Cd'] = [[0.0, 0.75], [0.009, 0.75]]
Valves11['type'] = 1
Valves11['typeVal'] = 'exh'
Valves11['angle_V0'] = 8.55211333477
Valves11['valve_model'] = 1
Cylinders5['exhaust_valves'].append(Valves11)


Valves.append(Valves11)


#--------- FIN Inicializacion de Valves


#--------- Inicializacion de Tubes

Tubes = []

Tubes0 = dict()
Tubes0['diameter'] = [0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045]
Tubes0['longitud'] = 0.3
Tubes0['nnod'] = 31
Tubes0['ndof'] = 3
Tubes0['twall'] = [300.0, 301.666666667, 303.333333333, 305.0, 306.666666667, 308.333333333, 310.0, 311.666666667, 313.333333333, 315.0, 316.666666667, 318.333333333, 320.0, 321.666666667, 323.333333333, 325.0, 326.666666667, 328.333333333, 330.0, 331.666666667, 333.333333333, 335.0, 336.666666667, 338.333333333, 340.0, 341.666666667, 343.333333333, 345.0, 346.666666667, 348.333333333, 350.0]
Tubes0['numNorm'] = 2
Tubes0['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes0['tright'] = 'cylinder'
Tubes0['label'] = 'tube0'
Tubes0['histo'] = [0, 30]
Tubes0['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3]
Tubes0['nleft'] = 0
Tubes0['position'] = (397, 67)
Tubes0['tleft'] = 'tank'
Tubes0['posNorm'] = [0.0, 1.0]
Tubes0['nright'] = 0
Tubes0['typeSave'] = 1
Tubes0['type'] = 'intake'

Tubes.append(Tubes0)

Tubes1 = dict()
Tubes1['diameter'] = [0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045]
Tubes1['longitud'] = 0.3
Tubes1['nnod'] = 31
Tubes1['ndof'] = 3
Tubes1['twall'] = [300.0, 301.666666667, 303.333333333, 305.0, 306.666666667, 308.333333333, 310.0, 311.666666667, 313.333333333, 315.0, 316.666666667, 318.333333333, 320.0, 321.666666667, 323.333333333, 325.0, 326.666666667, 328.333333333, 330.0, 331.666666667, 333.333333333, 335.0, 336.666666667, 338.333333333, 340.0, 341.666666667, 343.333333333, 345.0, 346.666666667, 348.333333333, 350.0]
Tubes1['numNorm'] = 2
Tubes1['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes1['tright'] = 'cylinder'
Tubes1['label'] = 'tube1'
Tubes1['histo'] = [0, 30]
Tubes1['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3]
Tubes1['nleft'] = 0
Tubes1['position'] = (397, 199)
Tubes1['tleft'] = 'tank'
Tubes1['posNorm'] = [0.0, 1.0]
Tubes1['nright'] = 1
Tubes1['typeSave'] = 1
Tubes1['type'] = 'intake'

Tubes.append(Tubes1)

Tubes2 = dict()
Tubes2['diameter'] = [0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045]
Tubes2['longitud'] = 0.3
Tubes2['nnod'] = 31
Tubes2['ndof'] = 3
Tubes2['twall'] = [300.0, 301.666666667, 303.333333333, 305.0, 306.666666667, 308.333333333, 310.0, 311.666666667, 313.333333333, 315.0, 316.666666667, 318.333333333, 320.0, 321.666666667, 323.333333333, 325.0, 326.666666667, 328.333333333, 330.0, 331.666666667, 333.333333333, 335.0, 336.666666667, 338.333333333, 340.0, 341.666666667, 343.333333333, 345.0, 346.666666667, 348.333333333, 350.0]
Tubes2['numNorm'] = 2
Tubes2['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes2['tright'] = 'cylinder'
Tubes2['label'] = 'tube2'
Tubes2['histo'] = [0, 30]
Tubes2['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3]
Tubes2['nleft'] = 0
Tubes2['position'] = (397, 331)
Tubes2['tleft'] = 'tank'
Tubes2['posNorm'] = [0.0, 1.0]
Tubes2['nright'] = 2
Tubes2['typeSave'] = 1
Tubes2['type'] = 'intake'

Tubes.append(Tubes2)

Tubes3 = dict()
Tubes3['diameter'] = [0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045]
Tubes3['longitud'] = 0.3
Tubes3['nnod'] = 31
Tubes3['ndof'] = 3
Tubes3['twall'] = [300.0, 301.666666667, 303.333333333, 305.0, 306.666666667, 308.333333333, 310.0, 311.666666667, 313.333333333, 315.0, 316.666666667, 318.333333333, 320.0, 321.666666667, 323.333333333, 325.0, 326.666666667, 328.333333333, 330.0, 331.666666667, 333.333333333, 335.0, 336.666666667, 338.333333333, 340.0, 341.666666667, 343.333333333, 345.0, 346.666666667, 348.333333333, 350.0]
Tubes3['numNorm'] = 2
Tubes3['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes3['tright'] = 'cylinder'
Tubes3['label'] = 'tube3'
Tubes3['histo'] = [0, 30]
Tubes3['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3]
Tubes3['nleft'] = 0
Tubes3['position'] = (397, 463)
Tubes3['tleft'] = 'tank'
Tubes3['posNorm'] = [0.0, 1.0]
Tubes3['nright'] = 3
Tubes3['typeSave'] = 1
Tubes3['type'] = 'intake'

Tubes.append(Tubes3)

Tubes4 = dict()
Tubes4['diameter'] = [0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045]
Tubes4['longitud'] = 0.3
Tubes4['nnod'] = 31
Tubes4['ndof'] = 3
Tubes4['twall'] = [300.0, 301.666666667, 303.333333333, 305.0, 306.666666667, 308.333333333, 310.0, 311.666666667, 313.333333333, 315.0, 316.666666667, 318.333333333, 320.0, 321.666666667, 323.333333333, 325.0, 326.666666667, 328.333333333, 330.0, 331.666666667, 333.333333333, 335.0, 336.666666667, 338.333333333, 340.0, 341.666666667, 343.333333333, 345.0, 346.666666667, 348.333333333, 350.0]
Tubes4['numNorm'] = 2
Tubes4['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes4['tright'] = 'cylinder'
Tubes4['label'] = 'tube4'
Tubes4['histo'] = [0, 30]
Tubes4['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3]
Tubes4['nleft'] = 0
Tubes4['position'] = (397, 463)
Tubes4['tleft'] = 'tank'
Tubes4['posNorm'] = [0.0, 1.0]
Tubes4['nright'] = 4
Tubes4['typeSave'] = 1
Tubes4['type'] = 'intake'

Tubes.append(Tubes4)

Tubes5 = dict()
Tubes5['diameter'] = [0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045, 0.045]
Tubes5['longitud'] = 0.3
Tubes5['nnod'] = 31
Tubes5['ndof'] = 3
Tubes5['twall'] = [300.0, 301.666666667, 303.333333333, 305.0, 306.666666667, 308.333333333, 310.0, 311.666666667, 313.333333333, 315.0, 316.666666667, 318.333333333, 320.0, 321.666666667, 323.333333333, 325.0, 326.666666667, 328.333333333, 330.0, 331.666666667, 333.333333333, 335.0, 336.666666667, 338.333333333, 340.0, 341.666666667, 343.333333333, 345.0, 346.666666667, 348.333333333, 350.0]
Tubes5['numNorm'] = 2
Tubes5['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes5['tright'] = 'cylinder'
Tubes5['label'] = 'tube5'
Tubes5['histo'] = [0, 30]
Tubes5['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3]
Tubes5['nleft'] = 0
Tubes5['position'] = (397, 463)
Tubes5['tleft'] = 'tank'
Tubes5['posNorm'] = [0.0, 1.0]
Tubes5['nright'] = 5
Tubes5['typeSave'] = 1
Tubes5['type'] = 'intake'

Tubes.append(Tubes5)

Tubes6 = dict()
Tubes6['diameter'] = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
Tubes6['longitud'] = 0.5
Tubes6['nnod'] = 51
Tubes6['ndof'] = 3
Tubes6['twall'] = [450.0, 449.0, 448.0, 447.0, 446.0, 445.0, 444.0, 443.0, 442.0, 441.0, 440.0, 439.0, 438.0, 437.0, 436.0, 435.0, 434.0, 433.0, 432.0, 431.0, 430.0, 429.0, 428.0, 427.0, 426.0, 425.0, 424.0, 423.0, 422.0, 421.0, 420.0, 419.0, 418.0, 417.0, 416.0, 415.0, 414.0, 413.0, 412.0, 411.0, 410.0, 409.0, 408.0, 407.0, 406.0, 405.0, 404.0, 403.0, 402.0, 401.0, 400.0]
Tubes6['numNorm'] = 2
Tubes6['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes6['tright'] = 'junction'
Tubes6['label'] = 'tube6'
Tubes6['histo'] = [0, 50]
Tubes6['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5]
Tubes6['nleft'] = 0
Tubes6['position'] = (925, 67)
Tubes6['tleft'] = 'cylinder'
Tubes6['posNorm'] = [0.0, 1.0]
Tubes6['nright'] = 0
Tubes6['typeSave'] = 1
Tubes6['type'] = 'exhaust'

Tubes.append(Tubes6)

Tubes7 = dict()
Tubes7['diameter'] = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
Tubes7['longitud'] = 0.5
Tubes7['nnod'] = 51
Tubes7['ndof'] = 3
Tubes7['curvature'] = []
Tubes7['numNorm'] = 0
Tubes7['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes7['tright'] = 'junction'
Tubes7['label'] = 'tube7'
Tubes7['histo'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
Tubes7['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5]
Tubes7['nleft'] = 1
Tubes7['position'] = (925, 199)
Tubes7['twall'] = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0]
Tubes7['posNorm'] = []
Tubes7['tleft'] = 'cylinder'
Tubes7['nright'] = 0
Tubes7['typeSave'] = 0
Tubes7['type'] = 'exhaust'

Tubes.append(Tubes7)

Tubes8 = dict()
Tubes8['diameter'] = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
Tubes8['longitud'] = 0.5
Tubes8['nnod'] = 51
Tubes8['ndof'] = 3
Tubes8['twall'] = [450.0, 449.0, 448.0, 447.0, 446.0, 445.0, 444.0, 443.0, 442.0, 441.0, 440.0, 439.0, 438.0, 437.0, 436.0, 435.0, 434.0, 433.0, 432.0, 431.0, 430.0, 429.0, 428.0, 427.0, 426.0, 425.0, 424.0, 423.0, 422.0, 421.0, 420.0, 419.0, 418.0, 417.0, 416.0, 415.0, 414.0, 413.0, 412.0, 411.0, 410.0, 409.0, 408.0, 407.0, 406.0, 405.0, 404.0, 403.0, 402.0, 401.0, 400.0]
Tubes8['numNorm'] = 2
Tubes8['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes8['tright'] = 'junction'
Tubes8['label'] = 'tube8'
Tubes8['histo'] = [0, 50]
Tubes8['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5]
Tubes8['nleft'] = 2
Tubes8['position'] = (925, 331)
Tubes8['tleft'] = 'cylinder'
Tubes8['posNorm'] = [0.0, 1.0]
Tubes8['nright'] = 0
Tubes8['typeSave'] = 1
Tubes8['type'] = 'exhaust'

Tubes.append(Tubes8)

Tubes9 = dict()
Tubes9['diameter'] = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
Tubes9['longitud'] = 0.5
Tubes9['nnod'] = 51
Tubes9['ndof'] = 3
Tubes9['twall'] = [450.0, 449.0, 448.0, 447.0, 446.0, 445.0, 444.0, 443.0, 442.0, 441.0, 440.0, 439.0, 438.0, 437.0, 436.0, 435.0, 434.0, 433.0, 432.0, 431.0, 430.0, 429.0, 428.0, 427.0, 426.0, 425.0, 424.0, 423.0, 422.0, 421.0, 420.0, 419.0, 418.0, 417.0, 416.0, 415.0, 414.0, 413.0, 412.0, 411.0, 410.0, 409.0, 408.0, 407.0, 406.0, 405.0, 404.0, 403.0, 402.0, 401.0, 400.0]
Tubes9['numNorm'] = 2
Tubes9['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes9['tright'] = 'junction'
Tubes9['label'] = 'tube9'
Tubes9['histo'] = [0, 50]
Tubes9['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5]
Tubes9['nleft'] = 3
Tubes9['position'] = (925, 463)
Tubes9['tleft'] = 'cylinder'
Tubes9['posNorm'] = [0.0, 1.0]
Tubes9['nright'] = 0
Tubes9['typeSave'] = 1
Tubes9['type'] = 'exhaust'

Tubes.append(Tubes9)

Tubes10 = dict()
Tubes10['diameter'] = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
Tubes10['longitud'] = 0.5
Tubes10['nnod'] = 51
Tubes10['ndof'] = 3
Tubes10['twall'] = [450.0, 449.0, 448.0, 447.0, 446.0, 445.0, 444.0, 443.0, 442.0, 441.0, 440.0, 439.0, 438.0, 437.0, 436.0, 435.0, 434.0, 433.0, 432.0, 431.0, 430.0, 429.0, 428.0, 427.0, 426.0, 425.0, 424.0, 423.0, 422.0, 421.0, 420.0, 419.0, 418.0, 417.0, 416.0, 415.0, 414.0, 413.0, 412.0, 411.0, 410.0, 409.0, 408.0, 407.0, 406.0, 405.0, 404.0, 403.0, 402.0, 401.0, 400.0]
Tubes10['numNorm'] = 2
Tubes10['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes10['tright'] = 'junction'
Tubes10['label'] = 'tube10'
Tubes10['histo'] = [0, 50]
Tubes10['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5]
Tubes10['nleft'] = 4
Tubes10['position'] = (925, 463)
Tubes10['tleft'] = 'cylinder'
Tubes10['posNorm'] = [0.0, 1.0]
Tubes10['nright'] = 0
Tubes10['typeSave'] = 1
Tubes10['type'] = 'exhaust'

Tubes.append(Tubes10)

Tubes11 = dict()
Tubes11['diameter'] = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
Tubes11['longitud'] = 0.5
Tubes11['nnod'] = 51
Tubes11['ndof'] = 3
Tubes11['twall'] = [450.0, 449.0, 448.0, 447.0, 446.0, 445.0, 444.0, 443.0, 442.0, 441.0, 440.0, 439.0, 438.0, 437.0, 436.0, 435.0, 434.0, 433.0, 432.0, 431.0, 430.0, 429.0, 428.0, 427.0, 426.0, 425.0, 424.0, 423.0, 422.0, 421.0, 420.0, 419.0, 418.0, 417.0, 416.0, 415.0, 414.0, 413.0, 412.0, 411.0, 410.0, 409.0, 408.0, 407.0, 406.0, 405.0, 404.0, 403.0, 402.0, 401.0, 400.0]
Tubes11['numNorm'] = 2
Tubes11['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes11['tright'] = 'junction'
Tubes11['label'] = 'tube11'
Tubes11['histo'] = [0, 50]
Tubes11['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5]
Tubes11['nleft'] = 5
Tubes11['position'] = (925, 463)
Tubes11['tleft'] = 'cylinder'
Tubes11['posNorm'] = [0.0, 1.0]
Tubes11['nright'] = 0
Tubes11['typeSave'] = 1
Tubes11['type'] = 'exhaust'

Tubes.append(Tubes11)

Tubes12 = dict()
Tubes12['diameter'] = [0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
Tubes12['longitud'] = 0.2
Tubes12['nnod'] = 21
Tubes12['ndof'] = 3
Tubes12['twall'] = [300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0]
Tubes12['numNorm'] = 2
Tubes12['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes12['tright'] = 'tank'
Tubes12['label'] = 'tube12'
Tubes12['histo'] = [0, 20]
Tubes12['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2]
Tubes12['nleft'] = 0
Tubes12['position'] = (133, 265)
Tubes12['tleft'] = 'atmosphere'
Tubes12['posNorm'] = [0.0, 1.0]
Tubes12['nright'] = 0
Tubes12['typeSave'] = 1
Tubes12['type'] = 'exhaust'
Tubes.append(Tubes12)

Tubes13 = dict()
Tubes13['diameter'] = [0.055, 0.0553, 0.0556, 0.0559, 0.0562, 0.0565, 0.0568, 0.0571, 0.0574, 0.0577, 0.058, 0.0583, 0.0586, 0.0589, 0.0592, 0.0595, 0.0598, 0.0601, 0.0604, 0.0607, 0.061, 0.0613, 0.0616, 0.0619, 0.0622, 0.0625, 0.0628, 0.0631, 0.0634, 0.0637, 0.064, 0.0643, 0.0646, 0.0649, 0.0652, 0.0655, 0.0658, 0.0661, 0.0664, 0.0667, 0.067, 0.0673, 0.0676, 0.0679, 0.0682, 0.0685, 0.0688, 0.0691, 0.0694, 0.0697, 0.07]
Tubes13['longitud'] = 0.5
Tubes13['nnod'] = 51
Tubes13['ndof'] = 3
Tubes13['twall'] = [400.0, 399.0, 398.0, 397.0, 396.0, 395.0, 394.0, 393.0, 392.0, 391.0, 390.0, 389.0, 388.0, 387.0, 386.0, 385.0, 384.0, 383.0, 382.0, 381.0, 380.0, 379.0, 378.0, 377.0, 376.0, 375.0, 374.0, 373.0, 372.0, 371.0, 370.0, 369.0, 368.0, 367.0, 366.0, 365.0, 364.0, 363.0, 362.0, 361.0, 360.0, 359.0, 358.0, 357.0, 356.0, 355.0, 354.0, 353.0, 352.0, 351.0, 350.0]
Tubes13['numNorm'] = 2
Tubes13['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes13['tright'] = 'atmosphere'
Tubes13['label'] = 'tube13'
Tubes13['histo'] = [0, 50]
Tubes13['xnod'] = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5]
Tubes13['nleft'] = 0
Tubes13['position'] = (1189, 265)
Tubes13['tleft'] = 'junction'
Tubes13['posNorm'] = [0.0, 1.0]
Tubes13['nright'] = 1
Tubes13['typeSave'] = 1
Tubes13['type'] = 'exhaust'
Tubes.append(Tubes13)


#--------- FIN Inicializacion de Tubes


# #--------- Inicializacion de Tanks (Tank might not be required)

Tanks = []

# Tanks0 = dict()
# Tanks0['Area_wall'] = 0.15
# Tanks0['nnod'] = 6
# Tanks0['ndof'] = 3
# Tanks0['label'] = 'tank0'
# Tanks0['Volume'] = 0.003
# Tanks0['int2tube'] = [8]
# Tanks0['extras'] = 1
# Tanks0['mass'] = 0.00354
# Tanks0['histo'] = [0]
# Tanks0['exh2tube'] = [0, 1, 2, 3]
# Tanks0['Cd_ports'] = [0.9, 0.8, 0.8, 0.8, 0.8]
# Tanks0['position'] = (265, 265)
# Tanks0['T_wall'] = 300.0
# Tanks0['state_ini'] = [[1.1769, 101330.0, 300.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
# Tanks0['h_film'] = 300.0

# Tanks.append(Tanks0)


#--------- FIN Inicializacion de Tanks


#--------- Inicializacion de Junctions

Junctions = []

# Junctions0 = dict()
# Junctions0['type_end'] = [1, 1, 1, 1, -1]
# Junctions0['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
# Junctions0['nnod'] = 5
# Junctions0['ndof'] = 3
# Junctions0['label'] = 'junc0'
# Junctions0['node2tube'] = [4, 5, 6, 7, 9]
# Junctions0['extras'] = 1
# Junctions0['histo'] = [0, 1, 4]
# Junctions0['position'] = (1057, 265)
# Junctions0['modelo_junc'] = 1

# Junctions.append(Junctions0)


#--------- FIN Inicializacion de Junctions


#--------- Inicializacion de Atmospheres

Atmospheres = []

Atmospheres0 = dict()
Atmospheres0['nnod'] = 1
Atmospheres0['ndof'] = 3
Atmospheres0['state_ini'] = [1.1842, 1.0, 101330.0]
Atmospheres0['position'] = (1, 265)

Atmospheres.append(Atmospheres0)

Atmospheres1 = dict()
Atmospheres1['nnod'] = 1
Atmospheres1['ndof'] = 3
Atmospheres1['state_ini'] = [1.1842, 1.0, 101330.0]
Atmospheres1['position'] = (1321, 265)

Atmospheres.append(Atmospheres1)


#--------- Inicializacion de injection
# int pulse < Identifies law type of fuel injection (Identifica el tipo de ley con que se inyecta el combustible) */
#	double m_inj;					/**< Fuel mass injected for cycle */
#	double dtheta_inj;				/**< Injection duration, measure in crank angle */
#	double T_fuel;					/**< Temperature of fuel injection */
#	double theta_inj_ini; 			/**< Angle of start the injection  */3
# 	double theta_id;				/**< Angle delay of ignition (can be data or calculated internally) */
#	int ignition_delay_model;		/**< Ignition delay Model 0:"L-W", 1:"H-H", 2:"user-defined"*/
#	double integral;				/**< Variable used to integrate the ratio t / t_d over time  */
#	vector<double> mfdot_array; 	/**< Injected Mass of fuel in angle's function (Array containing the fuel injected mass as a function of the angle) */

injection0 = dict()
injection0['pulse'] = 1
injection0['m_inj'] = 100.0
injection0['dtheta_inj'] = 30.0
injection0['T_fuel'] = 500.0
injection0['theta_inj_ini'] = 345.0
injection0['theta_id']	= 0.0
injection0['ignition_delay_model']	= 1	#0: "L-W" (default), 1: "H-H", 2: "user-defined"
injection0['integral']	= 1.0
injection0['mfdot_array'] = []
Cylinders0['injection'] = injection0

injection1 = dict()
injection1['pulse'] = 1
injection1['m_inj'] = 100.0
injection1['dtheta_inj'] = 30.0
injection1['T_fuel'] = 500.0
injection1['theta_inj_ini'] = 345.0
injection1['theta_id']	= 0.0
injection1['ignition_delay_model']	= 1	#0: "L-W" (default), 1: "H-H", 2: "user-defined"
injection1['integral']	= 1.0
injection1['mfdot_array'] = []
Cylinders1['injection'] = injection1

injection2 = dict()
injection2['pulse'] = 1
injection2['m_inj'] = 100.0
injection2['dtheta_inj'] = 30.0
injection2['T_fuel'] = 500.0
injection2['theta_inj_ini'] = 345.0 
injection2['theta_id']	= 0.0
injection2['ignition_delay_model']	= 1	#0: "L-W" (default), 1: "H-H", 2: "user-defined"
injection2['integral']	= 1.0
injection2['mfdot_array'] = []
Cylinders2['injection'] = injection2

injection3 = dict()
injection3['pulse'] = 1
injection3['m_inj'] = 100.0
injection3['dtheta_inj'] = 30.0
injection3['T_fuel'] = 500.0
injection3['theta_inj_ini'] = 345.0
injection3['theta_id']	= 0.0
injection3['ignition_delay_model']	= 1	#0: "L-W" (default), 1: "H-H", 2: "user-defined"
injection3['integral']	= 1.0
injection3['mfdot_array'] = []
Cylinders3['injection'] = injection3

injection4 = dict()
injection4['pulse'] = 1
injection4['m_inj'] = 100.0
injection4['dtheta_inj'] = 30.0
injection4['T_fuel'] = 500.0
injection4['theta_inj_ini'] = 345.0
injection4['theta_id']	= 0.0
injection4['ignition_delay_model']	= 1	#0: "L-W" (default), 1: "H-H", 2: "user-defined"
injection4['integral']	= 1.0
injection4['mfdot_array'] = [] 
Cylinders4['injection'] = injection4

injection5 = dict()
injection5['pulse'] = 1
injection5['m_inj'] = 100.0
injection5['dtheta_inj'] = 30.0
injection5['T_fuel'] = 500.0
injection5['theta_inj_ini'] = 345.0
injection5['theta_id']	= 0.0
injection5['ignition_delay_model']	= 1	#0: "L-W" (default), 1: "H-H", 2: "user-defined"
injection5['integral']	= 1.0
injection5['mfdot_array'] = []
Cylinders5['injection'] = injection5



#--------- FIN Inicializacion de Atmospheres

kargs = {'Simulator':Simulator, 'Cylinders':Cylinders, 'Junctions':Junctions, 'Tubes':Tubes, 'Tanks':Tanks, 'Atmospheres':Atmospheres}