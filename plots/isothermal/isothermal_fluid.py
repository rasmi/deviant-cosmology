import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

isothermalpattern = re.compile(r'_isothermal(\d+)')
npattern = re.compile(r'_n(\d+)')

simtypes = ['fluid']
for simtype in simtypes:
    params = [simtype,'b100','n256','t0.005','h2','isothermal']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    base = 'particle_b100_n512_t0.005_h2_z50.out'
    
    kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

    for filename in filenames:
        isothermal = isothermalpattern.findall(filename)[0]
        n = npattern.findall(filename)[0]
        print filename
        kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
        ps = (ps - ps_base)/ps_base

        style = '--' if 'particle' in filename else '-'
        plt.semilogx(kvalues, ps, style, label=simtype+' n='+n+' cs='+isothermal)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Isothermal Fluid Comparison at Z=0')
plt.legend(numpoints=1, loc='best')
plt.savefig('isothermal_fluid.png')

plt.show()