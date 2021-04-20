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
Simulator0['rpms'] = [2200]
Simulator0['calc_engine_data'] = 1
Simulator0['filesave_state'] = 'KamAZ7405'
Simulator0['ncycles'] = 5
Simulator0['nsave'] = 5
Simulator0['folder_name'] = 'KamAZ7405'
Simulator0['ga'] = 1.4
Simulator0['viscous_flow'] = 1.0
Simulator0['filesave_spd'] = ''
Simulator0['ig_order'] = [0,1,2,3,4,5,6,7]
Simulator0['get_state'] = 2
Simulator0['nappend'] = 5.0
Simulator0['engine_type'] = 0
Simulator0['nstroke'] = 4

Simulator = Simulator0


#--------- Inicializacion de Cylinders 1

Cylinders = []

Cylinders0 = dict()
Cylinders0['crank_radius'] = 0.06
Cylinders0['type_ig'] = 1
Cylinders0['ndof'] = 3
Cylinders0['full_implicit'] = 0.0
Cylinders0['model_ht'] = 1
Cylinders0['factor_ht'] = 0.36
Cylinders0['piston_area'] = 0.011309734
Cylinders0['exhaust_valves'] = []
Cylinders0['ownState'] = 1
Cylinders0['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Cylinders0['nnod'] = 3
Cylinders0['label'] = 'cyl'
Cylinders0['twall'] = [459.0]
Cylinders0['state_ini'] = [[1.1769, 101330.0, 300.0], [1.3195, 0.1, 128000.0], [1.1769, 0.1, 101330.0]]
Cylinders0['nve'] = 1
Cylinders0['intake_valves'] = []
Cylinders0['head_chamber_area'] = 0.012817698
Cylinders0['type_temperature'] = 0
Cylinders0['rod_length'] = 0.225
Cylinders0['species_model'] = 0
Cylinders0['nvi'] = 1
Cylinders0['delta_ca'] = 0.0
Cylinders0['Vol_clearance'] = 9.04778684234e-05
Cylinders0['extras'] = 1
Cylinders0['histo'] = [0]
Cylinders0['position'] = (416, 219)
Cylinders0['Bore'] = 0.12
Cylinders0['scavenge'] = 0.0

#--------- Inicializacion de combustion

combustion0 = dict()
combustion0['m_wiebe'] = 1.64
combustion0['combustion_model'] = 1
combustion0['theta_ig_0'] = 6.1261056745
combustion0['a_wiebe'] = 6.0
combustion0['dtheta_comb'] = 1.20427718388
Cylinders0['combustion'] = combustion0


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel0 = dict()
fuel0['y'] = 2.16667
fuel0['hvap_fuel'] = 350000.0
fuel0['Q_fuel'] = 42500000.0
Cylinders0['fuel'] = fuel0


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection0 = dict()
injection0['ignition_delay_model'] = 1
injection0['dtheta_inj'] = 0.130009575981
injection0['m_inj'] = 0.0001218
injection0['theta_inj_ini'] = 6.0388392119
injection0['T_fuel'] = 300.0
injection0['pulse'] = 1
Cylinders0['injection'] = injection0


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders0)


Cylinders1 = dict()
Cylinders1['crank_radius'] = 0.06
Cylinders1['type_ig'] = 1
Cylinders1['ndof'] = 3
Cylinders1['full_implicit'] = 0.0
Cylinders1['model_ht'] = 1
Cylinders1['factor_ht'] = 0.36
Cylinders1['piston_area'] = 0.011309734
Cylinders1['exhaust_valves'] = []
Cylinders1['ownState'] = 1
Cylinders1['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Cylinders1['nnod'] = 3
Cylinders1['label'] = 'cyl'
Cylinders1['twall'] = [459.0]
Cylinders1['state_ini'] = [[1.1769, 101330.0, 300.0], [1.3195, 0.1, 128000.0], [1.1769, 0.1, 101330.0]]
Cylinders1['nve'] = 1
Cylinders1['intake_valves'] = []
Cylinders1['head_chamber_area'] = 0.012817698
Cylinders1['type_temperature'] = 0
Cylinders1['rod_length'] = 0.225
Cylinders1['species_model'] = 0
Cylinders1['nvi'] = 1
Cylinders1['delta_ca'] = 0.0
Cylinders1['Vol_clearance'] = 9.04778684234e-05
Cylinders1['extras'] = 1
Cylinders1['histo'] = [0]
Cylinders1['position'] = (416, 219)
Cylinders1['Bore'] = 0.12
Cylinders1['scavenge'] = 0.0

#--------- Inicializacion de combustion

combustion1 = dict()
combustion1['m_wiebe'] = 1.64
combustion1['combustion_model'] = 1
combustion1['theta_ig_0'] = 6.1261056745
combustion1['a_wiebe'] = 6.0
combustion1['dtheta_comb'] = 1.20427718388
Cylinders1['combustion'] = combustion1


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel1 = dict()
fuel1['y'] = 2.16667
fuel1['hvap_fuel'] = 350000.0
fuel1['Q_fuel'] = 42500000.0
Cylinders1['fuel'] = fuel1


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection1 = dict()
injection1['ignition_delay_model'] = 1
injection1['dtheta_inj'] = 0.130009575981
injection1['m_inj'] = 0.0001218
injection1['theta_inj_ini'] = 6.0388392119
injection1['T_fuel'] = 300.0
injection1['pulse'] = 1
Cylinders1['injection'] = injection1


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders1)

Cylinders2 = dict()
Cylinders2['crank_radius'] = 0.06
Cylinders2['type_ig'] = 1
Cylinders2['ndof'] = 3
Cylinders2['full_implicit'] = 0.0
Cylinders2['model_ht'] = 1
Cylinders2['factor_ht'] = 0.36
Cylinders2['piston_area'] = 0.011309734
Cylinders2['exhaust_valves'] = []
Cylinders2['ownState'] = 1
Cylinders2['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Cylinders2['nnod'] = 3
Cylinders2['label'] = 'cyl'
Cylinders2['twall'] = [459.0]
Cylinders2['state_ini'] = [[1.1769, 101330.0, 300.0], [1.3195, 0.1, 128000.0], [1.1769, 0.1, 101330.0]]
Cylinders2['nve'] = 1
Cylinders2['intake_valves'] = []
Cylinders2['head_chamber_area'] = 0.012817698
Cylinders2['type_temperature'] = 0
Cylinders2['rod_length'] = 0.225
Cylinders2['species_model'] = 0
Cylinders2['nvi'] = 1
Cylinders2['delta_ca'] = 0.0
Cylinders2['Vol_clearance'] = 9.04778684234e-05
Cylinders2['extras'] = 1
Cylinders2['histo'] = [0]
Cylinders2['position'] = (416, 219)
Cylinders2['Bore'] = 0.12
Cylinders2['scavenge'] = 0.0

#--------- Inicializacion de combustion

combustion2 = dict()
combustion2['m_wiebe'] = 1.64
combustion2['combustion_model'] = 1
combustion2['theta_ig_0'] = 6.1261056745
combustion2['a_wiebe'] = 6.0
combustion2['dtheta_comb'] = 1.20427718388
Cylinders2['combustion'] = combustion2


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel2 = dict()
fuel2['y'] = 2.16667
fuel2['hvap_fuel'] = 350000.0
fuel2['Q_fuel'] = 42500000.0
Cylinders2['fuel'] = fuel2


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection2 = dict()
injection2['ignition_delay_model'] = 1
injection2['dtheta_inj'] = 0.130009575981
injection2['m_inj'] = 0.0001218
injection2['theta_inj_ini'] = 6.0388392119
injection2['T_fuel'] = 300.0
injection2['pulse'] = 1
Cylinders2['injection'] = injection2


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders2)

Cylinders3 = dict()
Cylinders3['crank_radius'] = 0.06
Cylinders3['type_ig'] = 1
Cylinders3['ndof'] = 3
Cylinders3['full_implicit'] = 0.0
Cylinders3['model_ht'] = 1
Cylinders3['factor_ht'] = 0.36
Cylinders3['piston_area'] = 0.011309734
Cylinders3['exhaust_valves'] = []
Cylinders3['ownState'] = 1
Cylinders3['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Cylinders3['nnod'] = 3
Cylinders3['label'] = 'cyl'
Cylinders3['twall'] = [459.0]
Cylinders3['state_ini'] = [[1.1769, 101330.0, 300.0], [1.3195, 0.1, 128000.0], [1.1769, 0.1, 101330.0]]
Cylinders3['nve'] = 1
Cylinders3['intake_valves'] = []
Cylinders3['head_chamber_area'] = 0.012817698
Cylinders3['type_temperature'] = 0
Cylinders3['rod_length'] = 0.225
Cylinders3['species_model'] = 0
Cylinders3['nvi'] = 1
Cylinders3['delta_ca'] = 0.0
Cylinders3['Vol_clearance'] = 9.04778684234e-05
Cylinders3['extras'] = 1
Cylinders3['histo'] = [0]
Cylinders3['position'] = (416, 219)
Cylinders3['Bore'] = 0.12
Cylinders3['scavenge'] = 0.0

#--------- Inicializacion de combustion

combustion3 = dict()
combustion3['m_wiebe'] = 1.64
combustion3['combustion_model'] = 1
combustion3['theta_ig_0'] = 6.1261056745
combustion3['a_wiebe'] = 6.0
combustion3['dtheta_comb'] = 1.20427718388
Cylinders3['combustion'] = combustion3


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel3 = dict()
fuel3['y'] = 2.16667
fuel3['hvap_fuel'] = 350000.0
fuel3['Q_fuel'] = 42500000.0
Cylinders3['fuel'] = fuel3


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection3 = dict()
injection3['ignition_delay_model'] = 1
injection3['dtheta_inj'] = 0.130009575981
injection3['m_inj'] = 0.0001218
injection3['theta_inj_ini'] = 6.0388392119
injection3['T_fuel'] = 300.0
injection3['pulse'] = 1
Cylinders3['injection'] = injection3


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders3)

Cylinders4 = dict()
Cylinders4['crank_radius'] = 0.06
Cylinders4['type_ig'] = 1
Cylinders4['ndof'] = 3
Cylinders4['full_implicit'] = 0.0
Cylinders4['model_ht'] = 1
Cylinders4['factor_ht'] = 0.36
Cylinders4['piston_area'] = 0.011309734
Cylinders4['exhaust_valves'] = []
Cylinders4['ownState'] = 1
Cylinders4['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Cylinders4['nnod'] = 3
Cylinders4['label'] = 'cyl'
Cylinders4['twall'] = [459.0]
Cylinders4['state_ini'] = [[1.1769, 101330.0, 300.0], [1.3195, 0.1, 128000.0], [1.1769, 0.1, 101330.0]]
Cylinders4['nve'] = 1
Cylinders4['intake_valves'] = []
Cylinders4['head_chamber_area'] = 0.012817698
Cylinders4['type_temperature'] = 0
Cylinders4['rod_length'] = 0.225
Cylinders4['species_model'] = 0
Cylinders4['nvi'] = 1
Cylinders4['delta_ca'] = 0.0
Cylinders4['Vol_clearance'] = 9.04778684234e-05
Cylinders4['extras'] = 1
Cylinders4['histo'] = [0]
Cylinders4['position'] = (416, 219)
Cylinders4['Bore'] = 0.12
Cylinders4['scavenge'] = 0.0

#--------- Inicializacion de combustion

combustion4 = dict()
combustion4['m_wiebe'] = 1.64
combustion4['combustion_model'] = 1
combustion4['theta_ig_0'] = 6.1261056745
combustion4['a_wiebe'] = 6.0
combustion4['dtheta_comb'] = 1.20427718388
Cylinders4['combustion'] = combustion4


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel4 = dict()
fuel4['y'] = 2.16667
fuel4['hvap_fuel'] = 350000.0
fuel4['Q_fuel'] = 42500000.0
Cylinders4['fuel'] = fuel4


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection4 = dict()
injection4['ignition_delay_model'] = 1
injection4['dtheta_inj'] = 0.130009575981
injection4['m_inj'] = 0.0001218
injection4['theta_inj_ini'] = 6.0388392119
injection4['T_fuel'] = 300.0
injection4['pulse'] = 1
Cylinders4['injection'] = injection4


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders4)

Cylinders5 = dict()
Cylinders5['crank_radius'] = 0.06
Cylinders5['type_ig'] = 1
Cylinders5['ndof'] = 3
Cylinders5['full_implicit'] = 0.0
Cylinders5['model_ht'] = 1
Cylinders5['factor_ht'] = 0.36
Cylinders5['piston_area'] = 0.011309734
Cylinders5['exhaust_valves'] = []
Cylinders5['ownState'] = 1
Cylinders5['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Cylinders5['nnod'] = 3
Cylinders5['label'] = 'cyl'
Cylinders5['twall'] = [459.0]
Cylinders5['state_ini'] = [[1.1769, 101330.0, 300.0], [1.3195, 0.1, 128000.0], [1.1769, 0.1, 101330.0]]
Cylinders5['nve'] = 1
Cylinders5['intake_valves'] = []
Cylinders5['head_chamber_area'] = 0.012817698
Cylinders5['type_temperature'] = 0
Cylinders5['rod_length'] = 0.225
Cylinders5['species_model'] = 0
Cylinders5['nvi'] = 1
Cylinders5['delta_ca'] = 0.0
Cylinders5['Vol_clearance'] = 9.04778684234e-05
Cylinders5['extras'] = 1
Cylinders5['histo'] = [0]
Cylinders5['position'] = (416, 219)
Cylinders5['Bore'] = 0.12
Cylinders5['scavenge'] = 0.0

#--------- Inicializacion de combustion

combustion5 = dict()
combustion5['m_wiebe'] = 1.64
combustion5['combustion_model'] = 1
combustion5['theta_ig_0'] = 6.1261056745
combustion5['a_wiebe'] = 6.0
combustion5['dtheta_comb'] = 1.20427718388
Cylinders5['combustion'] = combustion5


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel5 = dict()
fuel5['y'] = 2.16667
fuel5['hvap_fuel'] = 350000.0
fuel5['Q_fuel'] = 42500000.0
Cylinders5['fuel'] = fuel5


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection5 = dict()
injection5['ignition_delay_model'] = 1
injection5['dtheta_inj'] = 0.130009575981
injection5['m_inj'] = 0.0001218
injection5['theta_inj_ini'] = 6.0388392119
injection5['T_fuel'] = 300.0
injection5['pulse'] = 1
Cylinders5['injection'] = injection5


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders5)

Cylinders6 = dict()
Cylinders6['crank_radius'] = 0.06
Cylinders6['type_ig'] = 1
Cylinders6['ndof'] = 3
Cylinders6['full_implicit'] = 0.0
Cylinders6['model_ht'] = 1
Cylinders6['factor_ht'] = 0.36
Cylinders6['piston_area'] = 0.011309734
Cylinders6['exhaust_valves'] = []
Cylinders6['ownState'] = 1
Cylinders6['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Cylinders6['nnod'] = 3
Cylinders6['label'] = 'cyl'
Cylinders6['twall'] = [459.0]
Cylinders6['state_ini'] = [[1.1769, 101330.0, 300.0], [1.3195, 0.1, 128000.0], [1.1769, 0.1, 101330.0]]
Cylinders6['nve'] = 1
Cylinders6['intake_valves'] = []
Cylinders6['head_chamber_area'] = 0.012817698
Cylinders6['type_temperature'] = 0
Cylinders6['rod_length'] = 0.225
Cylinders6['species_model'] = 0
Cylinders6['nvi'] = 1
Cylinders6['delta_ca'] = 0.0
Cylinders6['Vol_clearance'] = 9.04778684234e-05
Cylinders6['extras'] = 1
Cylinders6['histo'] = [0]
Cylinders6['position'] = (416, 219)
Cylinders6['Bore'] = 0.12
Cylinders6['scavenge'] = 0.0

#--------- Inicializacion de combustion

combustion6 = dict()
combustion6['m_wiebe'] = 1.64
combustion6['combustion_model'] = 1
combustion6['theta_ig_0'] = 6.1261056745
combustion6['a_wiebe'] = 6.0
combustion6['dtheta_comb'] = 1.20427718388
Cylinders6['combustion'] = combustion6


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel6 = dict()
fuel6['y'] = 2.16667
fuel6['hvap_fuel'] = 350000.0
fuel6['Q_fuel'] = 42500000.0
Cylinders6['fuel'] = fuel6


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection6 = dict()
injection6['ignition_delay_model'] = 1
injection6['dtheta_inj'] = 0.130009575981
injection6['m_inj'] = 0.0001218
injection6['theta_inj_ini'] = 6.0388392119
injection6['T_fuel'] = 300.0
injection6['pulse'] = 1
Cylinders6['injection'] = injection6


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders6)

Cylinders7 = dict()
Cylinders7['crank_radius'] = 0.06
Cylinders7['type_ig'] = 1
Cylinders7['ndof'] = 3
Cylinders7['full_implicit'] = 0.0
Cylinders7['model_ht'] = 1
Cylinders7['factor_ht'] = 0.36
Cylinders7['piston_area'] = 0.011309734
Cylinders7['exhaust_valves'] = []
Cylinders7['ownState'] = 1
Cylinders7['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Cylinders7['nnod'] = 3
Cylinders7['label'] = 'cyl'
Cylinders7['twall'] = [459.0]
Cylinders7['state_ini'] = [[1.1769, 101330.0, 300.0], [1.3195, 0.1, 128000.0], [1.1769, 0.1, 101330.0]]
Cylinders7['nve'] = 1
Cylinders7['intake_valves'] = []
Cylinders7['head_chamber_area'] = 0.012817698
Cylinders7['type_temperature'] = 0
Cylinders7['rod_length'] = 0.225
Cylinders7['species_model'] = 0
Cylinders7['nvi'] = 1
Cylinders7['delta_ca'] = 0.0
Cylinders7['Vol_clearance'] = 9.04778684234e-05
Cylinders7['extras'] = 1
Cylinders7['histo'] = [0]
Cylinders7['position'] = (416, 219)
Cylinders7['Bore'] = 0.12
Cylinders7['scavenge'] = 0.0

#--------- Inicializacion de combustion

combustion7 = dict()
combustion7['m_wiebe'] = 1.64
combustion7['combustion_model'] = 1
combustion7['theta_ig_0'] = 6.1261056745
combustion7['a_wiebe'] = 6.0
combustion7['dtheta_comb'] = 1.20427718388
Cylinders7['combustion'] = combustion7


#--------- FIN Inicializacion de combustion


#--------- Inicializacion de fuel

fuel7 = dict()
fuel7['y'] = 2.16667
fuel7['hvap_fuel'] = 350000.0
fuel7['Q_fuel'] = 42500000.0
Cylinders7['fuel'] = fuel7


#--------- FIN Inicializacion de fuel


#--------- Inicializacion de injection

injection7 = dict()
injection7['ignition_delay_model'] = 1
injection7['dtheta_inj'] = 0.130009575981
injection7['m_inj'] = 0.0001218
injection7['theta_inj_ini'] = 6.0388392119
injection7['T_fuel'] = 300.0
injection7['pulse'] = 1
Cylinders7['injection'] = injection7


#--------- FIN Inicializacion de injection


Cylinders.append(Cylinders7)


#--------- FIN Inicializacion de Cylinders


#--------- Inicializacion de Valves

Valves = []

Valves0 = dict()
Valves0['Lvmax'] = 0.0088452
Valves0['tube'] = 0
Valves0['angle_VC'] = 4.01425727959
Valves0['ncyl'] = 0
Valves0['label'] = 'ivalve'
Valves0['Lv'] = []
Valves0['histo'] = 0
Valves0['Nval'] = 1
Valves0['Dv'] = 0.04
Valves0['position'] = (289, 193)
Valves0['type_dat'] = 0
Valves0['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves0['type'] = 0
Valves0['typeVal'] = 'int'
Valves0['angle_V0'] = 12.3045712266
Valves0['valve_model'] = 1
Cylinders0['intake_valves'].append(Valves0)


Valves.append(Valves0)

Valves1 = dict()
Valves1['Lvmax'] = 0.00880308
Valves1['tube'] = 1
Valves1['angle_VC'] = 0.261799387799
Valves1['ncyl'] = 0
Valves1['label'] = 'evalve'
Valves1['Lv'] = []
Valves1['histo'] = 0
Valves1['Nval'] = 1
Valves1['Dv'] = 0.04
Valves1['position'] = (509, 205)
Valves1['type_dat'] = 0
Valves1['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves1['type'] = 1
Valves1['typeVal'] = 'exh'
Valves1['angle_V0'] = 8.29031394697
Valves1['valve_model'] = 1
Cylinders0['exhaust_valves'].append(Valves1)


Valves.append(Valves1)

# Cyl 2

Valves2 = dict()
Valves2['Lvmax'] = 0.0088452
Valves2['tube'] = 0
Valves2['angle_VC'] = 4.01425727959
Valves2['ncyl'] = 1
Valves2['label'] = 'ivalve'
Valves2['Lv'] = []
Valves2['histo'] = 0
Valves2['Nval'] = 1
Valves2['Dv'] = 0.04
Valves2['position'] = (289, 193)
Valves2['type_dat'] = 0
Valves2['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves2['type'] = 0
Valves2['typeVal'] = 'int'
Valves2['angle_V0'] = 12.3045712266
Valves2['valve_model'] = 1
Cylinders1['intake_valves'].append(Valves2)


Valves.append(Valves2)

Valves3 = dict()
Valves3['Lvmax'] = 0.00880308
Valves3['tube'] = 1
Valves3['angle_VC'] = 0.261799387799
Valves3['ncyl'] = 1
Valves3['label'] = 'evalve'
Valves3['Lv'] = []
Valves3['histo'] = 0
Valves3['Nval'] = 1
Valves3['Dv'] = 0.04
Valves3['position'] = (509, 205)
Valves3['type_dat'] = 0
Valves3['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves3['type'] = 1
Valves3['typeVal'] = 'exh'
Valves3['angle_V0'] = 8.29031394697
Valves3['valve_model'] = 1
Cylinders1['exhaust_valves'].append(Valves3)


Valves.append(Valves3)

# Cyl 3

Valves4 = dict()
Valves4['Lvmax'] = 0.0088452
Valves4['tube'] = 0
Valves4['angle_VC'] = 4.01425727959
Valves4['ncyl'] = 2
Valves4['label'] = 'ivalve'
Valves4['Lv'] = []
Valves4['histo'] = 0
Valves4['Nval'] = 1
Valves4['Dv'] = 0.04
Valves4['position'] = (289, 193)
Valves4['type_dat'] = 0
Valves4['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves4['type'] = 0
Valves4['typeVal'] = 'int'
Valves4['angle_V0'] = 12.3045712266
Valves4['valve_model'] = 1
Cylinders2['intake_valves'].append(Valves4)


Valves.append(Valves4)

Valves5 = dict()
Valves5['Lvmax'] = 0.00880308
Valves5['tube'] = 1
Valves5['angle_VC'] = 0.261799387799
Valves5['ncyl'] = 2
Valves5['label'] = 'evalve'
Valves5['Lv'] = []
Valves5['histo'] = 0
Valves5['Nval'] = 1
Valves5['Dv'] = 0.04
Valves5['position'] = (509, 205)
Valves5['type_dat'] = 0
Valves5['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves5['type'] = 1
Valves5['typeVal'] = 'exh'
Valves5['angle_V0'] = 8.29031394697
Valves5['valve_model'] = 1
Cylinders2['exhaust_valves'].append(Valves5)


Valves.append(Valves5)

# Cyl 4

Valves6 = dict()
Valves6['Lvmax'] = 0.0088452
Valves6['tube'] = 0
Valves6['angle_VC'] = 4.01425727959
Valves6['ncyl'] = 3
Valves6['label'] = 'ivalve'
Valves6['Lv'] = []
Valves6['histo'] = 0
Valves6['Nval'] = 1
Valves6['Dv'] = 0.04
Valves6['position'] = (289, 193)
Valves6['type_dat'] = 0
Valves6['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves6['type'] = 0
Valves6['typeVal'] = 'int'
Valves6['angle_V0'] = 12.3045712266
Valves6['valve_model'] = 1
Cylinders3['intake_valves'].append(Valves6)


Valves.append(Valves6)

Valves7 = dict()
Valves7['Lvmax'] = 0.00880308
Valves7['tube'] = 1
Valves7['angle_VC'] = 0.261799387799
Valves7['ncyl'] = 3
Valves7['label'] = 'evalve'
Valves7['Lv'] = []
Valves7['histo'] = 0
Valves7['Nval'] = 1
Valves7['Dv'] = 0.04
Valves7['position'] = (509, 205)
Valves7['type_dat'] = 0
Valves7['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves7['type'] = 1
Valves7['typeVal'] = 'exh'
Valves7['angle_V0'] = 8.29031394697
Valves7['valve_model'] = 1
Cylinders3['exhaust_valves'].append(Valves7)


Valves.append(Valves7)

# Cyl 5

Valves8 = dict()
Valves8['Lvmax'] = 0.0088452
Valves8['tube'] = 0
Valves8['angle_VC'] = 4.01425727959
Valves8['ncyl'] = 4
Valves8['label'] = 'ivalve'
Valves8['Lv'] = []
Valves8['histo'] = 0
Valves8['Nval'] = 1
Valves8['Dv'] = 0.04
Valves8['position'] = (289, 193)
Valves8['type_dat'] = 0
Valves8['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves8['type'] = 0
Valves8['typeVal'] = 'int'
Valves8['angle_V0'] = 12.3045712266
Valves8['valve_model'] = 1
Cylinders4['intake_valves'].append(Valves8)


Valves.append(Valves8)

Valves9 = dict()
Valves9['Lvmax'] = 0.00880308
Valves9['tube'] = 1
Valves9['angle_VC'] = 0.261799387799
Valves9['ncyl'] = 4
Valves9['label'] = 'evalve'
Valves9['Lv'] = []
Valves9['histo'] = 0
Valves9['Nval'] = 1
Valves9['Dv'] = 0.04
Valves9['position'] = (509, 205)
Valves9['type_dat'] = 0
Valves9['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves9['type'] = 1
Valves9['typeVal'] = 'exh'
Valves9['angle_V0'] = 8.29031394697
Valves9['valve_model'] = 1
Cylinders4['exhaust_valves'].append(Valves9)


Valves.append(Valves9)

# Cyl 6

Valves10 = dict()
Valves10['Lvmax'] = 0.0088452
Valves10['tube'] = 0
Valves10['angle_VC'] = 4.01425727959
Valves10['ncyl'] = 5
Valves10['label'] = 'ivalve'
Valves10['Lv'] = []
Valves10['histo'] = 0
Valves10['Nval'] = 1
Valves10['Dv'] = 0.04
Valves10['position'] = (289, 193)
Valves10['type_dat'] = 0
Valves10['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves10['type'] = 0
Valves10['typeVal'] = 'int'
Valves10['angle_V0'] = 12.3045712266
Valves10['valve_model'] = 1
Cylinders5['intake_valves'].append(Valves10)


Valves.append(Valves10)

Valves11 = dict()
Valves11['Lvmax'] = 0.00880308
Valves11['tube'] = 1
Valves11['angle_VC'] = 0.261799387799
Valves11['ncyl'] = 5
Valves11['label'] = 'evalve'
Valves11['Lv'] = []
Valves11['histo'] = 0
Valves11['Nval'] = 1
Valves11['Dv'] = 0.04
Valves11['position'] = (509, 205)
Valves11['type_dat'] = 0
Valves11['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves11['type'] = 1
Valves11['typeVal'] = 'exh'
Valves11['angle_V0'] = 8.29031394697
Valves11['valve_model'] = 1
Cylinders5['exhaust_valves'].append(Valves11)


Valves.append(Valves11)

# Cyl 7 

Valves12 = dict()
Valves12['Lvmax'] = 0.0088452
Valves12['tube'] = 0
Valves12['angle_VC'] = 4.01425727959
Valves12['ncyl'] = 6
Valves12['label'] = 'ivalve'
Valves12['Lv'] = []
Valves12['histo'] = 0
Valves12['Nval'] = 1
Valves12['Dv'] = 0.04
Valves12['position'] = (289, 193)
Valves12['type_dat'] = 0
Valves12['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves12['type'] = 0
Valves12['typeVal'] = 'int'
Valves12['angle_V0'] = 12.3045712266
Valves12['valve_model'] = 1
Cylinders6['intake_valves'].append(Valves12)


Valves.append(Valves12)

Valves13 = dict()
Valves13['Lvmax'] = 0.00880308
Valves13['tube'] = 1
Valves13['angle_VC'] = 0.261799387799
Valves13['ncyl'] = 6
Valves13['label'] = 'evalve'
Valves13['Lv'] = []
Valves13['histo'] = 0
Valves13['Nval'] = 1
Valves13['Dv'] = 0.04
Valves13['position'] = (509, 205)
Valves13['type_dat'] = 0
Valves13['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves13['type'] = 1
Valves13['typeVal'] = 'exh'
Valves13['angle_V0'] = 8.29031394697
Valves13['valve_model'] = 1
Cylinders6['exhaust_valves'].append(Valves13)


Valves.append(Valves13)

# Cyl 8 

Valves14 = dict()
Valves14['Lvmax'] = 0.0088452
Valves14['tube'] = 0
Valves14['angle_VC'] = 4.01425727959
Valves14['ncyl'] = 7
Valves14['label'] = 'ivalve'
Valves14['Lv'] = []
Valves14['histo'] = 0
Valves14['Nval'] = 1
Valves14['Dv'] = 0.04
Valves14['position'] = (289, 193)
Valves14['type_dat'] = 0
Valves14['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves14['type'] = 0
Valves14['typeVal'] = 'int'
Valves14['angle_V0'] = 12.3045712266
Valves14['valve_model'] = 1
Cylinders7['intake_valves'].append(Valves14)


Valves.append(Valves14)

Valves15 = dict()
Valves15['Lvmax'] = 0.00880308
Valves15['tube'] = 1
Valves15['angle_VC'] = 0.261799387799
Valves15['ncyl'] = 7
Valves15['label'] = 'evalve'
Valves15['Lv'] = []
Valves15['histo'] = 0
Valves15['Nval'] = 1
Valves15['Dv'] = 0.04
Valves15['position'] = (509, 205)
Valves15['type_dat'] = 0
Valves15['Cd'] = [[0.0, 1.0], [0.009, 1.0]]
Valves15['type'] = 1
Valves15['typeVal'] = 'exh'
Valves15['angle_V0'] = 8.29031394697
Valves15['valve_model'] = 1
Cylinders7['exhaust_valves'].append(Valves15)


Valves.append(Valves15)


#--------- FIN Inicializacion de Valves


#--------- Inicializacion de Tubes

Tubes = []

Tubes0 = dict()
Tubes0['diameter'] = [0.044, 0.0442666666667, 0.0445333333333, 0.0448, 0.0450666666667, 0.0453333333333, 0.0456, 0.0458666666667, 0.0461333333333, 0.0464, 0.0466666666667, 0.0469333333333, 0.0472, 0.0474666666667, 0.0477333333333, 0.048, 0.0482666666667, 0.0485333333333, 0.0488, 0.0490666666667, 0.0493333333333, 0.0496, 0.0498666666667, 0.0501333333333, 0.0504, 0.0506666666667, 0.0509333333333, 0.0512, 0.0514666666667, 0.0517333333333, 0.052]
Tubes0['longitud'] = 0.15
Tubes0['nnod'] = 31
Tubes0['numNorm'] = 3
Tubes0['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0]
Tubes0['ndof'] = 3
Tubes0['state_ini'] = [[1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0]]
Tubes0['tright'] = 'cylinder'
Tubes0['label'] = 'tube0'
Tubes0['histo'] = [0, 15, 30]
Tubes0['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]
Tubes0['nleft'] = 0
Tubes0['position'] = (216, 210)
Tubes0['tleft'] = 'atmosphere'
Tubes0['posNorm'] = [0.0, 0.5, 1.0]
Tubes0['curvature'] = []
Tubes0['nright'] = 0
Tubes0['typeSave'] = 1

Tubes.append(Tubes0)

Tubes1 = dict()
Tubes1['diameter'] = [0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038]
Tubes1['longitud'] = 0.4
Tubes1['nnod'] = 81
Tubes1['numNorm'] = 3
Tubes1['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 375.0, 380.0, 385.0, 390.0, 395.0, 400.0]
Tubes1['ndof'] = 3
Tubes1['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes1['tright'] = 'atmosphere'
Tubes1['label'] = 'tube1'
Tubes1['histo'] = [0, 40, 80]
Tubes1['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4]
Tubes1['nleft'] = 0
Tubes1['position'] = (614, 213)
Tubes1['tleft'] = 'cylinder'
Tubes1['posNorm'] = [0.0, 0.5, 1.0]
Tubes1['curvature'] = []
Tubes1['nright'] = 1
Tubes1['typeSave'] = 1

Tubes.append(Tubes1)

# Cylinder 2

Tubes2 = dict()
Tubes2['diameter'] = [0.044, 0.0442666666667, 0.0445333333333, 0.0448, 0.0450666666667, 0.0453333333333, 0.0456, 0.0458666666667, 0.0461333333333, 0.0464, 0.0466666666667, 0.0469333333333, 0.0472, 0.0474666666667, 0.0477333333333, 0.048, 0.0482666666667, 0.0485333333333, 0.0488, 0.0490666666667, 0.0493333333333, 0.0496, 0.0498666666667, 0.0501333333333, 0.0504, 0.0506666666667, 0.0509333333333, 0.0512, 0.0514666666667, 0.0517333333333, 0.052]
Tubes2['longitud'] = 0.15
Tubes2['nnod'] = 31
Tubes2['numNorm'] = 3
Tubes2['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0]
Tubes2['ndof'] = 3
Tubes2['state_ini'] = [[1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0]]
Tubes2['tright'] = 'cylinder'
Tubes2['label'] = 'tube0'
Tubes2['histo'] = [0, 15, 30]
Tubes2['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]
Tubes2['nleft'] = 0
Tubes2['position'] = (216, 210)
Tubes2['tleft'] = 'atmosphere'
Tubes2['posNorm'] = [0.0, 0.5, 1.0]
Tubes2['curvature'] = []
Tubes2['nright'] = 1
Tubes2['typeSave'] = 1

Tubes.append(Tubes2)

Tubes3 = dict()
Tubes3['diameter'] = [0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038]
Tubes3['longitud'] = 0.4
Tubes3['nnod'] = 81
Tubes3['numNorm'] = 3
Tubes3['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 375.0, 380.0, 385.0, 390.0, 395.0, 400.0]
Tubes3['ndof'] = 3
Tubes3['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes3['tright'] = 'atmosphere'
Tubes3['label'] = 'tube1'
Tubes3['histo'] = [0, 40, 80]
Tubes3['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4]
Tubes3['nleft'] = 1
Tubes3['position'] = (614, 213)
Tubes3['tleft'] = 'cylinder'
Tubes3['posNorm'] = [0.0, 0.5, 1.0]
Tubes3['curvature'] = []
Tubes3['nright'] = 1
Tubes3['typeSave'] = 1

Tubes.append(Tubes3)

# Cylinder 3

Tubes4 = dict()
Tubes4['diameter'] = [0.044, 0.0442666666667, 0.0445333333333, 0.0448, 0.0450666666667, 0.0453333333333, 0.0456, 0.0458666666667, 0.0461333333333, 0.0464, 0.0466666666667, 0.0469333333333, 0.0472, 0.0474666666667, 0.0477333333333, 0.048, 0.0482666666667, 0.0485333333333, 0.0488, 0.0490666666667, 0.0493333333333, 0.0496, 0.0498666666667, 0.0501333333333, 0.0504, 0.0506666666667, 0.0509333333333, 0.0512, 0.0514666666667, 0.0517333333333, 0.052]
Tubes4['longitud'] = 0.15
Tubes4['nnod'] = 31
Tubes4['numNorm'] = 3
Tubes4['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0]
Tubes4['ndof'] = 3
Tubes4['state_ini'] = [[1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0]]
Tubes4['tright'] = 'cylinder'
Tubes4['label'] = 'tube0'
Tubes4['histo'] = [0, 15, 30]
Tubes4['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]
Tubes4['nleft'] = 0
Tubes4['position'] = (216, 210)
Tubes4['tleft'] = 'atmosphere'
Tubes4['posNorm'] = [0.0, 0.5, 1.0]
Tubes4['curvature'] = []
Tubes4['nright'] = 2
Tubes4['typeSave'] = 1

Tubes.append(Tubes4)

Tubes5 = dict()
Tubes5['diameter'] = [0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038]
Tubes5['longitud'] = 0.4
Tubes5['nnod'] = 81
Tubes5['numNorm'] = 3
Tubes5['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 375.0, 380.0, 385.0, 390.0, 395.0, 400.0]
Tubes5['ndof'] = 3
Tubes5['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes5['tright'] = 'atmosphere'
Tubes5['label'] = 'tube1'
Tubes5['histo'] = [0, 40, 80]
Tubes5['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4]
Tubes5['nleft'] = 2
Tubes5['position'] = (614, 213)
Tubes5['tleft'] = 'cylinder'
Tubes5['posNorm'] = [0.0, 0.5, 1.0]
Tubes5['curvature'] = []
Tubes5['nright'] = 1
Tubes5['typeSave'] = 1

Tubes.append(Tubes5)

# Cylinder 4

Tubes6 = dict()
Tubes6['diameter'] = [0.044, 0.0442666666667, 0.0445333333333, 0.0448, 0.0450666666667, 0.0453333333333, 0.0456, 0.0458666666667, 0.0461333333333, 0.0464, 0.0466666666667, 0.0469333333333, 0.0472, 0.0474666666667, 0.0477333333333, 0.048, 0.0482666666667, 0.0485333333333, 0.0488, 0.0490666666667, 0.0493333333333, 0.0496, 0.0498666666667, 0.0501333333333, 0.0504, 0.0506666666667, 0.0509333333333, 0.0512, 0.0514666666667, 0.0517333333333, 0.052]
Tubes6['longitud'] = 0.15
Tubes6['nnod'] = 31
Tubes6['numNorm'] = 3
Tubes6['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0]
Tubes6['ndof'] = 3
Tubes6['state_ini'] = [[1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0]]
Tubes6['tright'] = 'cylinder'
Tubes6['label'] = 'tube0'
Tubes6['histo'] = [0, 15, 30]
Tubes6['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]
Tubes6['nleft'] = 0
Tubes6['position'] = (216, 210)
Tubes6['tleft'] = 'atmosphere'
Tubes6['posNorm'] = [0.0, 0.5, 1.0]
Tubes6['curvature'] = []
Tubes6['nright'] = 3
Tubes6['typeSave'] = 1

Tubes.append(Tubes6)

Tubes7 = dict()
Tubes7['diameter'] = [0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038]
Tubes7['longitud'] = 0.4
Tubes7['nnod'] = 81
Tubes7['numNorm'] = 3
Tubes7['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 375.0, 380.0, 385.0, 390.0, 395.0, 400.0]
Tubes7['ndof'] = 3
Tubes7['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes7['tright'] = 'atmosphere'
Tubes7['label'] = 'tube1'
Tubes7['histo'] = [0, 40, 80]
Tubes7['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4]
Tubes7['nleft'] = 3
Tubes7['position'] = (614, 213)
Tubes7['tleft'] = 'cylinder'
Tubes7['posNorm'] = [0.0, 0.5, 1.0]
Tubes7['curvature'] = []
Tubes7['nright'] = 1
Tubes7['typeSave'] = 1

Tubes.append(Tubes7)

# Cylinder 5

Tubes8 = dict()
Tubes8['diameter'] = [0.044, 0.0442666666667, 0.0445333333333, 0.0448, 0.0450666666667, 0.0453333333333, 0.0456, 0.0458666666667, 0.0461333333333, 0.0464, 0.0466666666667, 0.0469333333333, 0.0472, 0.0474666666667, 0.0477333333333, 0.048, 0.0482666666667, 0.0485333333333, 0.0488, 0.0490666666667, 0.0493333333333, 0.0496, 0.0498666666667, 0.0501333333333, 0.0504, 0.0506666666667, 0.0509333333333, 0.0512, 0.0514666666667, 0.0517333333333, 0.052]
Tubes8['longitud'] = 0.15
Tubes8['nnod'] = 31
Tubes8['numNorm'] = 3
Tubes8['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0]
Tubes8['ndof'] = 3
Tubes8['state_ini'] = [[1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0]]
Tubes8['tright'] = 'cylinder'
Tubes8['label'] = 'tube0'
Tubes8['histo'] = [0, 15, 30]
Tubes8['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]
Tubes8['nleft'] = 0
Tubes8['position'] = (216, 210)
Tubes8['tleft'] = 'atmosphere'
Tubes8['posNorm'] = [0.0, 0.5, 1.0]
Tubes8['curvature'] = []
Tubes8['nright'] = 4
Tubes8['typeSave'] = 1

Tubes.append(Tubes8)

Tubes9 = dict()
Tubes9['diameter'] = [0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038]
Tubes9['longitud'] = 0.4
Tubes9['nnod'] = 81
Tubes9['numNorm'] = 3
Tubes9['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 375.0, 380.0, 385.0, 390.0, 395.0, 400.0]
Tubes9['ndof'] = 3
Tubes9['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes9['tright'] = 'atmosphere'
Tubes9['label'] = 'tube1'
Tubes9['histo'] = [0, 40, 80]
Tubes9['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4]
Tubes9['nleft'] = 4
Tubes9['position'] = (614, 213)
Tubes9['tleft'] = 'cylinder'
Tubes9['posNorm'] = [0.0, 0.5, 1.0]
Tubes9['curvature'] = []
Tubes9['nright'] = 1
Tubes9['typeSave'] = 1

Tubes.append(Tubes9)

# Cylinder 6

Tubes10 = dict()
Tubes10['diameter'] = [0.044, 0.0442666666667, 0.0445333333333, 0.0448, 0.0450666666667, 0.0453333333333, 0.0456, 0.0458666666667, 0.0461333333333, 0.0464, 0.0466666666667, 0.0469333333333, 0.0472, 0.0474666666667, 0.0477333333333, 0.048, 0.0482666666667, 0.0485333333333, 0.0488, 0.0490666666667, 0.0493333333333, 0.0496, 0.0498666666667, 0.0501333333333, 0.0504, 0.0506666666667, 0.0509333333333, 0.0512, 0.0514666666667, 0.0517333333333, 0.052]
Tubes10['longitud'] = 0.15
Tubes10['nnod'] = 31
Tubes10['numNorm'] = 3
Tubes10['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0]
Tubes10['ndof'] = 3
Tubes10['state_ini'] = [[1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0]]
Tubes10['tright'] = 'cylinder'
Tubes10['label'] = 'tube0'
Tubes10['histo'] = [0, 15, 30]
Tubes10['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]
Tubes10['nleft'] = 0
Tubes10['position'] = (216, 210)
Tubes10['tleft'] = 'atmosphere'
Tubes10['posNorm'] = [0.0, 0.5, 1.0]
Tubes10['curvature'] = []
Tubes10['nright'] = 5
Tubes10['typeSave'] = 1

Tubes.append(Tubes10)

Tubes11 = dict()
Tubes11['diameter'] = [0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038]
Tubes11['longitud'] = 0.4
Tubes11['nnod'] = 81
Tubes11['numNorm'] = 3
Tubes11['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 375.0, 380.0, 385.0, 390.0, 395.0, 400.0]
Tubes11['ndof'] = 3
Tubes11['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes11['tright'] = 'atmosphere'
Tubes11['label'] = 'tube1'
Tubes11['histo'] = [0, 40, 80]
Tubes11['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4]
Tubes11['nleft'] = 5
Tubes11['position'] = (614, 213)
Tubes11['tleft'] = 'cylinder'
Tubes11['posNorm'] = [0.0, 0.5, 1.0]
Tubes11['curvature'] = []
Tubes11['nright'] = 1
Tubes11['typeSave'] = 1

Tubes.append(Tubes11)

# Cylinder 7 

Tubes12 = dict()
Tubes12['diameter'] = [0.044, 0.0442666666667, 0.0445333333333, 0.0448, 0.0450666666667, 0.0453333333333, 0.0456, 0.0458666666667, 0.0461333333333, 0.0464, 0.0466666666667, 0.0469333333333, 0.0472, 0.0474666666667, 0.0477333333333, 0.048, 0.0482666666667, 0.0485333333333, 0.0488, 0.0490666666667, 0.0493333333333, 0.0496, 0.0498666666667, 0.0501333333333, 0.0504, 0.0506666666667, 0.0509333333333, 0.0512, 0.0514666666667, 0.0517333333333, 0.052]
Tubes12['longitud'] = 0.15
Tubes12['nnod'] = 31
Tubes12['numNorm'] = 3
Tubes12['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0]
Tubes12['ndof'] = 3
Tubes12['state_ini'] = [[1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0]]
Tubes12['tright'] = 'cylinder'
Tubes12['label'] = 'tube0'
Tubes12['histo'] = [0, 15, 30]
Tubes12['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]
Tubes12['nleft'] = 0
Tubes12['position'] = (216, 210)
Tubes12['tleft'] = 'atmosphere'
Tubes12['posNorm'] = [0.0, 0.5, 1.0]
Tubes12['curvature'] = []
Tubes12['nright'] = 6
Tubes12['typeSave'] = 1

Tubes.append(Tubes12)

Tubes13 = dict()
Tubes13['diameter'] = [0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038]
Tubes13['longitud'] = 0.4
Tubes13['nnod'] = 81
Tubes13['numNorm'] = 3
Tubes13['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 375.0, 380.0, 385.0, 390.0, 395.0, 400.0]
Tubes13['ndof'] = 3
Tubes13['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes13['tright'] = 'atmosphere'
Tubes13['label'] = 'tube1'
Tubes13['histo'] = [0, 40, 80]
Tubes13['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4]
Tubes13['nleft'] = 6
Tubes13['position'] = (614, 213)
Tubes13['tleft'] = 'cylinder'
Tubes13['posNorm'] = [0.0, 0.5, 1.0]
Tubes13['curvature'] = []
Tubes13['nright'] = 1
Tubes13['typeSave'] = 1

Tubes.append(Tubes13)

# Cylinder 8

Tubes14 = dict()
Tubes14['diameter'] = [0.044, 0.0442666666667, 0.0445333333333, 0.0448, 0.0450666666667, 0.0453333333333, 0.0456, 0.0458666666667, 0.0461333333333, 0.0464, 0.0466666666667, 0.0469333333333, 0.0472, 0.0474666666667, 0.0477333333333, 0.048, 0.0482666666667, 0.0485333333333, 0.0488, 0.0490666666667, 0.0493333333333, 0.0496, 0.0498666666667, 0.0501333333333, 0.0504, 0.0506666666667, 0.0509333333333, 0.0512, 0.0514666666667, 0.0517333333333, 0.052]
Tubes14['longitud'] = 0.15
Tubes14['nnod'] = 31
Tubes14['numNorm'] = 3
Tubes14['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0]
Tubes14['ndof'] = 3
Tubes14['state_ini'] = [[1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0], [1.3195, 0.1, 128000.0]]
Tubes14['tright'] = 'cylinder'
Tubes14['label'] = 'tube0'
Tubes14['histo'] = [0, 15, 30]
Tubes14['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]
Tubes14['nleft'] = 0
Tubes14['position'] = (216, 210)
Tubes14['tleft'] = 'atmosphere'
Tubes14['posNorm'] = [0.0, 0.5, 1.0]
Tubes14['curvature'] = []
Tubes14['nright'] = 7
Tubes14['typeSave'] = 1

Tubes.append(Tubes14)

Tubes15 = dict()
Tubes15['diameter'] = [0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038, 0.038]
Tubes15['longitud'] = 0.4
Tubes15['nnod'] = 81
Tubes15['numNorm'] = 3
Tubes15['twall'] = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 375.0, 380.0, 385.0, 390.0, 395.0, 400.0]
Tubes15['ndof'] = 3
Tubes15['state_ini'] = [[1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0], [1.1769, 0.1, 101330.0]]
Tubes15['tright'] = 'atmosphere'
Tubes15['label'] = 'tube1'
Tubes15['histo'] = [0, 40, 80]
Tubes15['xnod'] = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 0.195, 0.2, 0.205, 0.21, 0.215, 0.22, 0.225, 0.23, 0.235, 0.24, 0.245, 0.25, 0.255, 0.26, 0.265, 0.27, 0.275, 0.28, 0.285, 0.29, 0.295, 0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35, 0.355, 0.36, 0.365, 0.37, 0.375, 0.38, 0.385, 0.39, 0.395, 0.4]
Tubes15['nleft'] = 7
Tubes15['position'] = (614, 213)
Tubes15['tleft'] = 'cylinder'
Tubes15['posNorm'] = [0.0, 0.5, 1.0]
Tubes15['curvature'] = []
Tubes15['nright'] = 1
Tubes15['typeSave'] = 1

Tubes.append(Tubes15)


#--------- FIN Inicializacion de Tubes


#--------- Inicializacion de Tanks

Tanks = []


#--------- FIN Inicializacion de Tanks


#--------- Inicializacion de Junctions

Junctions = []


#--------- FIN Inicializacion de Junctions


#--------- Inicializacion de Atmospheres

Atmospheres = []

Atmospheres0 = dict()
Atmospheres0['nnod'] = 1
Atmospheres0['ndof'] = 3
Atmospheres0['state_ini'] = [1.3195, 0.1, 128000.0]
Atmospheres0['position'] = (135, 202)

Atmospheres.append(Atmospheres0)

Atmospheres1 = dict()
Atmospheres1['nnod'] = 1
Atmospheres1['ndof'] = 3
Atmospheres1['state_ini'] = [1.4351, 0.1, 120330.0]
Atmospheres1['position'] = (732, 217)

Atmospheres.append(Atmospheres1)


#--------- FIN Inicializacion de Atmospheres

kargs = {'Simulator':Simulator, 'Cylinders':Cylinders, 'Junctions':Junctions, 'Tubes':Tubes, 'Tanks':Tanks, 'Atmospheres':Atmospheres}