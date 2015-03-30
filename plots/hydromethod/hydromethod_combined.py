import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

tpattern = re.compile(r'_t(\d+.\d+)')
hpattern = re.compile(r'_h(\d+)')

simtypes = ['fluid']
for simtype in simtypes:
	params = [simtype,'b100','n256','z50']
	filenames = [filename for filename in results if all(param in filename for param in params)]
	base = [filename for filename in filenames if 't0.0015' in filename][0]

	kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

	for filename in filenames:
		t = tpattern.findall(filename)[0]
		h = hpattern.findall(filename)[0]
		kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
		ps = (ps - ps_base)/ps_base

		style = '-' if h is '0' else '--'
		plt.semilogx(kvalues, ps, style, label=simtype+' t='+t+' H='+h)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, HydroMethod Comparison at Z=0')
plt.legend(numpoints=1, loc='best')
plt.savefig('hydromethod_combined.png')

plt.show()