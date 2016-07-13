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

convolution_file = h5py.File('convolution_%s.hdf5' % directory, 'r')

density_data = np.array(convolution_file['density'][:])
pressure_data = np.array(convolution_file['pressure'][:])

convolution_data = {
    fields['density']: density_data,
    fields['pressure']: pressure_data
}

bbox = np.array([[-1.0, 1.0], [-1.0, 1.0], [-1.0, 1.0]])

convolution_ds = yt.load_uniform_grid(convolution_data, density_data.shape, length_unit=ds.length_unit, bbox=bbox)

density_slice = yt.SlicePlot(ds, 'z', fields['density'])
pressure_slice = yt.SlicePlot(ds, 'z', fields['pressure'])
density_smoothed_slice = yt.SlicePlot(convolution_ds, 'z', fields['density'])
pressure_smoothed_slice = yt.SlicePlot(convolution_ds, 'z', fields['pressure'])

density_slice.save('density_slice_%s.png' % directory)
pressure_slice.save('pressure_slice_%s.png' % directory)
density_smoothed_slice.save('density_slice_smoothed_%s.png' % directory)
pressure_smoothed_slice.save('pressure_slice_smoothed_%s.png' % directory)