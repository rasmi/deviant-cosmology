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
from scipy.signal import fftconvolve
import yt

fields = {
    'density': ('gas', 'density'),
    'pressure': ('gas', 'pressure')
}

def gaussian3D(sigma, start, stop, n):
    xaxis = np.linspace(start, stop, n)
    yaxis = np.linspace(start, stop, n)
    zaxis = np.linspace(start, stop, n)
    x = xaxis[:,None,None]
    y = yaxis[None,:,None]
    z = zaxis[None,None,:]

    sigma_square = sigma**2

    return np.exp(-(x**2 + y**2 + z**2)/(2.0*sigma_square))/(np.sqrt(2.0*np.pi*sigma_square))

sigma = 2.0/3.0
gaussian = gaussian3D(sigma, -100, 100, 1024)

ds = yt.load(directory+'/'+directory)
ad = ds.all_data()

density = ad[fields['density']]
pressure = ad[fields['pressure']]

density = density.reshape(gaussian.shape)
pressure = pressure.reshape(gaussian.shape)

density_convolution = fftconvolve(density, gaussian)
pressure_convolution = fftconvolve(pressure, gaussian)

density_file = h5py.File('density_convolution_%s.hdf5' % directory, 'w')
pressure_file = h5py.File('pressure_convolution_%s.hdf5' % directory, 'w')

density_file.create_dataset('convolution', data=density_convolution)
pressure_file.create_dataset('convolution', data=pressure_convolution)

density_file.close()
pressure_file.close()