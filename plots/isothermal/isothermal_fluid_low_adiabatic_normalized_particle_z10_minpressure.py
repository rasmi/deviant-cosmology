import os
import re
import numpy as np
import matplotlib.pyplot as plt

result_dir = '../../results/'
results = os.listdir(result_dir)

isothermalpattern = re.compile(r'_iso(\d+)')
testgrowthpattern = re.compile(r'testgrowthcs(\d+)')
npattern = re.compile(r'_n(\d+)')

soundspeeds = ['10','30','50','100','200','300']

simtypes = ['fluid']
for simtype in simtypes:
    params = [simtype,'b100','n1024','t0.005','h2','iso','z10_','z100']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    filenames.append('fluid_b100_n1024_t0.005_h2_z100_z10.out')

    base = 'particle_b100_n1024_t0.005_h2_z100_z10.out'
    kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)

    for filename in filenames:
        if 'iso' in filename and 'minpressure16' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if isothermal in soundspeeds:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                ps = (ps - ps_base)/ps_base
                plt.semilogx(kvalues, ps, '-', label='Isothermal fluid cs='+isothermal)
        elif filename is 'fluid_b100_n1024_t0.005_h2_z100_z10.out': 
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            ps = (ps - ps_base)/ps_base
            plt.semilogx(kvalues, ps, '--', label='Adiabatic fluid')

base = 'particle_b400_n1024_t0.005_h2_z100_z10.out'
kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)
kvalues_base = kvalues_base[kvalues_base < 10]
ps_base = ps_base[:len(kvalues_base)]

simtypes = ['fluid']
for simtype in simtypes:
    params = [simtype,'b400','n1024','t0.005','h2','iso','z10_','z100']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    filenames.append('fluid_b400_n1024_t0.005_h2_z100_z10.out')
    for filename in filenames:
        if 'iso' in filename and 'minpressure16' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if int(isothermal) <= 300:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                kvalues = kvalues[:len(kvalues_base)]
                ps = ps[:len(kvalues)]
                ps = (ps - ps_base)/ps_base
                style = '-'
                plt.semilogx(kvalues, ps, style, label=None)
        elif filename is 'fluid_b400_n1024_t0.005_h2_z100_z10.out': 
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            kvalues = kvalues[:len(kvalues_base)]
            ps = ps[:len(kvalues)]
            ps = (ps - ps_base)/ps_base
            plt.semilogx(kvalues, ps, '--', label=None)

base = 'particle_b200_n1024_t0.005_h2_z10.out'

kvalues_base, ps_base = np.loadtxt(result_dir+base, unpack=True)
kvalues_base = kvalues_base[kvalues_base < 10]
ps_base = ps_base[:len(kvalues_base)]
simtypes = ['fluid']
for simtype in simtypes:
    params = [simtype,'b200','n1024','t0.005','h2','iso','z10_','z100']
    filenames = [filename for filename in results if all(param in filename for param in params)]
    filenames.append('fluid_b200_n1024_t0.005_h2_z10.out')
    for filename in filenames:
        if 'iso' in filename and 'minpressure16' in filename:
            isothermal = isothermalpattern.findall(filename)[0]
            if int(isothermal) <= 300:
                n = npattern.findall(filename)[0]
                kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
                kvalues = kvalues[:len(kvalues_base)]
                ps = ps[:len(kvalues)]
                ps = (ps - ps_base)/ps_base
                style = '-'
                plt.semilogx(kvalues, ps, style, label=None)
        elif filename is 'fluid_b200_n1024_t0.005_h2_z100_z10.out': 
            kvalues, ps = np.loadtxt(result_dir+filename, unpack=True)
            kvalues = kvalues[:len(kvalues_base)]
            ps = ps[:len(kvalues)]
            ps = (ps - ps_base)/ps_base
            plt.semilogx(kvalues, ps, '--', label=None)

filenames = [filename for filename in results if 'testgrowth' in filename]
for filename in filenames:
    testgrowth = testgrowthpattern.findall(filename)[0]
    if testgrowth in soundspeeds:
        label = 'predicted cs='+testgrowth
        col1, kvalues, linearpower, col4, col5, sqrtsuppression = np.loadtxt(result_dir+filename, unpack=True)
        style = '-x'
        ps = (sqrtsuppression**2) - 1
        #ps /= 4*np.pi**2
        #plt.semilogx(kvalues, ps, style, label=label)

plt.xlim([0.1,7.0])
plt.ylim([-0.3,0.1])
plt.xlabel('$k \, (h/Mpc)$', fontsize=14)
plt.ylabel('$\delta P(k)$', fontsize=14)
plt.title('Relative Power Spectrum, Isothermal and Adiabatic Fluid Comparison z=10')
plt.legend(numpoints=1, loc='best', fontsize=10)
plt.savefig('isothermal_fluid_low_adiabatic_normalized_particle_z10_minpressure.png')

plt.show()