import argparse
import numpy as np
import sampling
import file_io
import sys

def get_args():

    args_parser = argparse.ArgumentParser()

    args_parser.add_argument(
        '--filename',
        help="The dynamical matrix file. ",
        required=True
    )

    args_parser.add_argument(
        '--nfiles',
        help=
        """
        The number of files containing the normal modes, i.e.
        the number of k-vectors in the normal mode calculation.
        """,
        default=1,
        type=int
    )
    
    args_parser.add_argument(
        '--temperature',
        help="Do I need to explain?.",
        default=0.1,
        type=float
    )

    args_parser.add_argument(
        '--sample-lim',
        help="""
        Spatial limits for the atomic position sampling. 
        Sampling points between sample-lim*[-latvec,latvec].
        """,
        default=10.0,
        type=float
    )    
    
    args_parser.add_argument(
        '--num-configs',
        help=
        """
        The number of different occupational configs to sample.
        """,
        default=10,
        type=int
    )

    args_parser.add_argument(
        '--write-output',
        help=
        """
        1: Write QE input files from sampled configurations.
        0: Don't.

        """,
        default=0,
        type=int
    )

    args_parser.add_argument(
        '--qe-input',
        help=
        """
        File of the QE pwscf input that will be rewritten for each 
        sampled configuration.
        """,
        default="in.pwscf",
        type=str
    )
    
    args_parser.add_argument(
        '--outdir',
        help="The directory to write the input files. ",
        required=True
    )
    
    return args_parser.parse_args()

def main():
    
    args=get_args()

    # Sample configurations
    configs,Natoms,latvec,La,Ra=sampling.sample_configurations(args)

    R=latvec*np.matmul(Ra,La)
    LaT=latvec*La.T
    print("Atomic positions in cartesian coordinates:")
    print(R)
    print("")
    if args.write_output==1:
        index=0
        for conf in configs:
            r=np.zeros((Natoms,3))
            for i in range(Natoms):
                r[i,:]=R[i,:]+conf[3*i:3*i+3]

            ATAinv=np.linalg.inv(np.matmul(LaT.T,LaT))
            MPinv=np.matmul(ATAinv,LaT.T)
            r=np.dot(MPinv,r.T).T

            
            file_io.write_input(args.qe_input,args.outdir+"/"+args.qe_input.split("/")[-1]+"_{}".format(index),Natoms,r)
            index+=1
            
if __name__ == '__main__':
    main()
