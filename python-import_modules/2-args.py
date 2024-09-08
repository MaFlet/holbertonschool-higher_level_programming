#!/usr/bin/python3
"""
This script prints the number of the list of
its arguments
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
import sys

if __name__ == "__main__":
    argv = sys.argv[1:] #Excludes the first element, script name itself
    num_args = len(argv) #number of arguments is determine by len

    if num_args == 0:
        print("0 arguments.") #If there are no arguments
    elif num_args == 1:
        print("1 argument:") #print excatly one argument
        print("1: {}". format(argv[0]))
    else:
        print("{} arguments:".format(num_args))
        for i in range(num_args):
            print("{}: {}".format(i + 1, argv[i]))
