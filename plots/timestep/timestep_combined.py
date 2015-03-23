import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

tpattern = re.compile(r'_t(\d+.\d+)')

simtypes = ['particle', 'fluid']
for simtype in simtypes:
	filenames = [filename for filename in results if simtype in filename and 'n256' in filename and 'z50' in filename and 'h2' in filename]
	base = [filename for filename in results if 't0.0015' in filename and 'particle' in filename][0]
	
	kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

	for filename in filenames:
		t = tpattern.findall(filename)[0]
		kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
		ps = (ps - ps_base)/ps_base

		style = '-' if simtype is 'particle' else '--'
		plt.semilogx(kvalues, ps, style, label=simtype+' dt='+t)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, dt Comparison at Z=0')
plt.legend(numpoints=1, loc='best')
plt.savefig('timestep_combined.png')

plt.show()