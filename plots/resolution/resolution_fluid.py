import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

npattern = re.compile(r'_n(\d+)')

simtypes = ['fluid']
for simtype in simtypes:
	filenames = [filename for filename in results if simtype in filename and 'z50' in filename and 'h2' in filename and 't0.005' in filename]
	base = [filename for filename in filenames if 'n512' in filename][0]

	kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

	for filename in filenames:
		n = npattern.findall(filename)[0]
		kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
		ps = (ps - ps_base)/ps_base

		style = '-'
		plt.semilogx(kvalues, ps, style, label=simtype+' n='+n)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Fluid Resolution Comparison at Z=0')
plt.legend(numpoints=1, loc='best')
plt.savefig('resolution_fluid.png')

plt.show()