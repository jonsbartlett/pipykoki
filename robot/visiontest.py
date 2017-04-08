from robot import *
from timeit import default_timer as timer
R = Robot()

while True:
    t1=timer()
    m = R.see((1024,768),preview=False,preview_time=1)
    t=timer()
    t = t - t1
    print t
    if len(m)>0:
        print m[0].distance
        print m[0].marker_type
    else:
        print "nothing"
