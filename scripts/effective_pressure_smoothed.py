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
    'velocity_x': ('gas', 'velocity_x'),
    'velocity_y': ('gas', 'velocity_y'),
    'velocity_z': ('gas', 'velocity_z')
}

ds = yt.load(directory+'/'+directory)

convolution_file = h5py.File('convolution_%s.hdf5' % directory, 'r')

convolution_data = {}

for fieldname, fieldvalue in fields.iteritems():
    field = np.array(convolution_file[fieldname][:])
    convolution_data[fieldvalue] = field

bbox = np.array([[-1.0, 1.0], [-1.0, 1.0], [-1.0, 1.0]])
data_shape = convolution_ds.values()[0].shape

convolution_ds = yt.load_uniform_grid(convolution_data, data_shape, length_unit=ds.length_unit, bbox=bbox)

ad = convolution_ds.all_data()

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

pressure_file = h5py.File('effective_pressure_smoothed_%s.hdf5' % directory, 'w')
pressure_file.create_dataset('p_eff_x', data=p_eff_x)
pressure_file.create_dataset('p_eff_y', data=p_eff_y)
pressure_file.create_dataset('p_eff_z', data=p_eff_z)
pressure_file.close()

subset = np.random.choice(len(p_eff_x), 1000)

pressure_subset_file = h5py.File('effective_pressure_smoothed_subset_%s.hdf5' % directory, 'w')
pressure_subset_file.create_dataset('p_eff_x', data=p_eff_x[subset])
pressure_subset_file.create_dataset('p_eff_y', data=p_eff_y[subset])
pressure_subset_file.create_dataset('p_eff_z', data=p_eff_z[subset])
pressure_subset_file.create_dataset('density', data=density[:-1][subset])
pressure_subset_file.create_dataset('subset', data=subset)
pressure_subset_file.close()