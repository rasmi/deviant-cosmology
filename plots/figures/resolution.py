import os
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.lines as mlines
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from styles import *

result_dir = '../../results/'
paper_dir = '../../paper/'
results = os.listdir(result_dir)

npattern = re.compile(r'_n(\d+)')

simtypes = ['particle', 'fluid']
for simtype in simtypes:
	params = [simtype, 'b200', 't0.005', 'h2', 'z50']
	filenames = [filename for filename in results if all(param in filename for param in params)]
	#base = 'particle_b200_n1024_t0.005_h2_z50.out'
	base_params = ['particle', 'b200', 't0.005', 'h2', 'z50', 'n1024']
	base = [filename for filename in results if all(param in filename for param in base_params)][0]
	
	kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

	for filename in filenames:
		n = npattern.findall(filename)[0]
		if int(n) > 128:
			kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
			ps = (ps - ps_base)/ps_base

			style = '-' if simtype is 'particle' else '--'
			plt.semilogx(kvalues, ps, style, color=linecolors['adiabatic'], alpha=lineopacity[n], linewidth=linewidth[n], label=simtype+' n='+n)

handles = []
labels = []

handles.append(mlines.Line2D([], [],  linestyle=linestyles['adiabatic'], color='k', alpha=lineopacity['adiabatic']))
labels.append('Adiabatic fluid')

handles.append(mlines.Line2D([], [], linestyle=linestyles['prediction'], color='k', alpha=lineopacity['adiabatic']))
labels.append('Particle')

for n in ['1024', '512', '256']:
    handles.append(mlines.Line2D([], [], color=linecolors['adiabatic'], alpha=lineopacity[n], linewidth=linewidth[n]))
    labels.append('$n='+n+'$')

plt.xlim([1e-1,1e1])
plt.xlabel('$k \,\, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.legend(handles, labels, numpoints=1, loc='lower left', prop=fm.FontProperties(family='serif', size=10), frameon=False)
plt.savefig(paper_dir+'resolution.pdf', format='pdf')