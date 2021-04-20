rpms = [600, 700, 800, 900, 1000, 1100, 1200]

final_times = [2, 1.71429, 1.5, 1.33334, 1.2, 1.09091, 1]

nstroke = 2
ncycles = 20
rho = 1.3195
Globals = dict()
Globals['engine_data'] = 1
Tubes = []
Tube0 = dict()
Tube0['label'] = 'tube0'
Tube0['nnod'] = 31
Tube0['ndof'] = 3
Tube0['histo'] = [0, 15, 30]
Tubes.append(Tube0)

Tube1 = dict()
Tube1['label'] = 'tube1'
Tube1['nnod'] = 81
Tube1['ndof'] = 3
Tube1['histo'] = [0, 40, 80]
Tubes.append(Tube1)

Tanks = []
Junctions = []
Cylinders = []
Cylinder0 = dict()
Cylinder0['label'] = 'cyl'
Cylinder0['ndof'] = 3
Cylinder0['nvi'] = 1
Cylinder0['nve'] = 1
Cylinder0['extras'] = 1
Cylinder0['Q_fuel'] = 4.25e+07
Cylinder0['crank_radius'] = 0.06
Cylinder0['histo'] = [0]
Cylinder0['angleClose'] = 230
Cylinders.append(Cylinder0)

