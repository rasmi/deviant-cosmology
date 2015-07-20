import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

isothermalpattern = re.compile(r'_iso(\d+)')

simtypes = ['fluid']
for simtype in simtypes:
    params = [simtype,'b100','n512','t0.005','h2','iso','z8']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    for filename in filenames:
        label = simtype
        isothermal = isothermalpattern.findall(filename)[0]
        label += ' cs='+isothermal
        kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
        style = '-'
        plt.loglog(kvalues, ps, style, label=label)

# Sort legend numerically by sound speed.
handles, labels = plt.gca().get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda item:  int(item[1].split(' ')[1].split('=')[1]))
handles2, labels2 = zip(*hl)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$P(k)$', fontsize=14)
plt.title('Power Spectrum, Isothermal Fluid at Z=8.1')
plt.legend(handles2, labels2, numpoints=1, loc='best')
plt.savefig('isothermal_fluid_all_z8.png')

plt.show()