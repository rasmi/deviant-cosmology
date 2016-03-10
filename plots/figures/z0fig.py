import os
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from styles import *

result_dir = '../../results/'
paper_dir = '../../paper/'
results = os.listdir(result_dir)

isothermalpattern = re.compile(r'_isothermal(\d+)')
npattern = re.compile(r'_n(\d+)')

boxsizes = ['b200']
soundspeeds = ['50','100','200','300']

for boxsize in boxsizes:
    params = [boxsize,'fluid', 'n1024','t0.005','h2','isothermal', 'z100']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    filenames.append('fluid_'+boxsize+'_n1024_t0.005_h2_z100.out')

    base = 'particle_'+boxsize+'_n1024_t0.005_h2_z100.out'
    kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

    for filename in filenames:
        if 'isothermal' in filename and 'minpressure16' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if isothermal in soundspeeds:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                ps = (ps - ps_base)/ps_base
                label = 'Isothermal fluid $c_s='+isothermal+'$' if boxsize in labels else None
                plt.semilogx(kvalues, ps, linestyles['isothermal'], label=label, color=linecolors[isothermal], alpha=lineopacity[isothermal], linewidth=linewidth['simulated'])
        elif filename == 'fluid_'+boxsize+'_n1024_t0.005_h2_z100.out':
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            ps = (ps - ps_base)/ps_base
            label = 'Adiabatic fluid' if boxsize in labels else None
            plt.semilogx(kvalues, ps, linestyles['adiabatic'], label=label, color=linecolors[isothermal], alpha=lineopacity['adiabatic'], linewidth=linewidth['simulated'])

_, linear_kvalues_400, _, nonlinear_ps_400, linear_ps_400, oneloop_400 = np.loadtxt(result_dir+'testPk0.400.dat', unpack=True)
linear_ps_400 = (linear_ps_400 - nonlinear_ps_400)/nonlinear_ps_400
oneloop_400 = (oneloop_400 - nonlinear_ps_400)/nonlinear_ps_400
plt.semilogx(linear_kvalues_400, linear_ps_400, linestyles['prediction'], label='Linear prediction', color=linecolors['prediction'], alpha=lineopacity['prediction_400'], linewidth=linewidth['analytic'])
plt.semilogx(linear_kvalues_400, oneloop_400, linestyles['oneloop'], label='One-loop', color=linecolors['oneloop'], alpha=lineopacity['oneloop'], linewidth=linewidth['analytic'])

def sortlabels(item):
    if len(item[1].split(' ')) > 2:
        return int(item[1].split(' ')[2].split('=')[1].replace('$',''))
    else:
        return item[1].split(' ')[0]

handles, labels = plt.gca().get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda item: sortlabels(item))
handles2, labels2 = zip(*hl)

plt.xlim([5.839613682298916419e-02,2.0])
plt.ylim([-1.0,0.5])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.legend(handles2, labels2, numpoints=1, loc='lower left', fontsize=10, frameon=False)
plt.savefig(paper_dir+'z0fig.pdf', format='pdf')

plt.show()