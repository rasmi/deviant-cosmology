#!/usr/bin/env python
# convolve.py
# convolve.py RD0006

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("directory", type=str, help="List one or more directories to analyze.")
args = parser.parse_args()
directory = args.directory

import numpy as np
import h5py
from scipy.ndimage.filters import gaussian_filter
import yt

convolution_file = h5py.File('convolution_%s.hdf5' % directory, 'w')

fields = {
    'density': ('gas', 'density'),
    'pressure': ('gas', 'pressure'),
    'velocity_x': ('gas', 'velocity_x'),
    'velocity_y': ('gas', 'velocity_y'),
    'velocity_z': ('gas', 'velocity_z')
}

ds = yt.load(directory+'/'+directory)
ad = ds.covering_grid(level=0, left_edge=[0.0, 0.0, 0.0], dims=ds.domain_dimensions)

sigma = 2.0/3.0

for fieldname, fieldvalue in fields.iteritems():
    field = ad[fieldvalue]
    convolution = gaussian_filter(field, sigma=sigma)
    convolution_file.create_dataset(fieldname, data=convolution)

convolution_file.close()