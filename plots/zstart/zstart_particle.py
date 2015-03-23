import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

zpattern = re.compile(r'_z(\d+)')

simtypes = ['particle']
for simtype in simtypes:
	filenames = [filename for filename in results if simtype in filename and 'n256' in filename and 'h2' in filename and 't0.005' in filename]
	base = [filename for filename in filenames if 'z100' in filename][0]

	kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

	for filename in filenames:
		zstart = zpattern.findall(filename)[0]
		kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
		ps = (ps - ps_base)/ps_base

		style = '-'
		plt.semilogx(kvalues, ps, style, label=simtype+' zstart='+zstart)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Particle zstart Comparison at Z=0')
plt.legend(numpoints=1, loc='best')
plt.savefig('zstart_particle.png')

plt.show()