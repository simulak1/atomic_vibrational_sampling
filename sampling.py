import numpy as np
import math
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
   
    An = (2**n*math.factorial(n)*np.sqrt(np.pi))**-0.5
    
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
    N_occ=args.num_occupation_configs
    Nconf=args.num_displ
    
    # Parse the dynamical matrix file
    Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs=parse_dynmat.parseDynMat(args.filename)

    print_output1(T,Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs)

    masses=[]
    for i in range(3*Natoms):
        mass=Matoms[atomNames[i/3]]
        masses.append(mass)
   

    ps=np.random.rand(N_occ,3*Natoms)
    occupations=PnInv(ps,omega,T)
    #hist=np.histogram(occupations[:,0],bins=np.arange(40),normed=True)
    #print(hist)

    occupations=occupations.astype(int)
    print(occupations)
    mode1=eigenstate()
    
    #xx=np.arange(-1,1,0.05)*np.sqrt(masses[0]*omega[0]/hbar)*latvec
    #phi=eigenstate(int(occupations[0]),xx)**2
    #plt.plot(xx,phi,'r*-')
    #plt.show()
    #plt.plot(hist[0],'ro')
    #plt.grid(True)
    #plt.show()

        

    
