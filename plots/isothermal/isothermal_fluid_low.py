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
    params = [simtype,'b100','n512','t0.005','h2','isothermal']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    base = 'fluid_b100_n512_t0.005_h2_z50.out'
    
    kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

    for filename in filenames:
        if 'isothermal' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if int(isothermal) < 300:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                ps = (ps - ps_base)/ps_base
                style = '--' if 'particle' in filename else '-'
                plt.semilogx(kvalues, ps, style, label=simtype+' cs='+isothermal)

# Sort legend numerically by sound speed.
handles, labels = plt.gca().get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda item:  int(item[1].split(' ')[1].split('=')[1]))
handles2, labels2 = zip(*hl)

plt.xlim([1e-1,1e0])
plt.ylim([-0.1,0.1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Isothermal Fluid Comparison, Low Sound Speeds')
plt.legend(handles2, labels2, numpoints=1, loc='best')
plt.savefig('isothermal_fluid_low.png')

plt.show()