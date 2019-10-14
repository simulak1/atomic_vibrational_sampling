import numpy as np
import math
import scipy.special
import parse_dynmat
import matplotlib.pyplot as plt

def Pn(n,w,T):
    kb = 1.38064852*10**-23
    hbar = 6.62607004*10**-34

    return np.exp(-n*hbar*w/(kb*T))*(1-np.exp(-hbar*w/(kb*T)))

def PnInv(prob,w,T):
    kb = 1.38064852*10**-23
    hbar = 6.62607004*10**-34
    inv=1.0/(hbar*w/(kb*T))
    return -np.log(-prob+1)*inv

def hermite_polynomial(N,X):

    N1=N.shape[0]
    N2=N.shape[1]

    H=np.zeros((N1,N2))

    for n1 in range(N1):
        for n2 in range(N2):
            h=0
            n=N[n1,n2]
            x=X[n1,n2]
            if n%2==0: # parillinen
                for l in range(n/2+1):
                    h+=((-1.0)**(0.5*n-l))/(1.0*math.factorial(2*l)*math.factorial(0.5*n-l))*(2.0*x)**(2.0*l)
            else: # pariton
                for l in range((n-1)/2+1):
                    h+=((-1)**(0.5*(n-1)-l))/(1.0*math.factorial(2*l+1)*math.factorial(0.5*(n-1)-l))*(2.0*x)**(2.0*l+1.0)
            h*=1.0*math.factorial(n)
            H[n1,n2]=h
    return H
        
def eigenstate(n,x):
    '''
    n and x are [Nconfig,3*Natoms]-dimensional numpy arrays.
    '''
    
    An = (2**n*scipy.special.factorial(n)*np.sqrt(np.pi))**-0.5
    
    return An * hermite_polynomial(n,x) * np.exp(-0.5*x**2)


def print_output1(T,Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs):
    print(" ")
    print("="*30+" Sample vibrational configurations "+"="*30)
    print(" ")
    print("Temperature: {}K".format(T))
    print(" ")
    print("-"*80)
    print("Number of atoms:      {}".format(Natoms))
    print("Number of atom types: {}".format(Ntypes))
    print("Atom names:           {}".format(atomNames))
    print("Lattice constant (m): {}".format(latvec))
    print("-"*80)
    print("The simulation cell:")
    print(La)
    print("-"*80)
    print("The atomic posittions in terms of the lattice vectors:")
    print(Ra)
    print("-"*80)
    print("Atomic masses (kg):")
    print(Matoms)
    print("-"*80)
    print("Normal mode angular frequencies:")
    print(omega)
    print("-"*80)
    print("Normal mode eigenvectors:")
    print(eigenvecs)
    print("-"*80)
    print("Normal mode excitation probabilities(%):")
    string="n"+" "*12
    for i in range(Natoms*3):
        string+="w"+str(i)+" "*14
    print(string)
    for i in range(10):
        string=str(i)
        for j in range(Natoms*3):
            value="{:.2f}".format(100.0*Pn(i,omega[j],T))
            value=value.rjust(16," ")
            string+=value#str(100.0*Pn(i,omega[j],T))+" "*10
        print(string)
    
def sample_configurations(args):

    T=args.temperature
    Nconf=args.num_configs

    lim=args.sample_lim
    
    # Parse the dynamical matrix file
    Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs=parse_dynmat.parseDynMat(args.filename)

    print_output1(T,Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs)

    # The relative squared norms of the eigenvecs
    r2=np.zeros((3*Natoms,Natoms))
    for i in range(Natoms):
        r2[:,i]=np.sum(eigenvecs[:,i*3:(i+1)*3]*eigenvecs[:,i*3:(i+1)*3],axis=1)

    # Sample occupations 
    ps=np.random.rand(Nconf,3*Natoms)
    occupations=PnInv(ps,omega,T)
    occupations=occupations.astype(int)

    # Create atomic displacements
    hbar = 6.62607004*10**-34
    displacements=lim*(-latvec+2*latvec*np.random.rand(Nconf,3*Natoms)) # Eigenvec displacements
    
    # Wfn values
    single_particle_wfn_values=np.ones((Nconf,3*Natoms))
    for i in range(Natoms):
        single_particle_wfn_values*=eigenstate(occupations,displacements*(np.sqrt(r2[:,i]*Matoms[atomNames[i]]*omega/hbar)))**2

    wfn_values=[]
    for i in range(Nconf):
        phi=1
        for j in range(3*Natoms):
            phi*=single_particle_wfn_values[i,j]
        wfn_values.append(phi)

    accepted=[]
    for i in range(Nconf):
        if wfn_values[i]>np.random.rand():
            accepted.append(i)

    print("Number of trial configurations: {}".format(Nconf))
    print("Accepted:                       {}".format(len(accepted)))
        
    
    
    
    

        

    
