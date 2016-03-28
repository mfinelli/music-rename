import os
import argparse
import music_rename

def main():
    parser = argparse.ArgumentParser(description='some help...',epilog="Distributed under the GPL")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + music_rename.__version__)
    parser.add_argument('-d', '--directory', help='foo help')
    args = parser.parse_args()
    print("Current directory: " + os.getcwd())
