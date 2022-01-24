# import math and time modules
import math
import time
import pyngl
# this get the unix clock tick as a float
tm=time.process_time()
# set some variables for radius
radiusX=2.0
radiusZ=4.0
# now get a circle based on the time
pointOnCircleX= math.cos(tm*10)*radiusX;
pointOnCircleZ= math.sin(tm*10)*radiusZ;
# finally set out values for the pos
pos[0]=pointOnCircleX
pos[2]=pointOnCircleZ
pos[1]=0.0

# note we can print for debug here
#print "pos values %f %f" %(pos[0],pos[2])

