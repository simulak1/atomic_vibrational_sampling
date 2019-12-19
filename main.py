import argparse
import numpy as np
import sampling
import file_io

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

        If 1 is chosen, you need to have a sample in.pwscf-file at the path where 
        you are executing this script.
        """,
        default=0,
        type=int
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

    if args.write_output==1:
        index=0
        for conf in configs:
            r=np.zeros((Natoms,3))
            for i in range(Natoms):
                atomind=i*3
                x=conf[atomind]/(latvec*np.sqrt(La[0,0]**2+La[0,1]**2+La[0,2]**2))
                y=conf[atomind+1]/(latvec*np.sqrt(La[1,0]**2+La[1,1]**2+La[1,2]**2))
                z=conf[atomind+2]/(latvec*np.sqrt(La[2,0]**2+La[2,1]**2+La[2,2]**2))
                r[i,0]=x+Ra[i,0]
                r[i,1]=y+Ra[i,1]
                r[i,2]=z+Ra[i,2]
            file_io.write_input("in.pwscf",args.outdir+"/in.pwscf_{}".format(index),Natoms,r)
            index+=1
            
if __name__ == '__main__':
    main()
