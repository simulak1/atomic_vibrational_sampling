# atomic_vibrational_sampling

A program to read in normal modes of vibrations in an atomic structure, solved by Quantum Espresso's (https://www.quantum-espresso.org/) PHONON-package, and to produce atomic configurations distributed according to the vibrational states in given temperature.

## Quick start to analyse example data

### Create local environment

1. Clone the repository
2. Go to repository
3. `pip install virtualenv`
4. `python -m venv virtualenv; source virtualenv/bin/activate'`
5. `pip install -r requirements.txt`

### Create 10 PWSCF input files for silicon 8-atom cubic cell based on inputs and outputs of PWSCF and PHONON in 'examples/silicon_8_atoms/'

6) `python src/main.py --outdir . --filename examples/silicon_8atoms/dyn --nfiles 1 --temperature 0 --sample-lim 1 --num-configs 10 --write-output 1 --qe-input examples/silicon_8atoms/in.pwscf`

## About this program

### Overview

Atoms are in constant motion, even at zero temperature. This program in essence takes images of atomic positions of given systems, and saves the images into PWSCF input files. Thus the images will be statistically distributed according to the atomic motion, and with infinite amount of image the atomic trajectories would be perfectly known. The PWSCF inputs can be used to run parallel simulations, and gather statstics on, e.g. energy differences between static equilibrium structures and the dynamic vibrating systems. While some vibrational properties of simulated systems can be analysed with the normal modes solved by PHONON-package (or any vibrational analysis tool), some features of the systems cannot be analysed with existing methods.

### Working principles

This program starts from the normal modes of a given atomic system, solved by density functional perturbation theory as implemented in Quantum Espresso's PWSCF and PHONON packages. The PHONON package uses the self-consistent charge density and Kohn-Sham orbitals as given by PWSCF. More information can be found [here](http://www.fisica.uniud.it/~giannozz/Didattica/MetNum/2010/phonons.html)

After executing PHONON's binary, a file containing the eigenfrequencies and corresponding eigenvectors of the normal modes is created and will be used as input for this program. The program 

- Reads in the simulation cell info and the normal modes.
- Samples the atomic configurations by repeatedly 
  - 2.1. Occupying the vibrational states by sampling the Boltzmann distribution
  - 2.2. Sampling displacements from the occupied states (states of 3N-dimensional quantum harmonic oscillators, if N is atom number) by using the Neumann's algorithm.
  - 2.3 Adding the displacements of individual occupied states together 
- Saves the atomic configurations to PWSCF input files for further calculations. 

### Practical example

The effect of lattice vibrations on positron lifetime within solids has been a theoretical question hanging on the positron researchers due to date. Positron lifetime is solved computationally usually by a two-component DFT calculation, where one can run e.g. PWSCF-computation to solve the charge density, and use a positron package Atsup to solve the positron density at the potential of the eletron density, and use the aqcuired densitites to calculate the lifetime. To estimate the effect of atomic vibrations on the lifetimes, one cannot use some existing theory to directly solve the effect based on the normal modes obtained from e.g. PHONON. Instead, a stochastic approach, such as the one presented here, can be used, and run N two-component DFT simulations for atomic structures produced for the system by this program. With obtained t_i lifetimes, the lifetime estimate with vibrational effects included can be estimated as 

t=1/N sum_i t_i,

and the error on the estimate is the standard deviation of t_i.
