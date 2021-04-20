rpms = [1000, 1200, 1400, 1600, 1800, 2000]

final_times = [0.48, 0.4, 0.342859, 0.300002, 0.266668, 0.24]

nstroke = 4
ncycles = 4
rho = 1.1647
Globals = dict()
Globals['engine_data'] = 1
Tubes = []
Tube0 = dict()
Tube0['label'] = 'tube0'
Tube0['nnod'] = 51
Tube0['ndof'] = 3
Tube0['histo'] = [0, 50]
Tubes.append(Tube0)

Tube1 = dict()
Tube1['label'] = 'tube1'
Tube1['nnod'] = 121
Tube1['ndof'] = 3
Tube1['histo'] = [0, 120]
Tubes.append(Tube1)

Tube2 = dict()
Tube2['label'] = 'tube2'
Tube2['nnod'] = 121
Tube2['ndof'] = 3
Tube2['histo'] = [0, 120]
Tubes.append(Tube2)

Tube3 = dict()
Tube3['label'] = 'tube3'
Tube3['nnod'] = 61
Tube3['ndof'] = 3
Tube3['histo'] = [0, 60]
Tubes.append(Tube3)

Tube4 = dict()
Tube4['label'] = 'tube4'
Tube4['nnod'] = 61
Tube4['ndof'] = 3
Tube4['histo'] = [0, 60]
Tubes.append(Tube4)

Tube5 = dict()
Tube5['label'] = 'tube5'
Tube5['nnod'] = 101
Tube5['ndof'] = 3
Tube5['histo'] = [0, 100]
Tubes.append(Tube5)

Tanks = []
Tank0 = dict()
Tank0['label'] = 'tank0'
Tank0['nnod'] = 4
Tank0['ndof'] = 3
Tank0['extras'] = 0
Tank0['histo'] = [0]
Tanks.append(Tank0)

Junctions = []
Junction0 = dict()
Junction0['label'] = 'junc0'
Junction0['nnod'] = 3
Junction0['ndof'] = 3
Junction0['histo'] = []
Junctions.append(Junction0)

Cylinders = []
Cylinder0 = dict()
Cylinder0['label'] = 'cyl0'
Cylinder0['ndof'] = 3
Cylinder0['nvi'] = 1
Cylinder0['nve'] = 1
Cylinder0['extras'] = 1
Cylinder0['Q_fuel'] = 4.6e+07
Cylinder0['crank_radius'] = 0.034
Cylinder0['histo'] = [0, 1, 2]
Cylinder0['angleClose'] = 230.999
Cylinders.append(Cylinder0)

Cylinder1 = dict()
Cylinder1['label'] = 'cyl1'
Cylinder1['ndof'] = 3
Cylinder1['nvi'] = 1
Cylinder1['nve'] = 1
Cylinder1['extras'] = 1
Cylinder1['Q_fuel'] = 4.6e+07
Cylinder1['crank_radius'] = 0.034
Cylinder1['histo'] = [0, 1, 2]
Cylinder1['angleClose'] = 230.999
Cylinders.append(Cylinder1)

