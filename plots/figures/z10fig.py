import os
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from styles import *

result_dir = '../../results/'
paper_dir = '../../paper/'
results = os.listdir(result_dir)

isothermalpattern = re.compile(r'_iso(\d+)')
testgrowthpattern = re.compile(r'testgrowthcs(\d+)')
npattern = re.compile(r'_n(\d+)')

boxsizes = ['b100','b200','b400']
soundspeeds = ['50','100','200','300']

for boxsize in boxsizes:
    params = [boxsize,'fluid', 'n1024','t0.005','h2','iso','z10_','z100']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    filenames.append('fluid_'+boxsize+'_n1024_t0.005_h2_z100_z10.out')

    base = 'particle_'+boxsize+'_n1024_t0.005_h2_z100_z10.out'
    kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

    for filename in filenames:
        if 'iso' in filename and 'minpressure16' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if isothermal in soundspeeds:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                ps = (ps - ps_base)/ps_base
                label = 'Isothermal fluid cs='+isothermal if boxsize in labels else None
                plt.semilogx(kvalues, ps, linestyles['isothermal'], label=label, color=linecolors[isothermal], alpha=lineopacity[isothermal])
        elif filename == 'fluid_'+boxsize+'_n1024_t0.005_h2_z100_z10.out':
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            ps = (ps - ps_base)/ps_base
            label = 'Adiabatic fluid' if boxsize in labels else None
            plt.semilogx(kvalues, ps, linestyles['adiabatic'], label=label, color=linecolors['adiabatic'], alpha=lineopacity[boxsize])

filenames = [filename for filename in results if 'testgrowth' in filename]
for filename in filenames:
    testgrowth = testgrowthpattern.findall(filename)[0]
    if testgrowth in soundspeeds:
        label = 'predicted cs='+testgrowth
        col1, kvalues, linearpower, col4, col5, sqrtsuppression = np.loadtxt(result_dir+filename, unpack=True)
        style = '-x'
        ps = (sqrtsuppression**2) - 1
        #plt.semilogx(kvalues, ps, style, label=label)

plt.xlim([0.1,7.0])
plt.ylim([-0.3,0.1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Isothermal and Adiabatic Fluid Comparison z=10')
plt.legend(numpoints=1, loc='best', fontsize=10)
plt.savefig(paper_dir+'z10fig.pdf', format='pdf')

plt.show()