import argparse
import parse_dynmat
import monte_carlo

def get_args():

    args_parser = argparse.ArgumentParser()

    args_parser.add_argument(
        '--filename',
        help="The dynamical matrix file. ",
        required=True
    )

    args_parser.add_argument(
        '--temperature',
        help="Do I need to explain?.",
        default=0.1,
        type=float
    )

    args_parser.add_argument(
        '--equil-step',
        help="The number of equilibration steps.",
        default=100,
        type=int
    )

    args_parser.add_argument(
	'--nstep',
        help="The number of statistics accumulation steps.",
        default=1000,
        type=int
    )

    args_parser.add_argument(
	'--decorr-period',
        help="The number of Metropolis steps to run between saving configs..",
        default=25,
        type=int
    )
    
    args_parser.add_argument(
        '--disp-distr',
        help="""
        The probabilistic distribution out of which 
        the displacements of atoms are proposed to the
        Metropolis.
        Options are: 
        1) uniform
        2) normal
        default is uniform.
        """,
        default="uniform"
    )

    args_parser.add_argument(
        '--pwidth',
        help="""
        A parameter to tune the probabilistic distribution
        chosen for Metropolis. 
        - In the case of uniform distribution,
          the displacements will be chosen from an interval
          latvec*[-pwidth,pwidth]. 
        - In the case of the normal distribution, pwidth is
          the width of the gaussian centered at zero. When
          numbers are sampled out of the gaussian, the disp-
          lacements will be the number*latvec.          
        """,
        default=0.1,
        type=float
    )
    
    return args_parser.parse_args()

def main():
    
    args=get_args()
    T=args.temperature

    # Sample configurations
    configs=monte_carlo.metropolis(args,T)
        
    
if __name__ == '__main__':
    main()
