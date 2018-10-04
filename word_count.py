#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to the file we want to read",
)

args = parser.parse_args( )
print(args)
print(args.data_file) # Namespace is a type of class that uses .

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
