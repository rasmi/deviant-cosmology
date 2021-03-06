import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
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
    soundspeed = np.sqrt((pressure / density))
    soundspeed_eff = np.sqrt((norm / density))
    slope, intercept = np.polyfit(density, pressure, 1)
    #slope_eff, intercept_eff = np.polyfit(density, norm, 1)
    slope = np.sqrt(slope)
    #slope_eff = np.sqrt(slope_eff)
    
    print pressuretype

    print '--------- Pressure ---------'
    print 'Mean %.4g' % (np.mean(soundspeed)*1e-5)
    print 'Slope %.4g' % (1e-5*slope)
    #print 'Intercept %.4g' % (1e-5*intercept)

    """
    print '---- Effective Pressure ----'
    print 'Mean %.4g' % (1e-6*np.mean(soundspeed_eff))
    print 'Slope %.4g' % (1e-6*slope_eff)
    #print 'Intercept %.4g' % (1e-6*intercept_eff)
    """
    print '----------------------------'
    
    effective_pressure = pd.DataFrame(
        {'p_eff_x': p_eff_x,
         'p_eff_y': p_eff_y,
         'p_eff_z': p_eff_z,
         'norm': norm,
         'density': density,
         'pressure': pressure,
         'soundspeed': soundspeed/1e5,
         'soundspeed_eff': soundspeed_eff/1e5
        }
    )

    ylim = [10e-25,10e-14]
    figsize = (20, 15)
    fontsize = 20

    effective_pressure.plot.scatter(x='density', y='p_eff_x', loglog=True, ylim=ylim, figsize=figsize, fontsize=fontsize).get_figure().savefig('p_eff_x%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='p_eff_y', loglog=True, ylim=ylim, figsize=figsize, fontsize=fontsize).get_figure().savefig('p_eff_y%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='p_eff_z', loglog=True, ylim=ylim, figsize=figsize, fontsize=fontsize).get_figure().savefig('p_eff_z%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='norm', loglog=True, ylim=ylim, figsize=figsize, fontsize=fontsize).get_figure().savefig('p_eff_norm%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='pressure', loglog=True, figsize=figsize, fontsize=fontsize).get_figure().savefig('pressure_density%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='soundspeed', logx=True, ylim=[-10, 500], xlim=[1e-31, 1e-27], figsize=figsize, fontsize=fontsize).get_figure().savefig('soundspeed_density%s.png' % pressuretype)
    effective_pressure.plot.scatter(x='density', y='soundspeed_eff', logx=True, ylim=[-10, 500], xlim=[1e-31, 1e-27], figsize=figsize, fontsize=fontsize).get_figure().savefig('soundspeed_eff_density%s.png' % pressuretype)
    plt.clf()
    effective_pressure['soundspeed'].hist().get_figure().savefig('soundspeed%s.png' % pressuretype)
    
    plt.clf()
    plt.hist2d(np.log10(effective_pressure['density']), effective_pressure['soundspeed'], bins=100, norm=LogNorm())
    plt.colorbar()
    plt.savefig('soundspeed_density_hist%s.png' % pressuretype)
    plt.clf()

pressuretypes = ['', '_iso50', '_iso100', '_iso200']

for pressuretype in pressuretypes:
    plot_effective_pressure(pressuretype)
    plot_effective_pressure('_smoothed'+pressuretype)