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
            speed = isothermalpattern.findall(filename)[0]
            if speed in soundspeeds:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                ps = (ps - ps_base)/ps_base
                plt.semilogx(kvalues, ps, linestyles['isothermal'], color=linecolors[speed], alpha=lineopacity[speed], linewidth=linewidth['simulated'])
        elif filename == 'fluid_'+boxsize+'_n1024_t0.005_h2_z100.out':
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            ps = (ps - ps_base)/ps_base
            plt.semilogx(kvalues, ps, linestyles['adiabatic'], color=linecolors['adiabatic'], alpha=lineopacity['adiabatic'], linewidth=linewidth['simulated'])

_, linear_kvalues_400, _, nonlinear_ps_400, linear_ps_400, oneloop_400 = np.loadtxt(result_dir+'testPk0.400.dat', unpack=True)
oneloop_400 = (oneloop_400 - nonlinear_ps_400)/nonlinear_ps_400
linear_ps_400 = (linear_ps_400 - nonlinear_ps_400)/nonlinear_ps_400
plt.semilogx(linear_kvalues_400, oneloop_400, linestyles['oneloop'], color=linecolors['oneloop'], alpha=lineopacity['oneloop'], linewidth=linewidth['oneloop'])
plt.semilogx(linear_kvalues_400, linear_ps_400, linestyles['prediction'], color=linecolors['prediction'], alpha=lineopacity['prediction'], linewidth=linewidth['prediction'])

handles = []
labels = []
for speed in soundspeeds:
    handles.append(mlines.Line2D([], [], linestyle=linestyles['isothermal'], color=linecolors[speed], alpha=lineopacity[speed], linewidth=linewidth['simulated']))
    labels.append('$c_s='+speed+'$')

handles.append(mlines.Line2D([], [], linestyle=linestyles['adiabatic'], color=linecolors['adiabatic'], alpha=lineopacity['adiabatic'], linewidth=linewidth['simulated']))
labels.append('Adiabatic fluid')

handles.append(mlines.Line2D([], [], linestyle=linestyles['oneloop'], color=linecolors['oneloop'], alpha=lineopacity['oneloop'], linewidth=linewidth['oneloop']))
labels.append('One-loop')

handles.append(mlines.Line2D([], [], linestyle=linestyles['prediction'], color=linecolors['prediction'], alpha=lineopacity['prediction'], linewidth=linewidth['prediction']))
labels.append('Linear prediction')


plt.xlim([5.839613682298916419e-02,2.0])
plt.ylim([-1.0,0.5])
plt.xlabel('$k \,\, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.legend(handles, labels, numpoints=1, loc='lower left', prop=fm.FontProperties(family='serif', size=10), frameon=False)
plt.savefig(paper_dir+'z0fig.pdf', format='pdf')

plt.show()