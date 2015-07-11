import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

isothermalpattern = re.compile(r'_isothermal(\d+)')
npattern = re.compile(r'_n(\d+)')

simtypes = ['fluid', 'particle']
for simtype in simtypes:
    params = [simtype,'b100','n512','t0.005','h2']
    filenames = [filename for filename in results if all(param in filename for param in params)]

    for filename in filenames:
        n = npattern.findall(filename)[0]
        label = simtype
        if 'isothermal' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            label += ' cs='+isothermal
        kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
        style = '--' if 'isothermal' in filename else '-'
        plt.loglog(kvalues, ps, style, label=label)

# Sort legend numerically by sound speed.
def sortlabels(item):
    if len(item[1].split(' ')) > 1:
        return int(item[1].split(' ')[1].split('=')[1])
    else:
        return item[1].split(' ')[0]

handles, labels = plt.gca().get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda item: sortlabels(item))
handles2, labels2 = zip(*hl)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$P(k)$', fontsize=14)
plt.title('Power Spectrum, Fluid and Particle Comparison at Z=0')
plt.legend(handles2, labels2, numpoints=1, loc='best')
plt.savefig('isothermal_fluid_all.png')

plt.show()