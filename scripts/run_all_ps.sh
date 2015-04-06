#!/bin/sh
pythonenv

cd $WORK/simulations/fluid/box_100/n_128/t_005/hydro_2/ic_100_128_005_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n128_t0.005_h2_z50.out
cd $WORK/simulations/fluid/box_100/n_256/t_0015/hydro_0/ic_100_256_0015_0_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.0015_h0_z50.out
cd $WORK/simulations/fluid/box_100/n_256/t_0015/hydro_2/ic_100_256_0015_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.0015_h2_z50.out
cd $WORK/simulations/fluid/box_100/n_256/t_005/hydro_0/ic_100_256_005_0_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.005_h0_z50.out
cd $WORK/simulations/fluid/box_100/n_256/t_005/hydro_2/z_25/ic_100_256_005_2_25_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.005_h2_z25.out
cd $WORK/simulations/fluid/box_100/n_256/t_005/hydro_2/z_50/ic_100_256_005_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.005_h2_z50.out
cd $WORK/simulations/fluid/box_100/n_256/t_005/hydro_2/z_100/ic_100_256_005_2_100_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.005_h2_z100.out
cd $WORK/simulations/fluid/box_100/n_256/t_015/hydro_0/ic_100_256_015_0_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.015_h0_z50.out
cd $WORK/simulations/fluid/box_100/n_256/t_015/hydro_2/ic_100_256_015_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.015_h2_z50.out
cd $WORK/simulations/fluid/box_100/n_512/t_005/hydro_2/ic_100_512_005_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n512_t0.005_h2_z50.out
cd $WORK/simulations/particle/box_100/n_128/t_005/ic_100_128_005_2_enzo/
power_spect.py RD0000 --type particle --output particle_b100_n128_t0.005_h2_z50.out
cd $WORK/simulations/particle/box_100/n_256/t_0015/ic_100_256_0015_2_enzo/
power_spect.py RD0000 --type particle --output particle_b100_n256_t0.0015_h2_z50.out
cd $WORK/simulations/particle/box_100/n_256/t_005/z_25/ic_100_256_005_2_25_enzo/
power_spect.py RD0000 --type particle --output particle_b100_n256_t0.005_h2_z25.out
cd $WORK/simulations/particle/box_100/n_256/t_005/z_50/ic_100_256_005_2_enzo/
power_spect.py RD0000 --type particle --output particle_b100_n256_t0.005_h2_z50.out
cd $WORK/simulations/particle/box_100/n_256/t_005/z_100/ic_100_256_005_2_100_enzo/
power_spect.py RD0000 --type particle --output particle_b100_n256_t0.005_h2_z100.out
cd $WORK/simulations/particle/box_100/n_256/t_015/ic_100_256_015_2_enzo/
power_spect.py RD0000 --type particle --output particle_b100_n256_t0.015_h2_z50.out
cd $WORK/simulations/particle/box_100/n_512/t_005/ic_100_512_005_2_enzo/
sbatch run_power_spect.sh