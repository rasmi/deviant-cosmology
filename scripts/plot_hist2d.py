#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')
import numpy as np
import yt
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import h5py

fields = {
    'density': ('gas', 'density'),
    'pressure': ('gas', 'pressure'),
}

ds = yt.load('RD0000/RD0000')
ad = ds.covering_grid(level=0, left_edge=[0.0, 0.0, 0.0], dims=ds.domain_dimensions)

density = np.array(ad[fields['density']][:])[:-1,:-1,:-1]
pressure = np.array(ad[fields['pressure']][:])[:-1,:-1,:-1]

filename = 'effective_pressure_RD0000.hdf5'
effective_pressure_file = h5py.File(filename)
p_eff_x = np.array(effective_pressure_file['p_eff_x'][:])[:,:-1,:-1]
p_eff_y = np.array(effective_pressure_file['p_eff_y'][:])[:-1,:,:-1]
p_eff_z = np.array(effective_pressure_file['p_eff_z'][:])[:-1,:-1,:]
print "density", density.shape
print "pressure", pressure.shape
print "p_eff_x", p_eff_x.shape
print "p_eff_y", p_eff_y.shape
print "p_eff_z", p_eff_z.shape

norm = np.sqrt(np.square(p_eff_x) + np.square(p_eff_y) + np.square(p_eff_z))
soundspeed = np.sqrt((pressure / density)) / 1e5
soundspeed_eff = np.sqrt((norm / density)) / 1e5

soundspeed = soundspeed.flatten()
soundspeed_eff = soundspeed_eff.flatten()
density = density.flatten()
logdensity = np.log10(density)

plt.hist2d(logdensity, soundspeed, bins=100, norm=LogNorm())
plt.colorbar()
plt.savefig('soundspeed_density_hist.png')

plt.clf()

plt.hist2d(logdensity, soundspeed_eff, bins=100, norm=LogNorm())
plt.colorbar()
plt.savefig('soundspeed_eff_density_hist.png')
