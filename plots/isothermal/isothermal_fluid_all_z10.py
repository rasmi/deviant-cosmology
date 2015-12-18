import os
import re
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

result_dir = '../../results/'
results = os.listdir(result_dir)

isothermalpattern = re.compile(r'_iso(\d+)')
testgrowthpattern = re.compile(r'testgrowthcs(\d+)')

simtypes = ['fluid']
for simtype in simtypes:
    params = [simtype,'b100','n512','t0.005','h2','iso','z10_']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    for filename in filenames:
        label = simtype
        isothermal = isothermalpattern.findall(filename)[0]
        if isothermal in ['10','30','100']:
            label += ' cs='+isothermal
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            style = '-'
            plt.loglog(kvalues, ps, style, label=label)



filenames = [filename for filename in results if 'testgrowth' in filename]
for filename in filenames:
    testgrowth = testgrowthpattern.findall(filename)[0]
    if testgrowth in ['10','40','100']:
        label = 'predicted cs='+testgrowth
        col1, kvalues, linearpower, col4, col5, sqrtsuppression = np.loadtxt(result_dir+filename, unpack=True)
        style = '--'
        ps = linearpower * (sqrtsuppression**2)
        ps /= (2*np.pi)**3
        plt.loglog(kvalues, ps, style, label=label)

'''
for filename in filenames:
    testgrowth = testgrowthpattern.findall(filename)[0]
    label = 'predicted cs='+testgrowth
    col1, kvalues, linearpower, col4, col5, sqrtsuppression = np.loadtxt(result_dir+filename, unpack=True)
    interpolator = interpolate.BarycentricInterpolator(particlekvalues, particleps)
    interpolatedps = interpolator(kvalues)
    style = '-x'
    ps = interpolatedps * (sqrtsuppression**2)
    plt.loglog(kvalues, ps, style, label=label)
'''
# Sort legend numerically by sound speed.
handles, labels = plt.gca().get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda item:  int(item[1].split(' ')[1].split('=')[1]))
handles2, labels2 = zip(*hl)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$P(k)$', fontsize=14)
plt.title('Power Spectrum, Isothermal Fluid at Z=10')
plt.legend(handles2, labels2, numpoints=1, loc='best')
particleresults = 'particle_b100_n512_t0.005_h2_z10.out'
particlekvalues, particleps = np.loadtxt(result_dir+particleresults, unpack=True)
col1, linearkvalues, linearpower, col4, col5, sqrtsuppression = np.loadtxt(result_dir+'testgrowthcs10.dat', unpack=True)
plt.loglog(particlekvalues, particleps, '-x', label='particle')
plt.loglog(linearkvalues, linearpower/(2*np.pi)**3, '-o', label='linearpower')
plt.savefig('isothermal_fluid_all_z10.png')

plt.show()