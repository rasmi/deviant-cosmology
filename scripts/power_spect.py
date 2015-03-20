# power_spect.py
# Generate the power spectrum of a given enzo directory.
# Specify --type fluid or particle.
# Optionally specify --output filename.
# power_spect.py --type fluid DD0046

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("directory", type=str, help="List one or more directories to analyze.")
parser.add_argument("--type", type=str, required=True, help="fluid or particle")
parser.add_argument("--output", type=str, help="output file name")
args = parser.parse_args()

import numpy as np
from yt.mods import *

ytfield = ''
if args.type == 'particle':
	ytfield = 'all_cic'
elif args.type == 'fluid':
	ytfield = 'density'

directory = args.directory

# Load field and parse attributes.
pf = load(directory+'/'+directory)

z = pf.current_redshift
redshift = str(int(z))
box_size_in_Mpc = float(pf.length_unit)
n = pf.domain_dimensions[0]

# Create covering grid (with even spacing) of density field and compute overdensity
all_data_level_0 = pf.covering_grid(level=0, left_edge=pf.domain_left_edge, dims=pf.domain_dimensions)

# Generate dm density field
field = all_data_level_0[ytfield]

# Convert to overdensity
field /= field.mean()

# FFT and take modulus squared (n^6 factor is to renormalize)
field_fft = np.abs(np.fft.fftn(field))
field_fft *= field_fft/(n**6)

# compute k field
dim = field_fft.shape[0]
k1d = np.minimum(np.arange(dim), np.arange(dim, 0, -1)) * 2.0*np.pi/box_size_in_Mpc
k1d *= k1d
k_3d = np.sqrt(k1d[:, None, None] + k1d[:, None] + k1d)

# compute kmin and kmax
kmin = np.log10(2.0*np.pi*0.99/box_size_in_Mpc)
kmax = np.log10(2.0*np.pi*0.5*dim/box_size_in_Mpc)

# Generate histogram
krange = np.logspace(kmin, kmax, num = 50, endpoint=True)
ps, bin_edges = np.histogram(k_3d, bins=krange, weights=field_fft)
counts, bin_edges = np.histogram(k_3d, bins=krange, weights=None)

# normalize by 4 pi k^2 dk
kvalues = 0.5*(bin_edges[0:-1] + bin_edges[1:])
kwidth = (bin_edges[1:] - bin_edges[0:-1])
ps /= 4.0*np.pi * kvalues**2 * kwidth

# output
if not args.output:
	args.output = 'power_spect_'+args.type+'_n'+str(n)+'.out'

np.savetxt(args.output, zip(kvalues, ps))
