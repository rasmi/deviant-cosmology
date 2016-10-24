import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import h5py

def plot_effective_pressure(pressuretype):
    filename = 'effective_pressure_subset%s_RD0000.hdf5' % pressuretype
    effective_pressure_file = h5py.File(filename)
    p_eff_x = np.array(effective_pressure_file['p_eff_x'][:])
    p_eff_y = np.array(effective_pressure_file['p_eff_y'][:])
    p_eff_z = np.array(effective_pressure_file['p_eff_z'][:])
    density = np.array(effective_pressure_file['density'][:])
    pressure = np.array(effective_pressure_file['pressure'][:])
    norm = np.sqrt(np.square(p_eff_x) + np.square(p_eff_y) + np.square(p_eff_z))
    soundspeed = np.sqrt((5.0/3.0) * (pressure / density))
    slope, intercept = np.polyfit(density, pressure, 1)
    soundspeed_eff = np.sqrt((5.0/3.0) * (norm / density))
    slope_eff, intercept_eff = np.polyfit(density, norm, 1)
    
    print pressuretype

    print '--------- Pressure ---------'
    print 'Mean %.4g' % np.mean(soundspeed)
    print 'Slope %.4g' % slope
    print 'Intercept %.4g' % intercept

    print '---- Effective Pressure ----'
    print 'Mean %.4g' % np.mean(soundspeed_eff)
    print 'Slope %.4g' % slope_eff
    print 'Intercept %.4g' % intercept_eff
    print '----------------------------'

    effective_pressure = pd.DataFrame(
        {'p_eff_x': p_eff_x,
         'p_eff_y': p_eff_y,
         'p_eff_z': p_eff_z,
         'norm': norm,
         'density': density,
         'pressure': pressure,
         'soundspeed': soundspeed
        }
    )

    effective_pressure.plot.scatter(x='density', y='p_eff_x', loglog=True, ylim=[10e-25,10e-14], figsize=(20, 15), fontsize=20).get_figure().savefig('p_eff_x%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='p_eff_y', loglog=True, ylim=[10e-25,10e-14], figsize=(20, 15), fontsize=20).get_figure().savefig('p_eff_y%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='p_eff_z', loglog=True, ylim=[10e-25,10e-14], figsize=(20, 15), fontsize=20).get_figure().savefig('p_eff_z%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='norm', loglog=True, ylim=[10e-25,10e-14], figsize=(20, 15), fontsize=20).get_figure().savefig('p_eff_norm%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='pressure', loglog=True, figsize=(20, 15), fontsize=20).get_figure().savefig('pressure_density%s.png' % pressuretype)
    plt.clf()
    effective_pressure['soundspeed'].hist().get_figure().savefig('soundspeed%s.png' % pressuretype)

pressuretypes = ['', '_iso50', '_iso100', '_iso200']

for pressuretype in pressuretypes:
    plot_effective_pressure(pressuretype)
    plot_effective_pressure('_smoothed'+pressuretype)