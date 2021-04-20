rpms = [3000]

final_times = [0.200001]

nstroke = 2
ncycles = 10
rho = 1.1842
Globals = dict()
Globals['engine_data'] = 1
Tubes = []
Tube0 = dict()
Tube0['label'] = 'tube0'
Tube0['nnod'] = 41
Tube0['ndof'] = 3
Tube0['histo'] = [0, 40]
Tubes.append(Tube0)

Tube1 = dict()
Tube1['label'] = 'tube1'
Tube1['nnod'] = 19
Tube1['ndof'] = 3
Tube1['histo'] = [0, 18]
Tubes.append(Tube1)

Tube2 = dict()
Tube2['label'] = 'tube2'
Tube2['nnod'] = 41
Tube2['ndof'] = 3
Tube2['histo'] = [0, 40]
Tubes.append(Tube2)

Tube3 = dict()
Tube3['label'] = 'tube3'
Tube3['nnod'] = 41
Tube3['ndof'] = 3
Tube3['histo'] = [0, 40]
Tubes.append(Tube3)

Tanks = []
Tank0 = dict()
Tank0['label'] = 'tank0'
Tank0['nnod'] = 3
Tank0['ndof'] = 3
Tank0['extras'] = 1
Tank0['histo'] = [0]
Tanks.append(Tank0)

Junctions = []
Cylinders = []
Cylinder0 = dict()
Cylinder0['label'] = 'cyl'
Cylinder0['ndof'] = 3
Cylinder0['nvi'] = 1
Cylinder0['nve'] = 1
Cylinder0['extras'] = 1
Cylinder0['Q_fuel'] = 4.3e+07
Cylinder0['crank_radius'] = 0.035
Cylinder0['histo'] = [0]
Cylinder0['angleClose'] = 264
Cylinders.append(Cylinder0)

Cylinder1 = dict()
Cylinder1['label'] = 'ccase'
Cylinder1['ndof'] = 3
Cylinder1['nvi'] = 1
Cylinder1['nve'] = 1
Cylinder1['extras'] = 1
Cylinder1['Q_fuel'] = 1e-10
Cylinder1['crank_radius'] = 0.035
Cylinder1['histo'] = [0]
Cylinder1['angleClose'] = 240
Cylinders.append(Cylinder1)

