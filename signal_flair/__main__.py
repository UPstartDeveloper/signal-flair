import os, sys


def main():
    '''Prevent errors due to different file systems.'''
    path = os.path.dirname(os.path.abspath(__file__))
    os.system("gunicorn app:app --chdir " + path)


if __name__ == "__main__":
    sys.exit(main())
