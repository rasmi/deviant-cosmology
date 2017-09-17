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

boxsizes = ['50', '100', '200']
for boxsize in boxsizes:
	base = 'particle_b{}_n1024_t0.005_h2_z50.out'.format(boxsize)
	kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

	filename = base.replace('particle', 'fluid')
	kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
	ps = (ps - ps_base)/ps_base

	if boxsize == '200':
		# Add one base line at zero.
		plt.semilogx(kvalues, ps_base - ps_base, linestyle=linestyles['prediction'], color=linecolors['prediction'], alpha=lineopacity['adiabatic'])

	plt.semilogx(kvalues, ps, '-',  color=linecolors['adiabatic'], alpha=lineopacity['b'+boxsize], linewidth=linewidth['b'+boxsize])

handles = []
labels = []

handles.append(mlines.Line2D([], [], linestyle=linestyles['prediction'], color=linecolors['prediction'], alpha=lineopacity['adiabatic']))
labels.append('Particle')

for b in ['50', '100', '200']:
    handles.append(mlines.Line2D([], [], color=linecolors['adiabatic'], alpha=lineopacity['b'+b], linewidth=linewidth['b'+b]))
    labels.append('$L='+b+'\, Mpc/h''$')

plt.xlim([1e-1,1e1])
plt.xlabel('$k \,\, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.legend(handles, labels, numpoints=1, loc='lower left', prop=fm.FontProperties(family='serif', size=10), frameon=False)
plt.savefig(paper_dir+'boxsize.pdf', format='pdf')