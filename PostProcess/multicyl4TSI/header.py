rpms = [1000, 2000, 3000, 4000, 5000, 6000]

final_times = [0.600007, 0.300004, 0.200001, 0.150001, 0.120001, 0.100001]

nstroke = 4
ncycles = 5
rho = 1.1842
Globals = dict()
Globals['engine_data'] = 1
Tubes = []
Tube0 = dict()
Tube0['label'] = 'tube0'
Tube0['nnod'] = 31
Tube0['ndof'] = 3
Tube0['histo'] = [0, 30]
Tubes.append(Tube0)

Tube1 = dict()
Tube1['label'] = 'tube1'
Tube1['nnod'] = 31
Tube1['ndof'] = 3
Tube1['histo'] = [0, 30]
Tubes.append(Tube1)

Tube2 = dict()
Tube2['label'] = 'tube2'
Tube2['nnod'] = 31
Tube2['ndof'] = 3
Tube2['histo'] = [0, 30]
Tubes.append(Tube2)

Tube3 = dict()
Tube3['label'] = 'tube3'
Tube3['nnod'] = 31
Tube3['ndof'] = 3
Tube3['histo'] = [0, 30]
Tubes.append(Tube3)

Tube4 = dict()
Tube4['label'] = 'tube4'
Tube4['nnod'] = 51
Tube4['ndof'] = 3
Tube4['histo'] = [0, 50]
Tubes.append(Tube4)

Tube5 = dict()
Tube5['label'] = 'tube5'
Tube5['nnod'] = 51
Tube5['ndof'] = 3
Tube5['histo'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
Tubes.append(Tube5)

Tube6 = dict()
Tube6['label'] = 'tube6'
Tube6['nnod'] = 51
Tube6['ndof'] = 3
Tube6['histo'] = [0, 50]
Tubes.append(Tube6)

Tube7 = dict()
Tube7['label'] = 'tube7'
Tube7['nnod'] = 51
Tube7['ndof'] = 3
Tube7['histo'] = [0, 50]
Tubes.append(Tube7)

Tube8 = dict()
Tube8['label'] = 'tube8'
Tube8['nnod'] = 21
Tube8['ndof'] = 3
Tube8['histo'] = [0, 20]
Tubes.append(Tube8)

Tube9 = dict()
Tube9['label'] = 'tube9'
Tube9['nnod'] = 51
Tube9['ndof'] = 3
Tube9['histo'] = [0, 50]
Tubes.append(Tube9)

Tanks = []
Tank0 = dict()
Tank0['label'] = 'tank0'
Tank0['nnod'] = 6
Tank0['ndof'] = 3
Tank0['extras'] = 1
Tank0['histo'] = [0]
Tanks.append(Tank0)

Junctions = []
Junction0 = dict()
Junction0['label'] = 'junc0'
Junction0['nnod'] = 5
Junction0['ndof'] = 3
Junction0['histo'] = [0, 1, 4]
Junctions.append(Junction0)

Cylinders = []
Cylinder0 = dict()
Cylinder0['label'] = 'cyl00'
Cylinder0['ndof'] = 3
Cylinder0['nvi'] = 1
Cylinder0['nve'] = 1
Cylinder0['extras'] = 1
Cylinder0['Q_fuel'] = 4.43e+007
Cylinder0['crank_radius'] = 0.05
Cylinder0['histo'] = [0]
Cylinder0['angleClose'] = 220
Cylinders.append(Cylinder0)

Cylinder1 = dict()
Cylinder1['label'] = 'cyl1'
Cylinder1['ndof'] = 3
Cylinder1['nvi'] = 1
Cylinder1['nve'] = 1
Cylinder1['extras'] = 1
Cylinder1['Q_fuel'] = 4.43e+007
Cylinder1['crank_radius'] = 0.05
Cylinder1['histo'] = [0]
Cylinder1['angleClose'] = 220
Cylinders.append(Cylinder1)

Cylinder2 = dict()
Cylinder2['label'] = 'cyl2'
Cylinder2['ndof'] = 3
Cylinder2['nvi'] = 1
Cylinder2['nve'] = 1
Cylinder2['extras'] = 1
Cylinder2['Q_fuel'] = 4.43e+007
Cylinder2['crank_radius'] = 0.05
Cylinder2['histo'] = [0]
Cylinder2['angleClose'] = 220
Cylinders.append(Cylinder2)

Cylinder3 = dict()
Cylinder3['label'] = 'cyl3'
Cylinder3['ndof'] = 3
Cylinder3['nvi'] = 1
Cylinder3['nve'] = 1
Cylinder3['extras'] = 1
Cylinder3['Q_fuel'] = 4.43e+007
Cylinder3['crank_radius'] = 0.05
Cylinder3['histo'] = [0]
Cylinder3['angleClose'] = 220
Cylinders.append(Cylinder3)

