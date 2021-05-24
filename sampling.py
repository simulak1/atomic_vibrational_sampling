import numpy as np
import math
import sys
import scipy.special
import file_io
import matplotlib.pyplot as plt

def pn(n,alpha):
    return np.exp(-alpha*n)*(1-np.exp(-alpha))

def PN(N,alpha):
    return 1-np.exp(-alpha*(N+1))

def PNinv(prob,alpha,levels):

    if(abs(1-prob)<0.0000000000001):
        ind=0
        while(abs(levels[ind]-1)>0.00000000000001):
            ind+=1
        return ind
            
    a1=alpha
    a2=np.log(1-prob)

    return -1*(a1+a2)/alpha

def map2level(p,pn):
    i=0
    while(p>pn[i]):
        i+=1
    return pn[i]

def hermite_polynomial(n,x):

    h=0
    if n%2==0: # parillinen
        for l in range(int(n/2)+1):
            h+=((-1.0)**(0.5*n-l))/(1.0*math.factorial(2*l)*math.factorial(0.5*n-l))*(2.0*x)**(2.0*l)
    else: # pariton
        for l in range(int((n-1)/2)+1):
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

    kb = 1.38064852*10**-23
    hbar = 6.62607004*10**-34

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
    string="n"+" "*10
    for i in range(8):
        string+=str(i)+" "*10
    print(string)
    for i in range(3,eigenvecs.shape[0]):
        string="f"+str(i)
        for j in range(8):
            alpha=hbar*omega[i]/(kb*T)
            value="{:.2f}".format(100.0*pn(j,alpha))
            value=value.rjust(11," ")
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
    kb = 1.38064852*10**-23
    
    # Parse the dynamical matrix file
    Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs=file_io.parseDynMat(args.filename,args.nfiles)

    masses=np.zeros((3*Natoms,))

    ind=0
    for i in range(Natoms):
        for j in range(3):
            masses[ind]=Matoms[atomNames[i]]
            ind+=1
    
    print_output1(T,Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs)
    
    configs=[]

    for i in range(Nconf):
        r=np.zeros((3*Natoms,))
        for j in range(3,eigenvecs.shape[0]):

            alpha=hbar*omega[j]/(kb*T)
            # Sample occupation
            cumulative_values=PN(np.arange(0,100),alpha)
            randi=np.random.rand()
            cumulative_sample_value=map2level(randi,cumulative_values)
            if(T<0.000000001):
                n=0
            else:
                n=np.rint(PNinv(cumulative_sample_value,alpha,cumulative_values))

            # Sample displacements in units of sqrt(hbar/(m*omega))
            q=sample_q(lim,n)
            
            # Multiply eigenvec, add to total displacement
            r+=q*eigenvecs[j]/np.sqrt(masses*omega[j]/hbar)
            
        configs.append(r)

    return configs,Natoms,latvec,La,Ra
            
            
            
            
    
    
    
    

        

    
