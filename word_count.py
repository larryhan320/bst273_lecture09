#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to the file we want to read",
)

args = parser.parse_args( )
print("args =", args)
print("args.data_file=", args.data_file) # Namespace is a type of class that uses .

fh = open(args.data_file) # Open the file called data_file using args and assign it
print("the file handle is", fh)

lines = 0
words = 0
chars = 0

for line in fh:
	print(line)


#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
