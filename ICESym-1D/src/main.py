from numpy import array
import time

from simCythonCPP import Simulator

test = raw_input("Choise the Script with the data for the TEST (without '.py'): ")
#test='BoscaMono'
data=__import__(test)
now = time.time()

Sim = Simulator(**data.kargs)
print "termina de inicializar"
Sim.printData()
Sim.solver()
now2 = time.time()
print now2-now
