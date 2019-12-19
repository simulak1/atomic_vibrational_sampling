import numpy as np
import math
import sys
import scipy.special
import file_io
import matplotlib.pyplot as plt

def Pn(n,w,T):
    kb = 1.38064852*10**-23
    hbar = 6.62607004*10**-34

    return np.exp(-n*hbar*w/(kb*T))*(1-np.exp(-hbar*w/(kb*T)))

def PnInv(prob,w,T):
    kb = 1.38064852*10**-23
    hbar = 6.62607004*10**-34
    inv = kb*T/(hbar*w)
    return -np.log(-prob+1)*inv

def hermite_polynomial(n,x):

    h=0
    if n%2==0: # parillinen
        for l in range(n/2+1):
            h+=((-1.0)**(0.5*n-l))/(1.0*math.factorial(2*l)*math.factorial(0.5*n-l))*(2.0*x)**(2.0*l)
    else: # pariton
        for l in range((n-1)/2+1):
            h+=((-1)**(0.5*(n-1)-l))/(1.0*math.factorial(2*l+1)*math.factorial(0.5*(n-1)-l))*(2.0*x)**(2.0*l+1.0)
    h*=1.0*math.factorial(n)
    return h
        
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

def sample_q(lim,n):

    sum=0
    accepted=False
    while(not(accepted)):
        q=lim*(-1+2*np.random.rand())
        wfn=eigenstate(n,q)
        sum+=1
        if wfn**2>np.random.rand():
            accepted=True
            return q    
        
def sample_configurations(args):

    T=args.temperature
    Nconf=args.num_configs

    lim=args.sample_lim

    hbar = 6.62607004*10**-34
    
    # Parse the dynamical matrix file
    Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs=file_io.parseDynMat(args.filename,args.nfiles)

    masses=np.zeros((3*Natoms,))
    for i in range(3*Natoms):
        masses[i]=Matoms[atomNames[i/3]]
    
    print_output1(T,Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs)

    configs=[]

    for i in range(Nconf):
        r=np.zeros((3*Natoms,))
        for j in range(3,eigenvecs.shape[0]):
            
            # Sample occupation 
            n=int(PnInv(np.random.rand(),omega[j],T))

            # Sample displacements
            q=sample_q(lim,n)
            
            # Multiply eigenvec, add to total displacement
            r+=q*eigenvecs[j]/np.sqrt(masses*omega[j]/hbar)
        configs.append(r)

    return configs,Natoms,latvec,La,Ra
            
            
            
            
    
    
    
    

        

    
