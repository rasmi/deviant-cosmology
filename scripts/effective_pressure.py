#!/usr/bin/env python
# effective_pressure.py
# effective_pressure.py RD0006

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("directory", type=str, help="List one or more directories to analyze.")
args = parser.parse_args()
directory = args.directory

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
ad = ds.covering_grid(level=0, left_edge=[0.0, 0.0, 0.0], dims=ds.domain_dimensions)

density = ad[fields['density']]

velocity_x = ad[fields['velocity_x']]
velocity_y = ad[fields['velocity_y']]
velocity_z = ad[fields['velocity_z']]

def compute_effective_pressure(velocity, axis, density_slice):
    dv = np.diff(velocity, axis=axis)
    dv[dv > 0] = 0
    dv = np.square(dv)
    dv *= 2*density_slice

    return dv

p_eff_x = compute_effective_pressure(velocity_x, 0, density[:-1])
p_eff_y = compute_effective_pressure(velocity_y, 1, density[:,:-1])
p_eff_z = compute_effective_pressure(velocity_z, 2, density[:,:,:-1])

pressure_file = h5py.File('effective_pressure_%s.hdf5' % directory, 'w')
pressure_file.create_dataset('p_eff_x', data=p_eff_x)
pressure_file.create_dataset('p_eff_y', data=p_eff_y)
pressure_file.create_dataset('p_eff_z', data=p_eff_z)
pressure_file.close()

subset = np.random.randint(ds.domain_dimensions[0]-1, size=(1000, 3))
subset_indices = tuple(subset.T)

pressure_subset_file = h5py.File('effective_pressure_subset_%s.hdf5' % directory, 'w')
pressure_subset_file.create_dataset('p_eff_x', data=p_eff_x[subset_indices])
pressure_subset_file.create_dataset('p_eff_y', data=p_eff_y[subset_indices])
pressure_subset_file.create_dataset('p_eff_z', data=p_eff_z[subset_indices])
pressure_subset_file.create_dataset('density', data=density[subset_indices])
pressure_subset_file.create_dataset('subset', data=subset)
pressure_subset_file.close()