import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='some help...',epilog="Distributed under the GPL")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')
    parser.add_argument('-d', '--directory', help='foo help')
    args = parser.parse_args()
    print("Current directory: " + os.getcwd())
