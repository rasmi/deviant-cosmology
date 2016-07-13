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
    'pressure': ('gas', 'pressure')
}

ds = yt.load(directory+'/'+directory)

convolution_file = h5py.File('convolution_2d_%s.hdf5' % directory, 'r')

density_data = np.array(convolution_file['density'][:])
pressure_data = np.array(convolution_file['pressure'][:])

density_slice = yt.SlicePlot(ds, 'z', fields['density'])
pressure_slice = yt.SlicePlot(ds, 'z', fields['pressure'])
density_smoothed_slice = yt.ImageArray(density_data, info={'field': fields['density']})
pressure_smoothed_slice = yt.ImageArray(pressure_data, info={'field': fields['pressure']})

density_slice.save('density_slice_2d_%s.png' % directory)
pressure_slice.save('pressure_slice_2d_%s.png' % directory)
density_smoothed_slice.save('density_slice_smoothed_2d_%s.png' % directory)
pressure_smoothed_slice.save('pressure_slice_smoothed_2d_%s.png' % directory)