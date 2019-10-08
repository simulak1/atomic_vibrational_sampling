import numpy as np
from numpy import linalg as LA
import parse_dynmat
import boltzmann

def move_single_normal_coordinate(config1,dist,width,mM):
    '''
    Samples a random configuration by displacing the atoms in the simulation
    cell from their equilibrium positions. The displacements are along the
    eigenvectors of the vibrational normal modes. 
    '''
    
    normal_vector_to_move=np.random.randint(low=0,high=eunit.shape[0])
    
    if dist=="uniform":
        displacement = np.random.uniform(low=-width,high=width)
    elif dist=="normal":
        displacement = np.random.normal(loc=0.0,scale=width)

    config1[normal_vector_to_move]+=latvec*displacement

    delta_E = 0.5*
    
    return displacements

def accept_move(config1,config2,eunit,latvec):
    R1=latvec*(eunit.T*config1).T
    R1=latvec*(eunit.T*config1).T


def metropolis(args,T):

    # Parse the dynamical matrix file
    Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs=parse_dynmat.parseDynMat(args.filename)

    masses=[]
    for i in range(Natoms):
        masses.append[Matoms[atomNames[i]]]
    massMatrix=np.diag(masses)
    
    # Atomic positions in one matrix
    R0 = latvec*np.dot(Ra,La)
    R0=R0.flatten()


    config=sample_point(eigenvecs,R0,latvec,args.disp_distr,args.pwidth,massMatrix)


