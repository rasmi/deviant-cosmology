# modifyGridDensity.py
# Divide GridDensity by the baryon fraction to scale up baryon density generated by MUSIC.

import h5py

f = h5py.File('GridDensity', 'r+')
f['GridDensity'][...] = f['GridDensity'][...]*(f.attrs['omega_m']/f.attrs['omega_b'])
f.close()