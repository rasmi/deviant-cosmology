#!/bin/sh
pythonenv

# Submit all analyses that require largemem processing (fluid n=1024, particle n=512,1024)

cd $WORK/simulations/fluid/box_50/n_1024/t_005/hydro_2/ic_50_1024_005_2_enzo/
sbatch run_power_spect.sh
cd $WORK/simulations/fluid/box_100/n_1024/t_005/hydro_2/ic_100_1024_005_2_enzo/
sbatch run_power_spect.sh
cd $WORK/simulations/fluid/box_200/n_1024/t_005/hydro_2/ic_200_1024_005_2_enzo/
sbatch run_power_spect.sh

cd $WORK/simulations/particle/box_50/n_512/t_005/ic_50_512_005_enzo/
sbatch run_power_spect.sh
cd $WORK/simulations/particle/box_50/n_1024/t_005/ic_50_1024_005_enzo/
sbatch run_power_spect.sh
cd $WORK/simulations/particle/box_100/n_512/t_005/ic_100_512_005_2_enzo/
sbatch run_power_spect.sh
cd $WORK/simulations/particle/box_100/n_1024/t_005/ic_100_1024_005_2_enzo/
sbatch run_power_spect.sh
cd $WORK/simulations/particle/box_200/n_512/t_005/ic_200_512_005_enzo/
sbatch run_power_spect.sh
cd $WORK/simulations/particle/box_200/n_1024/t_005/ic_200_1024_005_enzo/
sbatch run_power_spect.sh

# Run box_50 fluid
cd $WORK/simulations/fluid/box_50/n_128/t_005/hydro_2/ic_50_128_005_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b50_n128_t0.005_h2_z50.out
cd $WORK/simulations/fluid/box_50/n_256/t_005/hydro_2/ic_50_256_005_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b50_n256_t0.005_h2_z50.out
cd $WORK/simulations/fluid/box_50/n_512/t_005/hydro_2/ic_50_512_005_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b50_n512_t0.005_h2_z50.out

# Run box_100 fluid
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

# Run box_200 fluid
cd $WORK/simulations/fluid/box_200/n_128/t_005/hydro_2/ic_200_128_005_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b200_n128_t0.005_h2_z50.out
cd $WORK/simulations/fluid/box_200/n_256/t_005/hydro_2/ic_200_256_005_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b200_n256_t0.005_h2_z50.out
cd $WORK/simulations/fluid/box_200/n_512/t_005/hydro_2/ic_200_512_005_2_enzo/
power_spect.py RD0000 --type fluid --output fluid_b200_n512_t0.005_h2_z50.out

# Run box_50 particle
cd $WORK/simulations/particle/box_50/n_128/t_005/ic_50_128_005_enzo/
power_spect.py RD0000 --type particle --output particle_b50_n128_t0.005_h2_z50.out
cd $WORK/simulations/particle/box_50/n_256/t_005/ic_50_256_005_enzo/
power_spect.py RD0000 --type particle --output particle_b50_n256_t0.005_h2_z50.out

# Run box_100 particle
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

# Run box_200 particle
cd $WORK/simulations/particle/box_200/n_128/t_005/ic_200_128_005_enzo/
power_spect.py RD0000 --type particle --output particle_b200_n128_t0.005_h2_z50.out
cd $WORK/simulations/particle/box_200/n_256/t_005/ic_200_256_005_enzo/
power_spect.py RD0000 --type particle --output particle_b200_n256_t0.005_h2_z50.out

# CourantSafety fluid
cd $SCRATCH/safetyConstant/fluid/box_100/n_128/t_005/hydro_2/safety_01/ic_100_128_005_2_01_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n128_t0.005_cs0.1.out
cd $SCRATCH/safetyConstant/fluid/box_100/n_256/t_005/hydro_2/safety_01/ic_100_256_005_2_01_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.005_cs0.1.out

# CourantSafety particle
cd $SCRATCH/safetyConstant/particle/box_100/n_128/t_005/safety_01/ic_100_128_005_2_01_enzo/
power_spect.py RD0000 --type particle --output particle_b100_n128_t0.005_cs0.1.out
cd $SCRATCH/safetyConstant/particle/box_100/n_256/t_005/safety_01/ic_100_256_005_2_01_enzo/
power_spect.py RD0000 --type particle --output particle_b100_n256_t0.005_cs0.1.out

# Isothermal
cd $SCRATCH/isothermal_tests/box_100/n_256/t_005/hydro_2/cs_3/ic_100_256_005_2_3_isothermal_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.005_h2_isothermal3.out
cd $SCRATCH/isothermal_tests/box_100/n_256/t_005/hydro_2/cs_10/ic_100_256_005_2_10_isothermal_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.005_h2_isothermal10.out
cd $SCRATCH/isothermal_tests/box_100/n_256/t_005/hydro_2/cs_30/ic_100_256_005_2_30_isothermal_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.005_h2_isothermal30.out
cd $SCRATCH/isothermal_tests/box_100/n_256/t_005/hydro_2/cs_100/ic_100_256_005_2_100_isothermal_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n256_t0.005_h2_isothermal100.out

cd $SCRATCH/isothermal_tests/box_100/n_512/t_005/hydro_2/cs_3/ic_100_512_005_2_3_isothermal_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n512_t0.005_h2_isothermal3.out
cd $SCRATCH/isothermal_tests/box_100/n_512/t_005/hydro_2/cs_10/ic_100_512_005_2_10_isothermal_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n512_t0.005_h2_isothermal10.out
cd $SCRATCH/isothermal_tests/box_100/n_512/t_005/hydro_2/cs_30/ic_100_512_005_2_30_isothermal_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n512_t0.005_h2_isothermal30.out
cd $SCRATCH/isothermal_tests/box_100/n_512/t_005/hydro_2/cs_100/ic_100_512_005_2_100_isothermal_enzo/
power_spect.py RD0000 --type fluid --output fluid_b100_n512_t0.005_h2_isothermal100.out