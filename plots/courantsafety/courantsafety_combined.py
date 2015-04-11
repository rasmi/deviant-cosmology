import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

cspattern = re.compile(r'_cs(\d+.\d+)')
npattern = re.compile(r'_n(\d+)')
defaultcs = {
	'fluid': '0.5',
	'particle': '0.8'
}

simtypes = ['particle','fluid']
for simtype in simtypes:
	params = [simtype,'b100','t0.005','h2', 'z50']
	filenames = [filename for filename in results if all(param in filename for param in params)]
	filenames = [filename for filename in filenames if any(param in filename for param in ['n128','n256'])]
	base_params = ['b100','t0.005','cs0.1']
	base = [filename for filename in results if all(param in filename for param in base_params)]
	filenames = filenames + [filename for filename in base if simtype in filename]
	base = [filename for filename in base if 'n256' and 'particle' in filename][0]

	kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

	for filename in filenames:
		cs = cspattern.findall(filename)[0] if 'cs' in filename else defaultcs[simtype]
		n = npattern.findall(filename)[0]
		kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
		ps = (ps - ps_base)/ps_base

		style = '-' if cs is not defaultcs[simtype] else '--'
		plt.loglog(kvalues, ps, style, label=simtype+' n='+n+' CS='+cs)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Courant Safety Number Comparison at Z=0')
plt.legend(numpoints=1, loc='best')
plt.savefig('courantsafety_combined.png')

plt.show()