import argparse


def main():
    parser = argparse.ArgumentParser(description='Collect input arguments')
    parser.add_argument('--who', required=False, default="John Doe", help='Who should we greet?')
    args = parser.parse_args()

    # Do some Github feedback stuff
    print("::notice file=entrypoint.sh,line=11::Checkpoint reached")

    # The output of our action
    result = "Helo there %s" % args.who
    print(f'::set-output name=greeting::{result}')


if __name__ == "__main__":
    main()
