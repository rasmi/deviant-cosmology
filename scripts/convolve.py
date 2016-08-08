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

fields = {
    'density': ('gas', 'density'),
    'pressure': ('gas', 'pressure')
}

ds = yt.load(directory+'/'+directory)
ad = ds.covering_grid(level=0, left_edge=[0.0, 0.0, 0.0], dims=ds.domain_dimensions)

sigma = 2.0/3.0

density = ad[fields['density']]
pressure = ad[fields['pressure']]

density_convolution = gaussian_filter(density, sigma=sigma)
pressure_convolution = gaussian_filter(pressure, sigma=sigma)

convolution_file = h5py.File('convolution_%s.hdf5' % directory, 'w')

convolution_file.create_dataset('density', data=density_convolution)
convolution_file.create_dataset('pressure', data=pressure_convolution)

convolution_file.close()