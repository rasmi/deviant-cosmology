#!/usr/bin/env python
# convolution_check.py
# convolution_check.py RD0006

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("directory", type=str, help="List one or more directories to analyze.")
args = parser.parse_args()
directory = args.directory

import numpy as np
import h5py
import yt

fields = {
    'density': ('gas', 'density'),
    'pressure': ('gas', 'pressure'),
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

for fieldname, fieldvalue in fields.iteritems():
    slice_original = yt.SlicePlot(ds, 'z', fieldvalue)
    slice_smoothed = yt.SlicePlot(convolution_ds, 'z', fieldvalue)

    slice_original.save('%s_slice_%s.png' % (fieldname, directory))
    slice_smoothed.save('%s_slice_smoothed_%s.png' % (fieldname, directory))