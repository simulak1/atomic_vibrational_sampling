import numpy as np
import math
import parse_dynmat

def n_be(T,w):
    kb = 1.38064852*10**-23
    hbar = 6.62607004*10**-34
    if T>0.0:
        exponential = (hbar*w)/(kb*T)
        return int((np.exp(exponential)-1)**-1)
    else:
        return 0

def hermite_polynomial(n,x):
    
    h=0
    if n%2==0: # parillinen
       for l in range(n/2):
           h+=((-1.0)**(0.5*n-l))/(1.0*math.factorial(2*l)*math.factorial(0.5*n-l))*(2.0*x)**(2.0*l)
       h*=1.0*math.factorial(n)
    else: # pariton
        for l in range((n-1/2)):
            h+=((-1)**(0.5*(n-1)-l))/(1.0*math.factorial(2*l+1)*math.factorial(0.5*(n-1)-l))*(2.0*x)**(2.0*l+1.0)
        h*=1.0*math.factorial(n)
    return h        
        
def eigenstate(n,x):
   
    An = (2**n*math.factorial(n)*np.sqrt(np.pi))**-0.5
    return An * hermite_polynomial(n,x) * np.exp(-0.5*x**2)

def sample_configurations(args):

    T=args.temperature
    
    # Parse the dynamical matrix file
    Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs=parse_dynmat.parseDynMat(args.filename)

    masses=[]
    for i in range(3*Natoms):
        mass=Matoms[atomNames[i/3]]
        masses.append(mass)
    massMatrix=np.diag(masses)

    occupations=[]
    # Get occupations
    for i in range(3*Natoms):
        occupations.append(n_be(T,omega[i]))

    print(occupations)
    print("*"*40)
    print(massMatrix)
    
