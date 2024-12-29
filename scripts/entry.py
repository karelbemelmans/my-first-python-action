import argparse
import os


def greet(who=None):
    return f"Hello, {who}!"


def main():
    parser = argparse.ArgumentParser(description='Collect input arguments')
    parser.add_argument('--who', required=False, default="John Doe", help='Who should we greet?')
    args = parser.parse_args()

    # Do some Github feedback stuff
    print("::notice file=entrypoint.sh,line=11::Checkpoint reached")

    # Do the actual call
    greeting = greet(args.who)

    # Set the output variable for Github Actions
    with open(os.environ.get('GITHUB_OUTPUT'), 'a') as fh:
        fh.write(f'greeting={greeting}\n')


if __name__ == "__main__":
    main()
