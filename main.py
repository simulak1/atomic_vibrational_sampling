import argparse
import sampling

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

    return args_parser.parse_args()

def main():
    
    args=get_args()

    # Sample configurations
    configs=sampling.sample_configurations(args)
        
    
if __name__ == '__main__':
    main()
