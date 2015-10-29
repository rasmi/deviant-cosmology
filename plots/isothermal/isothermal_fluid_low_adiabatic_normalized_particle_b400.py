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
    params = [simtype,'b400','n1024','t0.005','h2','isothermal']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    filenames.append('fluid_b400_n1024_t0.005_h2_z50.out')
    base = 'particle_b400_n1024_t0.005_h2_z50.out'
    
    kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

    for filename in filenames:
        if 'isothermal' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if int(isothermal) <= 400:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                ps = (ps - ps_base)/ps_base
                plt.semilogx(kvalues, ps, '-', label='Isothermal fluid cs='+isothermal)
        elif filename is 'fluid_b400_n1024_t0.005_h2_z50.out': 
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            ps = (ps - ps_base)/ps_base
            plt.semilogx(kvalues, ps, '--', label='Adiabatic fluid')

plt.xlim([0.02,5e0])
plt.ylim([-1,0.5])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Isothermal and Adiabatic Fluid Comparison 400Mpc/h')
plt.legend(numpoints=1, loc='best')
plt.savefig('isothermal_fluid_low_adiabatic_normalized_particle_b400.png')

plt.show()