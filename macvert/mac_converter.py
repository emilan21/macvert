#!/usr/bin/python

# mac_convertor.py - Converts mac address from various formats to other formats

import os
import sys

sys.path += [os.path.abspath('..')]
from macvert.web import app

def main():
	app.run(debug=True)	

if __name__ == '__main__':
    	main()
