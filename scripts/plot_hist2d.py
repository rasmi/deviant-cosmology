#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import h5py

filename = 'effective_pressure_RD0000.hdf5'
effective_pressure_file = h5py.File(filename)
p_eff_x = np.array(effective_pressure_file['p_eff_x'][:])
p_eff_y = np.array(effective_pressure_file['p_eff_y'][:])
p_eff_z = np.array(effective_pressure_file['p_eff_z'][:])
density = np.array(effective_pressure_file['density'][:])
pressure = np.array(effective_pressure_file['pressure'][:])
norm = np.sqrt(np.square(p_eff_x) + np.square(p_eff_y) + np.square(p_eff_z))
soundspeed = np.sqrt((pressure / density)) / 1e5
soundspeed_eff = np.sqrt((norm / density)) / 1e5

plt.hist2d(np.log10(density), soundspeed, bins=100, norm=LogNorm())
plt.colorbar()
plt.savefig('soundspeed_density_hist%s.png' % pressuretype)

plt.clf()

plt.hist2d(np.log10(density), soundspeed_eff, bins=100, norm=LogNorm())
plt.colorbar()
plt.savefig('soundspeed_eff_density_hist%s.png' % pressuretype)
