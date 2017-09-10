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

density = np.array(ad[fields['density']][:])
pressure = np.array(ad[fields['pressure']][:])

filename = 'effective_pressure_RD0000.hdf5'
effective_pressure_file = h5py.File(filename)
p_eff_x = np.array(effective_pressure_file['p_eff_x'][:])
p_eff_y = np.array(effective_pressure_file['p_eff_y'][:])
p_eff_z = np.array(effective_pressure_file['p_eff_z'][:])

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
