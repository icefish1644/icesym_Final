from numpy import array
import time
import sys
import os
from simCythonCPP import Simulator

sys.path.append("/mnt/c/Users/Gilbert/Desktop/icesym2/ICESym-GUI/saves")
data = __import__("compBiCyl")
now = time.time()
Sim = Simulator(**data.kargs)
print "termina de inicializar"
Sim.printData()
Sim.solver()
now2 = time.time()
print now2-now
