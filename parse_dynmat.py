import numpy as np

def parseDynMat(filename):

    def _readConstants(line):
        words=line.split()
        Ntypes=int(words[0])
        Natoms=int(words[1])
        # Lattice vector is in Bohrs. Convert to meters.
        latvec=52.9177249*10.0**-12*float(words[3])
        return Ntypes,Natoms,latvec
    
    def _readBasis(lines,Natoms,Ntypes):
        A=np.zeros((3,3))
        for i in [0,1,2]:
            words=lines[i].split()
            A[i,0]=float(words[0])
            A[i,1]=float(words[1])
            A[i,2]=float(words[2])
        # Note: the masses are converted from atomic units
        #       by dividing them by 2*m_e (twice the electron mass).
        atom_masses={}
        atomnames=[]
        for i in range(3,3+Ntypes):
            words=lines[i].split()
            atomnames.append(str(words[1]))
            atom_masses[str(words[1])]=float(words[3])
        atompos=np.zeros((Natoms,3))
        atomtypes={}
        for i in range(3+Ntypes,3+Ntypes+Natoms):
            words=lines[i].split()
            counter=i-3-Ntypes
            atompos[counter,0]=float(words[2])
            atompos[counter,1]=float(words[3])
            atompos[counter,2]=float(words[4])
            atomtypes[counter]=atomnames[int(words[1])-1]

        # Change atomic masses to kg:
        # new units=pwscf_units/amu2me*2*amu2kg
        for i in range(Ntypes):
            atom_masses[atomnames[i]]=atom_masses[atomnames[i]]/1822.888486209*2*1.66053906660*10**-27
            
        return A,atompos,atom_masses,atomtypes

    def _readNormalModes(lines,Natoms):
        freqs=[]
        eigenvec=np.zeros((3*Natoms,3*Natoms))
        counter=0
        for i in range(len(lines)):
            words=lines[i].split()
            if words[0]=="freq":
                freqs.append(float(words[4]))
                for j in range(Natoms):
                    words2=lines[i+1+j].split()

                    eigenvec[counter,3*j+0]=float(words2[1])
                    eigenvec[counter,3*j+1]=float(words2[3])
                    eigenvec[counter,3*j+2]=float(words2[5])
                counter=counter+1
                    
        # Change frequencies from THz to angular freqs.
        freqs=np.array(freqs,dtype=float)*10.0**12*2*np.pi

        return freqs,eigenvec

    # Parse the dynamical matrix file with the predefined functions
    with open(filename) as f:
        lines=f.readlines()
        N=len(lines)
        for i in range(N):
            line=lines[i]
            words=line.split()
            if len(words)>0 and words[0]=="phonons":
                Ntypes,Natoms,latvec=_readConstants(lines[i+1])
            if len(words)>0 and words[0]=="Basis":
                La,Ra,Matoms,atomNames = _readBasis(lines[i+1:i+4+Natoms+1],Natoms,Ntypes)
            if len(words)>0 and words[0][:30]=="*"*30:
                omega,eigenvecs=_readNormalModes(lines[i+1:],Natoms)
                break

    return Ntypes,Natoms,latvec,La,Ra,Matoms,atomNames,omega,eigenvecs
            

