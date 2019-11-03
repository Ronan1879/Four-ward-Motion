#-----------------------------------------------------------------------
# universe.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
from body import Body 
from instream import InStream
from vector import Vector
import numpy as np

#-----------------------------------------------------------------------

class Universe:

    # Construct a new Universe object by reading a description
    # from the file whose name is filename.

    def __init__(self, filename):
        instream = InStream(filename)
        n = instream.readInt()

        radius = instream.readFloat()
        stddraw.setXscale(-radius, +radius)
        stddraw.setYscale(-radius, +radius)
        self._bodies = stdarray.create1D(n)
        self._xtracks = stdarray.create1D(n)
        self._ytracks = stdarray.create1D(n)

        for i in range(n):
            rx   = instream.readFloat()
            ry   = instream.readFloat()
            vx   = instream.readFloat()
            vy   = instream.readFloat()
            mass = instream.readFloat()
            r = Vector([rx, ry])
            v = Vector([vx, vy])
            self._bodies[i] = Body(r, v, mass)
            self._xtracks[i] = []
            self._ytracks[i] = []

    # Simulate the passing of dt seconds in self.
    
    def increaseTime(self, dt):
        
        # Initialize the forces to zero.
        n = len(self._bodies)
        f = stdarray.create1D(n, Vector([0, 0]))
        
        # Compute the forces.
        for i in range(n):
            for j in range(n):
                if i != j:
                    bodyi = self._bodies[i]
                    bodyj = self._bodies[j]
                    f[i] = f[i] + bodyi.forceFrom(bodyj)

        # Move the bodies.
        for i in range(n):
            current_body = self._bodies[i]
            current_body.move(f[i], dt)  
            self._xtracks[i].append(current_body._r[0])
            self._ytracks[i].append(current_body._r[1])
            # print(n)
            if n == 10:
                np.save("xtracks.npy", self._xtracks)
                np.save("ytracks.npy", self._ytracks)


    # Draw self to standard draw.
    def draw(self):
        for body in self._bodies:
            body.draw()


#-----------------------------------------------------------------------

# Accept a string filename and a float dt as command-line arguments.
# Simulate the motion in the universe defined by the contents of
# the file with the given filename, increasing time at the rate
# specified by dt.

def main():
    filename = sys.argv[1]
    dt = float(sys.argv[2])
    universe = Universe(filename)
    j = 0 
    while True:
        j += 1
        universe.increaseTime(dt)
        stddraw.clear()
        universe.draw()
        stddraw.show(10)
        if j == 1000:
            np.save("xtracks_{}.npy".format(len(universe._xtracks)), universe._xtracks)
            np.save("ytracks_{}.npy".format(len(universe._ytracks)), universe._ytracks)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python universe.py 2bodyTiny.txt 20000

# python universe.py 2body.txt 20000

# python universe.py 3body.txt 20000

# python universe.py 4body.txt 20000


