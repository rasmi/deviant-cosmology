#!/usr/bin/env python
# convolve_2d.py
# convolve_2d.py RD0006

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("directory", type=str, help="List one or more directories to analyze.")
args = parser.parse_args()
directory = args.directory

import numpy as np
import h5py
import yt
from astropy.convolution import Gaussian2DKernel, convolve_fft

fields = {
    'density': ('gas', 'density'),
    'pressure': ('gas', 'pressure')
}

ds = yt.load(directory+'/'+directory)
slice = ds.slice('z', 0)

resolution = ds.domain_dimensions

sigma = 2.0/3.0
gaussian = Gaussian2DKernel(sigma)

density = slice[fields['density']]
pressure = slice[fields['pressure']]

density = density.reshape(ds.domain_dimensions[:-1])
pressure = pressure.reshape(ds.domain_dimensions[:-1])

density_convolution = convolve_fft(density, gaussian, allow_huge=True)
pressure_convolution = convolve_fft(pressure, gaussian, allow_huge=True)

convolution_file = h5py.File('convolution_2d_%s.hdf5' % directory, 'w')

convolution_file.create_dataset('density', data=density_convolution)
convolution_file.create_dataset('pressure', data=pressure_convolution)

convolution_file.close()