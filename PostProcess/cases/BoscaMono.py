# coding: utf-8
#	SINGLE CYLINDER ENGINE MODEL - BOSCAROL # 20/06
#	School of Mechanical Engineering - FCEIA - UNR


##Geometrical parameters
L0 = 0.14;	D0I = 0.24;	D0F = 0.186;
L1 = 0.26;
D1 = 0.08;
L2a = 0.15;	
L2b = 0.225;
D2aI = 0.05;	D2aF = 0.043;	D2bF = 0.042;
L3 = 0.92;
D3I = 0.044;	D3F = 0.044;
L4 = 0.5;
D4I = 0.060;	D4F = 0.078;	##Before it was 2 of 0.65

##Valve diameter
DValInt = 0.03; DValExh = 0.023; #Minimum seat diameters according to drawings

##Values ​​used for initialization
rho_ini = 1.1647;	p_ini = 101330.0;	T_ini = 330.15;	Q = 0.001; 	#IC based on Q to maintain continuity condition in canhos
pi = 3.14159
pi = 3.14159
PHI = 1.4318
rpms = [8000]
#Start combustion
theta0 = 5.65
#Combustion Duration
dtheta = 1.6755
AWiebe = 5
MWiebe = 2

#Plenum CD, for test restriction washer
CdPlen = 1

CdI0 = 0.65 #0.9;
CdE0 = 0.62 #0.9;

CdI = [[0., 0.], [1e-8, CdI0],[0.004, 0.65],[0.012, 0.4], [0.015, 0.44]]
CdE = [[0., 0.], [1e-8, CdE0], [0.007, 0.6], [0.015, 0.4]]

#--------------------End of model parameter definition----------------------##
##Libraries used to manage arrangements
from numpy import ones, arange, zeros, concatenate

#--------- Simulator Initialization
Simulator0 = dict()							#Create Simulator Dictionary
Simulator0['filein_state'] = 'mono.dat'	    #File to load initial state
Simulator0['filesave_spd'] = ''				#File name to save the chemical concentration of the species at each time step.
Simulator0['filesave_state'] = 'mono.dat'	#File name to save the state at each step of time.
Simulator0['folder_name'] = 'BoscaMono'		#Name of the folder to save the simulation. It must be searched for to carry out the post-processing.
Simulator0['calc_engine_data'] = 1
Simulator0['heat_flow'] = 1.0				#Calculate heat transfer. 0 = no, 1 = yes.
Simulator0['viscous_flow'] = 1.0			#Calculate friction. 0 = no, 1 = yes.
Simulator0['get_state'] = 2					#Select how you initialize the state: \n
                                            #From Here-> You must indicates the State in each component \n
                                            #From File-> You must indicates the file to load the state for all components. (Used when you need to continue a simulation) \n
                                            #From Fortran-> ICESym-1D calculates the initial state numerically with a predictor.
Simulator0['nappend'] = 50	#100.0			#Number of iterations to save the information of the components. To correctly see the results in the post-process, it is convenient to decrease this value. For more speed, increase it. 0 = never.
Simulator0['nsave'] = 10					#Number of iterations to save the state of the simulation. 0 = Never.
Simulator0['Courant'] = 0.7
Simulator0['dtheta_rpm'] = 0.05				#Variation of the crankshaft angle at each time step.
Simulator0['dt'] = 0.366666666e-7	        #0.3666666666667e-7	
Simulator0['rpms'] = rpms 		            #List of RPM to simulate.
Simulator0['ncycles'] = 6					#Number of cycles (thermodynamics) to simulate at each RPM
Simulator0['nstroke'] = 4					#Times per cycle (4 times, or 2 times)
Simulator0['R_gas'] = 286.9					#Gas Constant
Simulator0['ga'] = 1.36						#Specific Heat Ratio
Simulator0['ga_intake'] = 1.37
Simulator0['ig_order'] = [0]			    #Ignition order
Simulator0['engine_type'] = 0
Simulator0['use_global_gas_properties'] = 1
Simulator = Simulator0
#--------- FIN Simulator Initialization


#--------- Cylinder Initialization
Cylinders = []
#			Cylinder0
Cylinders0 = dict()					#Create Cylinder0 dictionary.
Cylinders0['label'] = 'CYLINDER0'	#Label
Cylinders0['position'] = (965,1100)	#Location on the GUI screen.
Cylinders0['nvi'] = 1				#Number of intake valves per cylinder.
Cylinders0['nve'] = 1				#Number of exhaust valves per cylinder.
Cylinders0['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3
Cylinders0['type_ig'] = 0			#Ignition Type: 0 = by spark, 1 = by compression.
Cylinders0['full_implicit'] = 0.0	
Cylinders0['model_ht'] = 3			#Heat transfer calculation model. 3 = Taylor.
Cylinders0['factor_ht'] = 0.8
Cylinders0['ownState'] = 1
Cylinders0['nnod'] = 3				#Number of nodes. The cylinder has 3.
Cylinders0['species_model'] = 0		
Cylinders0['scavenge'] = 0.0
Cylinders0['extras'] = 1
Cylinders0['histo'] = [0, 1, 2]		#List of nodes for which data is saved.
Cylinders0['delta_ca'] = 0.0		#Only applies to engines with opposing pistons.
Cylinders0['exhaust_valves'] = []
Cylinders0['intake_valves'] = []
Cylinders0['crank_radius'] = 0.044	#Crankshaft Radius.
Cylinders0['rod_length'] = 0.14		#Connecting Rod Length
Cylinders0['piston_area'] = 0.0057	#Piston Area
Cylinders0['Bore'] = 0.0865			#Bore Diameter
Cylinders0['twall'] = [600.0]		#Temperature of Cylinder Wall
Cylinders0['SRv'] = 0.01			#Scavenge ratio by volume.
Cylinders0['head_chamber_area'] = 0.005741 	#Wall surface of the combustion chamber
Cylinders0['Vol_clearance'] = 5.944e-05		#Combustion chamber volume
Cylinders0['mass_C'] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] #Mass of fuel, air and residual gases in cylinder.
Cylinders0['state_ini'] = [[rho_ini, p_ini, T_ini], [rho_ini, 1.0, p_ini], [rho_ini, 1.0, p_ini]]

#--------- FIN Cylinder Initialization

#--------- Fuel Initialization
fuel0 = dict()					#Create Fuel0 dictionary.
fuel0['y'] = 2.25				#Hydrogen / Carbon Ratio of Fuel.
fuel0['hvap_fuel'] = 0.01 		#Heat of vaporization of fuel [J / kg].
fuel0['Q_fuel'] = 	46000000.0	#Lower calorific power of fuel [J / kg].
Cylinders0['fuel'] = fuel0
#--------- FIN Fuel Initialization

#--------- Combustion Initialization
combustion0 = dict()			#Create Combustion0 dictionary'.
combustion0['phi'] = PHI 	#Fuel/ Air Ratio
combustion0['combustion_model'] = 1 #Combustion model
combustion0['a_wiebe'] = AWiebe		#Combustion efficiency parameter for the Wiebe function.
combustion0['m_wiebe'] = MWiebe		#Shape parameter for the Wiebe function.
combustion0['dtheta_comb'] = dtheta #Duration of combustion at crankshaft angle, in radians
combustion0['theta_ig_0'] = theta0		#Combustion initiation angle, in radians. 2 * pi = TDC of power cycle
Cylinders0['combustion'] = combustion0
#--------- FIN Combustion Initialization

#--------- Injection Initialization
injection0 = dict()	#Create dictionary 'Injection0'.
Cylinders0['injection'] = injection0
#--------- FIN Injection Initialization

Cylinders.append(Cylinders0) #Add Cylinder 0 to the set of cylinders (without this line, Cylinder 0 does not exist).

#--------- Valves Initialization
Valves = []
from numpy import loadtxt
LvI = loadtxt("../src/Lv_I-mb.dat")
LvE = loadtxt("../src/Lv_E-mb.dat")
IVO = 11.3446;	#11.8159
IVC = 4.93928;	#4.41568
EVO = 7.6969;	#8.22050
EVC = 1.3089;	#0.82030
Lvmaxi = max(LvI[:,1]);		Lvmaxe = max(LvE[:,1])
#Lvmaxi = 0.01419;	Lvmaxe = 0.01419

#			VALVE 0
Valves0 = dict()				#Create Valve0 dictionary.
Valves0['label'] = 'VALVE0'	    #Label
Valves0['position'] = (860,1170)#Location on the GUI screen.
Valves0['tube'] = 2				#Tube connected to the valve.
Valves0['ncyl'] = 0				#Cylinder connected to the valve.
Valves0['typeVal'] = 'int'		#Valve type: 'int' = intake, 'exh' = exhaust.
Valves0['type'] = 0				#Valve type: 0 = intake, 1 = exhaust.
Valves0['Nval'] = 2				#Number of valves
Valves0['histo'] = 1			#List of nodes for which data is saved.
Valves0['valve_model'] = 0      #Valve model, 0 or 1
Valves0['type_dat'] = 1			#Cam Profile Type: 0 = square sine, 1 = user defined.
Valves0['Lv'] =  LvI			#Arrays of pairs [Angle (deg), Height (m)].
Valves0['Lvmax'] = Lvmaxi		#Maximum opening height.
Valves0['angle_V0'] = IVO		#Opening Angle.
Valves0['angle_VC'] = IVC		#Angle Closure
Valves0['Dv'] = DValInt			#Valve head diameter.
Valves0['Cd'] = CdI				#Discharge coefficient.
Cylinders0['intake_valves'].append(Valves0)
Valves.append(Valves0)

#			VALVE 1
Valves1 = dict()				#Create Valve1 dictionary.
Valves1['label'] = 'VALVE 1'	#Label
Valves1['position'] = (1065,1170)#Location on the GUI screen.
Valves1['tube'] = 3				#Tube connected to the valve.
Valves1['ncyl'] = 0				#Cylinder connected to the valve..
Valves1['typeVal'] = 'exh'		#Valve type: 'int' = intake, 'exh' = exhaust.
Valves1['type'] = 1				#Valve type: 0 = intake, 1 = exhaust.
Valves1['Nval'] = 2				#Number of valves
Valves1['histo'] = 1			#List of nodes for which data is saved.
Valves1['valve_model'] = 0      #Valve model, 0 or 1
Valves1['type_dat'] = 1			#Cam Profile Type: 0 = square sine, 1 = user defined.
Valves1['Lv'] = LvE				#Arrays of pairs [Angle (deg), Height (m)].
Valves1['Lvmax'] = Lvmaxe		#Maximum opening height.
Valves1['angle_V0'] = EVO		#Opening Angle.
Valves1['angle_VC'] = EVC		#Angle Closure
Valves1['Dv'] = DValExh			#Valve head diameter.
Valves1['Cd'] = CdE				#Discharge coefficient.
Cylinders0['exhaust_valves'].append(Valves1)
Valves.append(Valves1)

#--------- Tubes Initialization
Tubes = []
#			Notes regarding tubes: One node every 5 mm.
#			They connect only to atmospheres, gaskets, tanks and cylinders..

#			TUBE 0
N0 = 28
diameter0 = D0I*ones(N0+1)+(D0F-D0I)/N0*arange(N0+1)
StateIni0 = zeros((N0+1,3))
StateIni0[:,0] = rho_ini
StateIni0[:,1] = Q/(pi*(diameter0/2)*(diameter0/2))
StateIni0[:,2] = p_ini
Tubes0 = dict()                 #Create Tubes0 dictionary
Tubes0['label'] = 'TUBO0'		#Label
Tubes0['position'] = (200,625)	#Location on the GUI screen.
Tubes0['typeSave'] = 1
Tubes0['tleft'] = 'atmosphere'	#Item type left
Tubes0['nleft'] = 0				#Index of the item on the left.
Tubes0['tright'] = 'tank'		#Item type on the right.
Tubes0['nright'] = 0			#Index of the item on the right.
Tubes0['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Tubes0['nnod'] = N0+1			#Number of nodes.
Tubes0['numNorm'] = 2			#Is left 2
Tubes0['histo'] = [0, N0] 		#List of nodes for which data is saved.
Tubes0['posNorm'] = [0.0, 1.0]
Tubes0['longitud'] = L0			#Tube length
Tubes0['diameter'] = diameter0.copy()
Tubes0['twall'] = T_ini*ones(N0+1)
Tubes0['xnod'] = L0/N0*arange(N0+1)
Tubes0['state_ini'] = StateIni0.copy() #[Density, Speed, Pressure] x Number of Nodes.
Tubes0['type'] = 'intake'
Tubes.append(Tubes0)

#			TUBE 1
Tubes1 = dict() #Create Tubes1 dictionary
N1 = int(L1/0.005)
diameter1 = D1*ones(N1+1)
StateIni1 = zeros((N1+1,3))
StateIni1[:,0] = rho_ini
StateIni1[:,1] = Q/(pi*(diameter1/2)*(diameter1/2))
StateIni1[:,2] = p_ini
Tubes1['label'] = 'TUBE1'		#Label
Tubes1['position'] = (435,625)	#Location on the GUI screen.
Tubes1['typeSave'] = 1
Tubes1['tleft'] = 'tank'		#Item type left
Tubes1['nleft'] = 0				#Index of the item on the left.
Tubes1['tright'] = 'tank'		#Item type on the right.
Tubes1['nright'] = 1			#Index of the item on the right
Tubes1['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Tubes1['nnod'] = N1+1			#Number of nodes.
Tubes1['numNorm'] = 2			#Is left 2
Tubes1['histo'] = [0, N1] 		#List of nodes for which data is saved.
Tubes1['posNorm'] = [0.0, 1.0]
Tubes1['longitud'] = L1         #Length of tube
Tubes1['diameter'] = diameter1.copy()
Tubes1['twall'] = T_ini*ones(N1+1)
Tubes1['xnod'] = L1/N1*arange(N1+1)
Tubes1['state_ini'] = StateIni1.copy() #[Density, Speed, Pressure] x Number of Nodes.
Tubes1['type'] = 'intake'
Tubes.append(Tubes1)

#			TUBE 2
Tubes2 = dict() ##Create Tubes2 dictionary
N2a = int(L2a/0.005);
N2b = int(L2b/0.005);
L2 = L2a+L2b;
N2 = N2a+N2b+1
diameter2 = D2aI*ones(N2a+1)+(D2aF-D2aI)/N2a*arange(N2a+1)
diameter2 = concatenate((diameter2,D2aF*ones(N2b+1)+(D2bF-D2aF)/N2b*arange(N2b+1)),axis=0)
StateIni2 = zeros((N2+1,3))
StateIni2[:,0] = rho_ini
StateIni2[:,1] = Q/(pi*(diameter2/2)*(diameter2/2))
StateIni2[:,2] = p_ini
Tubes2['label'] = 'TUBE2'		#Label
Tubes2['position'] = (730,1170)	#Location on the GUI screen.
Tubes2['typeSave'] = 1
Tubes2['tleft'] = 'tank'		#Item type left
Tubes2['nleft'] = 0				#Index of the item on the left.
Tubes2['tright'] = 'cylinder'		#Item type on the right.
Tubes2['nright'] = 0			#Index of the item on the right
Tubes2['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Tubes2['nnod'] = N2+1			#Number of nodes.
Tubes2['numNorm'] = 2			#Is left 2
Tubes2['histo'] = [0, N2] 		#List of nodes for which data is saved.
Tubes2['posNorm'] = [0.0, 1.0]
Tubes2['longitud'] = L2         #Length of tube
Tubes2['diameter'] = diameter2.copy()
Tubes2['twall'] = T_ini*ones(N2+1)
Tubes2['xnod'] = L2/N2*arange(N2+1)
Tubes2['state_ini'] = StateIni2.copy() #[Density, Speed, Pressure] x Number of Nodes.
Tubes2['type'] = 'intake'
Tubes.append(Tubes2)

#			TUBE 3
Tubes3 = dict() ##Create Tubes3 dictionary
N3 = int(L3/0.005)
diameter3 = D3I*ones(N3+1)+(D3F-D3I)/N3*arange(N3+1)
StateIni3 = zeros((N3+1,3))
StateIni3[:,0] = rho_ini
StateIni3[:,1] = Q/(pi*(diameter3/2)*(diameter3/2))
StateIni3[:,2] = p_ini
Tubes3['label'] = 'TUBE3'		#Label
Tubes3['position'] = (730,880)	#Location on the GUI screen.
Tubes3['typeSave'] = 1
Tubes3['tleft'] = 'cylinder'		#Item type left
Tubes3['nleft'] = 0				#Index of the item on the left.
Tubes3['tright'] = 'tank'		#Item type on the right.
Tubes3['nright'] = 2			#Index of the item on the right
Tubes3['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Tubes3['nnod'] = N3+1			#Number of nodes.
Tubes3['numNorm'] = 2			#Is left 2
Tubes3['histo'] = [0, N3] 		#List of nodes for which data is saved.
Tubes3['posNorm'] = [0.0, 1.0]
Tubes3['longitud'] = L3         #Length of tube
Tubes3['diameter'] = diameter3.copy()
Tubes3['twall'] = T_ini*ones(N3+1)
Tubes3['xnod'] = L3/N3*arange(N3+1)
Tubes3['state_ini'] = StateIni3.copy() #[Density, Speed, Pressure] x Number of Nodes.
Tubes3['type'] = 'exhaust'
Tubes.append(Tubes3)

#			TUBE 4
Tubes4 = dict() ##Create Tubes4 dictionary
N4 = int(L4/0.005)
diameter4 = D4I*ones(N4+1)+(D4F-D4I)/N4*arange(N4+1)
StateIni4 = zeros((N4+1,3))
StateIni4[:,0] = rho_ini
StateIni4[:,1] = Q/(pi*(diameter4/2)*(diameter4/2))
StateIni4[:,2] = p_ini
Tubes4['label'] = 'TUBE4'		#Label
Tubes4['position'] = (730,480)	#Location on the GUI screen.
Tubes4['typeSave'] = 1
Tubes4['tleft'] = 'tank'		#Item type left
Tubes4['nleft'] = 2				#Index of the item on the left.
Tubes4['tright'] = 'atmosphere'	#Item type on the right.
Tubes4['nright'] = 1        	#Index of the item on the right
Tubes4['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Tubes4['nnod'] = N4+1			#Number of nodes.
Tubes4['numNorm'] = 2			#Is left 2
Tubes4['histo'] = [0, N4] 		#List of nodes for which data is saved.
Tubes4['posNorm'] = [0.0, 1.0]
Tubes4['longitud'] = L4         #Length of tube
Tubes4['diameter'] = diameter4.copy()
Tubes4['twall'] = T_ini*ones(N4+1)
Tubes4['xnod'] = L4/N4*arange(N4+1)
Tubes4['state_ini'] = StateIni4.copy() #[Density, Speed, Pressure] x Number of Nodes.
Tubes4['type'] = 'exhaust'
Tubes.append(Tubes4)

#--------- Fin Tubes Initialization


#--------- Junction Initialization
Junctions = []	#In this model there are no joints
#
#--------- Fin Junction Initialization

#--------- Tanks Initialization
Tanks = []
#			TANK 0
Tanks0 = dict()				#Create Tank0 dictionary
Tanks0['label'] = 'TANK0'	#Label
Tanks0['position'] = (315,625)	#Location on the GUI screen.
Tanks0['implicit']  = 1
Tanks0['int2tube'] = [0]		#Intake tubes.
Tanks0['exh2tube'] = [1]		#Exhaust tubes.
Tanks0['type_end']  = [1, -1]
Tanks0['nnod'] = 3				#Number of nodes. nnod = tubes + 1
Tanks0['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Tanks0['extras'] = 0			
Tanks0['histo'] = [0, 1, 2]		#List of nodes for which data is saved.
Tanks0['Area_wall'] = 0.175	#Wall surface.
Tanks0['Volume'] = 0.0075		#Tank volume
Tanks0['mass'] = 0.01		#Mass of gas contained in the tank
Tanks0['Cd_ports'] = [1.0, 1.0]	#Discharge coefficient. For gaskets and tanks: 1.0 # 0.144 bounous reference for air intake
Tanks0['T_wall'] = 330.0		#Wall temperature.
Tanks0['h_film'] = 300.0		#Heat transfer coefficient [W / m ^ 2 K].
Tanks0['state_ini'] = [[rho_ini, p_ini, T_ini], [rho_ini, 1.0, p_ini], [rho_ini, 1.0, p_ini]]
Tanks0['type'] = 'intake'
Tanks.append(Tanks0)

#			TANK 1
Tanks1 = dict()				#Create Tank1 dictionary
Tanks1['label'] = 'TANK1'	#Label
Tanks1['position'] = (565,625)	#Location on the GUI screen.
Tanks1['implicit']  = 1
Tanks1['int2tube'] = [1]		#Intake tubes.
Tanks1['exh2tube'] = [2]		#Exhaust tubes.
Tanks1['type_end']  = [1, -1]
Tanks1['nnod'] = 3				#Number of nodes. nnod = tubes + 1
Tanks1['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Tanks1['extras'] = 0			
Tanks1['histo'] = [0, 1, 2]		#List of nodes for which data is saved.
Tanks1['Area_wall'] = 0.025	#Wall surface.
Tanks1['Volume'] = 0.00037504		#Tank volume
Tanks1['mass'] = 0.00045		#Mass of gas contained in the tank
Tanks1['Cd_ports'] = [1.0, CdPlen]	#Discharge coefficient. For gaskets and tanks: 1.0 For tube 1 the restriction of the flange is considered
Tanks1['T_wall'] = 330.0		#Wall temperature.
Tanks1['h_film'] = 300.0		#Heat transfer coefficient [W / m ^ 2 K].
Tanks1['state_ini'] = [[rho_ini, p_ini, T_ini], [rho_ini, 1.0, p_ini], [rho_ini, 1.0, p_ini]]
Tanks1['type'] = 'intake'
Tanks.append(Tanks1)

#			TANK 2
Tanks2 = dict()				#Create Tank2 dictionary
Tanks2['label'] = 'TANK2'	#Label
Tanks2['position'] = (1900,625)	#Location on the GUI screen.
Tanks2['implicit']  = 1
Tanks2['int2tube'] = [3]		#Intake tubes.
Tanks2['exh2tube'] = [4]		#Exhaust tubes.
Tanks2['type_end']  = [1, -1]
Tanks2['nnod'] = 3				#Number of nodes. nnod = tubes + 1
Tanks2['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Tanks2['extras'] = 0			
Tanks2['histo'] = [0, 1, 2]		#List of nodes for which data is saved.
Tanks2['Area_wall'] = 0.061261	#Wall surface.
Tanks2['Volume'] = 0.00183775		#Tank volume
Tanks2['mass'] = 0.0021425		#Mass of gas contained in the tank
Tanks2['Cd_ports'] = [1.0, 1.0]	#Discharge coefficient. For gaskets and tanks: 1.0 
Tanks2['T_wall'] = 330.0		#Wall temperature.
Tanks2['h_film'] = 300.0		#Heat transfer coefficient [W / m ^ 2 K].
Tanks2['state_ini'] = [[rho_ini, p_ini, T_ini], [rho_ini, 1.0, p_ini], [rho_ini, 1.0, p_ini]]
Tanks2['type'] = 'exhaust'
Tanks.append(Tanks2)

#--------- FIN Tank Initialization

#--------- Atmosphere Initialization
Atmospheres = []

#			ATMOSPHERE0
Atmospheres0 = dict()					#Create Atmosphere0 dictionary
Atmospheres0['position'] = (170,625)	#Location on the GUI screen.
Atmospheres0['implicit']  = 0
Atmospheres0['nnod'] = 1				#Number of nodes. nnod = 1.
Atmospheres0['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Atmospheres0['state_ini'] = [rho_ini, 2.2222, p_ini]	#[Density, Speed, Abs Pressure].
Atmospheres.append(Atmospheres0)

#			ATMOSPHERE2
Atmospheres1 = dict()					#Create Atmosphere0 dictionary
Atmospheres1['position'] = (2150,625)	#Location on the GUI screen.
Atmospheres1['implicit']  = 0
Atmospheres1['nnod'] = 1				#Number of nodes. nnod = 1.
Atmospheres1['ndof'] = 3				#Number of degrees of freedom: Always ndof = 3.
Atmospheres1['state_ini'] = [rho_ini, 4.666, p_ini]	#[Density, Speed, Abs Pressure].
Atmospheres.append(Atmospheres1)
#--------- FIN Atmosphere Initialization


#Locate the data
kargs = {'Simulator':Simulator, 'Cylinders':Cylinders, 'Junctions':Junctions, 'Tubes':Tubes, 'Tanks':Tanks, 'Atmospheres':Atmospheres}
