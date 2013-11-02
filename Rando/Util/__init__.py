#!/usr/bin/env python

##
## Rando/Util/__init__.py
##

###############################################################################
###############################################################################
## DEPENDENCIES:
###############################################################################
###############################################################################
##
## numpy
## scipy
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
## import Rando.Util as Util
##
###############################################################################
###############################################################################

import os
import numpy as np
import scipy.special as spc
import sys


###############################################################################
###############################################################################
##
## Rando.Util
##
###############################################################################
###############################################################################

def writedata(pathlist, pvals, r, md5):

    path = reduce(os.path.join, pathlist)
    with open(path, 'w') as f:
        f.write(r)
        f.write(':')
        #i = 0
        for pval in pvals:
            f.write(str(pvals[pval]))
            #if i < 14:
            f.write(':')

            #i += 1

        f.write(md5)
        f.write('\n')

    return

def verb(verbose, s, err):
    if verbose:
        if err:
            sys.stderr.write(s)
        else:
            sys.stdout.write(s)

def randgen(len):
    ##
    ## Spit out a stream of random numbers like 
    ## '1001001' with the length num
    ##

    rn = open('/dev/urandom', 'r')
    random_chars = rn.read(int(len) / 2)
    stream = ''
    for char in random_chars:
        c = ord(char)
        for i in range(0, 2):
            stream += str(c >> i & 1)
    return stream

def nonrand(verbose, len, n):
    ##
    ## spit out a stream of non-random test cases
    ##
    stream = ''
    if n == 1:
        verb(verbose, '[+]\n[+] running test 1 0000000011111111\n[+]\n', False)
        for i in range(len/16):
            stream += '0000000011111111'

    elif n == 2:
        verb(verbose, '[+]\n[+] running test 2 01010101\n[+]\n', False)
        for i in range(len/8):
            stream += '01010101'
    elif n == 3:
        verb(verbose, '[+]\n[+] running test 3 0000000100100011010001010110011110001001101010111100110111101111\n[+]\n', False)
        for i in range(len/64):
            stream += '0000000100100011010001010110011110001001101010111100110111101111'

    return stream

def hex2bin(hexin):
    ##
    ## loop through hex characters and do simple switch
    ##
    pairs = {}
    pairs['0'] = '0000'
    pairs['1'] = '0001'
    pairs['2'] = '0010'
    pairs['3'] = '0011'
    pairs['4'] = '0100'
    pairs['5'] = '0101'
    pairs['6'] = '0110'
    pairs['7'] = '0111'
    pairs['8'] = '1000'
    pairs['9'] = '1001'
    pairs['a'] = '1010'
    pairs['b'] = '1011'
    pairs['c'] = '1100'
    pairs['d'] = '1101'
    pairs['e'] = '1110'
    pairs['f'] = '1111'

    stream = ''
    chars = list(hexin)
    for c in chars:
        stream += pairs[c]

    return stream


def xor(a, b):
    ##
    ## shorter input in list1 ... residue of list2 to /dev/null
    ##
    if len(a) > len(b):
        list1 = list(b)
        list2 = list(a)
    else:
        list1 = list(a)
        list2 = list(b)

    stream = ''
    i = 0
    for l in list1:
        if l == list2[i]:
            stream += '0'
        else:
            stream += '1'

        i+=1

    return stream

