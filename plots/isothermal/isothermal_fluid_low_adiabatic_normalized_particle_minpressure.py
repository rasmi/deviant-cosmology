import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

isothermalpattern = re.compile(r'_isothermal(\d+)')
npattern = re.compile(r'_n(\d+)')

base = 'particle_b100_n1024_t0.005_h2_z100.out'
kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)
outofrange = len(kvalues_base) - len(kvalues_base[kvalues_base > 0.2])
kvalues_base = kvalues_base[kvalues_base > 0.2]
ps_base = ps_base[outofrange:]

simtypes = ['fluid']
for simtype in simtypes:
    params = [simtype,'b100','n1024','t0.005','h2','isothermal', 'z100']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    filenames.append('fluid_b100_n1024_t0.005_h2_z100.out')

    for filename in filenames:
        if 'isothermal' in filename and 'minpressure16' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if int(isothermal) <= 300:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                kvalues = kvalues[outofrange:]
                ps = ps[outofrange:]
                ps = (ps - ps_base)/ps_base
                style = '-'
                plt.semilogx(kvalues, ps, style, label='Isothermal fluid cs='+isothermal)
        elif filename is 'fluid_b100_n1024_t0.005_h2_z100.out': 
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            kvalues = kvalues[outofrange:]
            ps = ps[outofrange:]
            ps = (ps - ps_base)/ps_base
            plt.semilogx(kvalues, ps, '--', label='Adiabatic fluid')

base = 'particle_b400_n1024_t0.005_h2_z100.out'
kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)
kvalues_base = kvalues_base[kvalues_base < 10]
ps_base = ps_base[:len(kvalues_base)]

simtypes = ['fluid']
for simtype in simtypes:
    params = [simtype,'b400','n1024','t0.005','h2','isothermal', 'z100']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    filenames.append('fluid_b400_n1024_t0.005_h2_z100.out')

    for filename in filenames:
        if 'isothermal' in filename and 'minpressure16' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if int(isothermal) <= 300:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                kvalues = kvalues[:len(kvalues_base)]
                ps = ps[:len(kvalues)]
                ps = (ps - ps_base)/ps_base
                style = '-'
                plt.semilogx(kvalues, ps, style, label=None)
        elif filename is 'fluid_b400_n1024_t0.005_h2_z100.out': 
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            kvalues = kvalues[:len(kvalues_base)]
            ps = ps[:len(kvalues)]
            ps = (ps - ps_base)/ps_base
            plt.semilogx(kvalues, ps, '--', label=None)

base = 'particle_b200_n1024_t0.005_h2_z100.out'
kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)
kvalues_base = kvalues_base[kvalues_base < 10]
ps_base = ps_base[:len(kvalues_base)]

simtypes = ['fluid']
for simtype in simtypes:
    params = [simtype,'b200','n1024','t0.005','h2','isothermal', 'z100']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    filenames.append('fluid_b200_n1024_t0.005_h2_z100.out')

    for filename in filenames:
        if 'isothermal' in filename and 'minpressure16' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if int(isothermal) <= 300:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                kvalues = kvalues[:len(kvalues_base)]
                ps = ps[:len(kvalues)]
                ps = (ps - ps_base)/ps_base
                style = '-'
                plt.semilogx(kvalues, ps, style, label=None)
        elif filename is 'fluid_b200_n1024_t0.005_h2_z100.out': 
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            kvalues = kvalues[:len(kvalues_base)]
            ps = ps[:len(kvalues)]
            ps = (ps - ps_base)/ps_base
            plt.semilogx(kvalues, ps, '--', label=None)

_, linear_kvalues, linear_ps, nonlinear_ps = np.loadtxt(result_dir+'testPk0.dat', unpack=True)
linear_ps = (linear_ps - nonlinear_ps)/nonlinear_ps
plt.semilogx(linear_kvalues, linear_ps, '-x', label='Predicted linear particle')

_, linear_kvalues_400, _, nonlinear_ps_400, linear_ps_400, oneloop_400 = np.loadtxt(result_dir+'testPk0.400.dat', unpack=True)
linear_ps_400 = (linear_ps_400 - nonlinear_ps_400)/nonlinear_ps_400
oneloop_400 = (oneloop_400 - nonlinear_ps_400)/nonlinear_ps_400
plt.semilogx(linear_kvalues_400, linear_ps_400, '-x', label='linear prediction')
plt.semilogx(linear_kvalues_400, oneloop_400, '-x', label='one-loop')

plt.xlim([0.027,1])
plt.ylim([-1.0,0.3])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Isothermal and Adiabatic Fluid Comparison')
plt.legend(numpoints=1, loc='best')
plt.savefig('isothermal_fluid_low_adiabatic_normalized_particle_minpressure.png')

plt.show()