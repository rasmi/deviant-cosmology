import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

zpattern = re.compile(r'_z(\d+)')

simtypes = ['particle','fluid']
for simtype in simtypes:
	params = [simtype,'b100','n256','t0.005','h2']
	filenames = [filename for filename in results if all(param in filename for param in params)]
	base_params = ['particle','b100','n256','t0.005','h2','z100']
	base = [filename for filename in results if all(param in filename for param in base_params)][0]

	kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

	for filename in filenames:
		zstart = zpattern.findall(filename)[0]
		kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
		ps = (ps - ps_base)/ps_base

		style = '-' if simtype is 'particle' else '--'
		plt.semilogx(kvalues, ps, style, label=simtype+' zstart='+zstart)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, zstart Comparison at Z=0')
plt.legend(numpoints=1, loc='best')
plt.savefig('zstart_combined.png')

plt.show()