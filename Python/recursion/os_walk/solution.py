#!/usr/bin/env python

import os
import sys

def print_all_files(path):
    if os.path.isfile(path):
        print "file: {}".format(path)
    else:
        for f in os.listdir(path):
            print_all_files(os.path.join(path,f))

# Test function
if __name__ == '__main__':

    try:
        print_all_files(sys.argv[1])

    except IndexError:
        print "Please pass directory path!"
