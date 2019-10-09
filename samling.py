import numpy as np
from numpy import linalg as LA
import parse_dynmat
import boltzmann

def metropolis(args):

    T=args.temperature
    
    # Parse the dynamical matrix file
    Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs=parse_dynmat.parseDynMat(args.filename)

    masses=[]
    for i in range(3*Natoms):
        mass=Matoms[atomNames[i/3]]
        masses.append(mass)
    massMatrix=np.diag(masses)
    
