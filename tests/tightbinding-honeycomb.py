#!/usr/bin/python3

import sys
sys.path.append("../")

from bandstructure.lattice import HoneycombLattice
from bandstructure.system import TightBindingSystem
from bandstructure.plot import Plot
from bandstructure import Parameters

params = Parameters()
lattice = HoneycombLattice(params)
#lattice.makeFiniteCircle(2)
#lattice.makeFiniteRectangle(8,10,center=[0.5,0])
#lattice.makeFiniteAlongdirection(latticevector=0, repetitions=5)

system = TightBindingSystem(lattice, {'t': 1})
#plot = Plot(system)
#plot.plotDispersion()

# === tests ===
import matplotlib.pyplot as plt
import numpy as np

cutoff = 15

# --- distance matrix ---
distances = lattice.getDistances(cutoff)

nSubs = distances.shape[0]
nLinks = distances.shape[2]

distances = np.sqrt(np.sum(distances**2,axis=-1)).reshape(nSubs,nLinks*nSubs).T
plt.imshow(distances, aspect='auto',interpolation='nearest')
plt.show()

# --- positions ---
positions = lattice.getPositions(cutoff)

fig = plt.gcf()
fig.gca().add_artist(plt.Circle((0,0),cutoff,fc='0.9',ec='k'))

plt.plot(positions[:,0],positions[:,1], 'ko',ms=5)
plt.axes().set_aspect('equal')
plt.xlim(-1.3*cutoff,1.3*cutoff)
plt.ylim(-1.3*cutoff,1.3*cutoff)
plt.show()

# --- geometry ---
geometry = lattice.getGeometry(cutoff)

fig = plt.gcf()
fig.gca().add_artist(plt.Circle((0,0),cutoff,fc='0.9',ec='k'))

for p in geometry:
    plt.plot(p[:,0],p[:,1], 'o',ms=5)
plt.axes().set_aspect('equal')
plt.xlim(-1.3*cutoff,1.3*cutoff)
plt.ylim(-1.3*cutoff,1.3*cutoff)
plt.show()

# --- distance matrix ---
kvectors = lattice.getKvectorsZone(100)
kvectors = np.sqrt(np.sum(kvectors**2,axis=-1))

plt.imshow(kvectors, aspect='equal',interpolation='nearest')
plt.show()

print(lattice.getNNCutoff())
print(lattice.getKvectorsPath(10))