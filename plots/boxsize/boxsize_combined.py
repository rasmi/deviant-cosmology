import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

bpattern = re.compile(r'_b(\d+)')

simtypes = ['particle','fluid']
for simtype in simtypes:
	params = [simtype,'n256','t0.005','h2','z50']
	filenames = [filename for filename in results if all(param in filename for param in params)]
	base_params = ['particle','n256','t0.005','h2','z50', 'b200']
	base = [filename for filename in results if all(param in filename for param in base_params)][0]
	
	kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

	for filename in filenames:
		b = bpattern.findall(filename)[0]
		kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
		ps = (ps - ps_base)/ps_base

		style = '-' if simtype is 'particle' else '--'
		plt.loglog(kvalues, ps, style, label=simtype+' L='+b+' Mpc/h')

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Boxsize Comparison at Z=0')
plt.legend(numpoints=1, loc='best')
plt.savefig('boxsize_combined.png')

plt.show()