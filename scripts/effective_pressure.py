#!/usr/bin/env python
# effective_pressure.py
# effective_pressure.py RD0006

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("directory", type=str, help="List one or more directories to analyze.")
args = parser.parse_args()
directory = args.directory

import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['agg.path.chunksize'] = 10000
import matplotlib.pyplot as plt
import numpy as np
import yt
import h5py

fields = {
    'density': ('gas', 'density'),
    'pressure': ('gas', 'pressure'),
    'velocity_x': ('gas', 'velocity_x'),
    'velocity_y': ('gas', 'velocity_y'),
    'velocity_z': ('gas', 'velocity_z')
}

ds = yt.load(directory+'/'+directory)
ad = ds.all_data()

density = ad[fields['density']]

velocity_x = ad[fields['velocity_x']]
velocity_y = ad[fields['velocity_y']]
velocity_z = ad[fields['velocity_z']]

def compute_effective_pressure(velocity):
    dv = np.diff(velocity)
    dv[dv > 0] = 0
    dv = np.square(dv)
    dv *= 2*density[:-1]

    return dv

p_eff_x = compute_effective_pressure(velocity_x)
p_eff_y = compute_effective_pressure(velocity_y)
p_eff_z = compute_effective_pressure(velocity_z)

pressure_file = h5py.File('effective_pressure_%s.hdf5' % directory, 'w')
pressure_file.create_dataset('p_eff_x', data=p_eff_x)
pressure_file.create_dataset('p_eff_y', data=p_eff_y)
pressure_file.create_dataset('p_eff_z', data=p_eff_z)
pressure_file.close()

subset = np.random.choice(len(p_eff_x), 1000)

for i, pressure in enumerate([p_eff_x[subset], p_eff_y[subset], p_eff_z[subset]]):
    fig = plt.figure()
    ax = plt.gca()
    ax.scatter(density[:-1][subset], pressure, edgecolors='none')
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xlabel('$\\rho$')
    ax.set_ylabel('$P_{eff}$')
    fig.savefig('effective_pressure_%s_%d.png' % (directory, i))
    fig.clf()