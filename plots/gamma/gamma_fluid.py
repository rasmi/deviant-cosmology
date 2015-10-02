import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'

base = 'fluid_b100_n1024_t0.005_h2_z50.out'
filenames = ['fluid_b100_n1024_t0.005_gamma43.out', 'fluid_b100_n1024_t0.005_h2_z50.out']

kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

for filename in filenames:
	kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
	ps = (ps - ps_base)/ps_base

	style = '-'
	label = 'gamma = 4/3' if 'gamma43' in filename else 'gamma = 5/3'
	plt.semilogx(kvalues, ps, style, label=label)

plt.xlim([1e-1,1e1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Fluid Gamma Comparison')
plt.legend(numpoints=1, loc='best')
plt.savefig('gamma_fluid.png')

plt.show()