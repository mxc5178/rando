#!/usr/bin/env python

##
## Rando/Util/Args.py
##

###############################################################################
###############################################################################
## DEPENDENCIES:
###############################################################################
###############################################################################
##
## argparse (Python 2.7.3)
##
###############################################################################
###############################################################################
##
## TODO:
##
###############################################################################
###############################################################################
## USAGE
###############################################################################
###############################################################################
##
## import RANDO.Util.Args as Args
##
###############################################################################
###############################################################################

import argparse

###############################################################################
###############################################################################
##
## RANDO.Util.Args class
##
###############################################################################
###############################################################################

class Args(object):

    ##
    ## Argument parser
    ##
    parser = argparse.ArgumentParser(description='NIST Randomness Test Suite')

    parser.add_argument(
        '--infile', '-i',
        metavar='[INFILE]',
        dest='infile',
        nargs=1,
        default=None,
        help='File of binary bits'
    )

    parser.add_argument(
        '--outfile', '-o',
        metavar='[OUTFILE]',
        dest='outfile',
        nargs=1,
        default=None,
        help='Output file'
    )

    parser.add_argument(
        '--sites', '-s',
        metavar='[SITES]',
        dest='sites',
        nargs=1,
        default=None,
        help='List of sites to scrape'
    )

    parser.add_argument(
        '--test', '-t',
        dest='test',
        action='store_true',
        default=None,
        help='Generate non-random test data'
    )

    parser.add_argument(
        '--netrand', '-n',
        dest='netrand',
        action='store_true',
        default=None,
        help='Perform network based ranom number generation'
    )

    parser.add_argument(
        '--devrand', '-g',
        dest='devrand',
        action='store_true',
        default=None,
        help='Ranom number generation using /dev/urandom'
    )

    parser.add_argument(
        '--archive', '-a',
        dest='archive',
        action='store_true',
        default=None,
        help='Archive current files in <outdir> if older than one day'
    )

    parser.add_argument(
        '--verbose', '-v',
        dest='verbose',
        action='store_true',
        default=None,
        help='Generate verbose output'
    )

    parser.add_argument(
        '--outdir', '-d',
        metavar='[OUTDIR]',
        dest='outdir',
        nargs=1,
        default=None,
        help='Directory where output files are placed'
    )

    parser.add_argument(
        '--len', '-l',
        metavar='[LENGTH]',
        dest='len',
        nargs=1,
        default=None,
        help='Length of random number to be generated'
    )

    def parse(self):
        args = self.parser.parse_args()
        return args
