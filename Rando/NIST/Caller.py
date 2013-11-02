#!/usr/bin/env python

##
## Rando/NIST/Caller.py
##

###############################################################################
###############################################################################
## DEPENDENCIES:
###############################################################################
###############################################################################
##
## Rando.NIST.Tests.py
##
###############################################################################
###############################################################################
## USAGE
###############################################################################
###############################################################################
##
## import Rando.NIST.Runner as Runner
##
###############################################################################
###############################################################################

import sys
import Rando.Util as Util
import Rando.NIST.Tests as Tests


def callapproximateentropytest(len, binin, verbose):

    Util.verb(verbose, '[+]\n[+] PERFORMING APPROXIMATE ENTROPY TEST\n[+]\n', False)

    pval = Tests.approximateentropytest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval


def callbinarymatrixranktest(len, binin, verbose):
    if len < 1024:
        Util.verb(verbose, '[-]\n[-] input too short for Binary Matrix Rank Test\n[-]\n', True)
        pval = ''

    else:
        Util.verb(verbose, '[+]\n[+] PERFORMING BINARY MATRIX RANK TEST\n[+]\n', False)

        pval = Tests.binarymatrixranktest(binin)

        Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval


def callblockfrequencytest(len, binin, verbose): 
    Util.verb(verbose, '[+]\n[+] PERFORMING BLOCK FREQUENCY TEST\n[+]\n', False)

    pval = Tests.blockfrequencytest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval

def callcumulativesumstest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING CUMULATIVE SUMS TEST\n[+]\n', False)

    pval1 = Tests.cumulativesumstest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval1, False)
    Util.verb(verbose, '[+]\n[+] PERFORMING REVERSE CUMULATIVE TEST\n[+]\n', False)

    pval2 = Tests.cumulativesumstestreverse(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval2, False)

    return [pval1, pval2]


def calllinearcomplexitytest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING LINEAR COMPLEXITY TEST\n[+]\n', False)

    pval = Tests.linearcomplexitytest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval


def calllongestrunonestest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING LONGEST RUN OF ONES TEST\n[+]\n', False)

    pval = Tests.longestrunonestest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)
    
    return pval


def callmaurersuniversalstatistictest(len, binin, verbose):
    if len < 16384:
        Util.verb(verbose, '[-]\n[-] input too short for Maurer\'s Universal Statistic Test\n[-]\n', True)
        pval = ''
    else:
        Util.verb(verbose, '[+]\n[+] PERFORMING MAURER\'S UNIVERSAL STATISTIC TEST\n[+]\n', False)

        pval = Tests.maurersuniversalstatistictest(binin)

        Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval

def callmonobitfrequencytest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING MONOBIT FREQUENCY TEST\n[+]\n', False)

    pval = Tests.monobitfrequencytest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval


def callnonoverlappingtemplatematchingtest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING NONOVERLAPPING TEMPLATE MATCHING TEST\n[+]\n', False)

    pval = Tests.nonoverlappingtemplatematchingtest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval
   

def calloverlappingtemplatematchingtest(len, binin, verbose):
    if len < 2048:
        Util.verb(verbose, '[-]\n[-] input too short for Overlapping Template Matching Test\n[-]\n', True)
        pval = ''
    else:
        Util.verb(verbose, '[+]\n[+] PERFORMING OVERLAPPING TEMPLATE MATCHING TEST\n[+]\n', False)

        pval = Tests.overlappingtemplatematchingtest(binin)

        Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval


def callrandomexcursionstest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING RANDOM EXCURSIONS TEST\n[+]\n', False)

    pval = Tests.randomexcursionstest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval


def callrandomexcursionsvarianttest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING RANDOM EXCURSIONS VARIANT TEST\n[+]\n', False)

    pval = Tests.randomexcursionsvarianttest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval


def callrunstest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING RUNS TEST\n[+]\n', False)

    pval = Tests.runstest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval


def callserialtest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING SERIAL TEST\n[+]\n', False)

    pval = Tests.serialtest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)
        
    return pval


def callspectraltest(len, binin, verbose):
    Util.verb(verbose, '[+]\n[+] PERFORMING SPECTRAL TEST\n[+]\n', False)

    pval = Tests.spectraltest(binin)

    Util.verb(verbose, '[+] PVAL = %s\n'%pval, False)

    return pval


def callalltests(binin, verbose):

    ##
    ## dict to hold all the pvals
    ##
    ## pvals[0] = binarymatrixranktest
    ## pvals[1] = blockfrequencytest
    ## pvals[2] = cumulativesumstest
    ## pvals[3] = longestcallonestest
    ## pvals[4] = maurersuniversalstatistictest
    ## pvals[5] = monobitfrequencytest
    ## pvals[6] = nonoverlappingtemplatematchingtest
    ## pvals[7] = overlappingtemplatematchingtest
    ## pvals[8] = randomexcursionstest
    ## pvals[9] = randomexcursionsvarianttest
    ## pvals[10] = callstest
    ## pvals[11] = spectraltest
    ## pvals[12] = linearcomplexitytest
    ## pvals[13] = approximateentropytest
    ## pvals[14] = serialtest
    ##

    pvals = {}

    ##
    ## shortest tests first
    ##

    l = len(binin)

    pvals[0] = callbinarymatrixranktest(l, binin, verbose)
    pvals[1] = callblockfrequencytest(l, binin, verbose)
    pvals[2] = callcumulativesumstest(l, binin, verbose)
    pvals[3] = calllongestrunonestest(l, binin, verbose)
    pvals[4] = callmaurersuniversalstatistictest(l, binin, verbose)
    pvals[5] = callmonobitfrequencytest(l, binin, verbose)
    pvals[6] = callnonoverlappingtemplatematchingtest(l, binin, verbose)
    pvals[7] = calloverlappingtemplatematchingtest(l, binin, verbose)
    pvals[8] = callrandomexcursionstest(l, binin, verbose)
    pvals[9] = callrandomexcursionsvarianttest(l, binin, verbose)
    pvals[10] = callrunstest(l, binin, verbose)
    pvals[11] = callspectraltest(l, binin, verbose)

    ##
    ## medium tests next
    ##
    pvals[12] = calllinearcomplexitytest(l, binin, verbose)

    ##
    ## longer tests last
    ##
    pvals[13] = callapproximateentropytest(l, binin, verbose)
    pvals[14] = callserialtest(l, binin, verbose)

    return pvals
