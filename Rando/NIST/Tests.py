#!/usr/bin/env python

##
## Rando/NIST/Tests.py
##

###############################################################################
###############################################################################
## DEPENDENCIES:
###############################################################################
###############################################################################
##
##  scipy
##  numpy
##
##  Rando.NIST.Util 
##
###############################################################################
###############################################################################
##
## TODO:
##  deal with 128 bit longestrunones test
##
###############################################################################
###############################################################################
## USAGE
###############################################################################
###############################################################################
##
## import Rando.NIST.Tests as Tests
##
###############################################################################
###############################################################################

import os
import numpy as np
import scipy.special as spc
import scipy.stats as sst
import scipy.fftpack as sff

import Rando.NIST.Util as Util

###############################################################################
###############################################################################
##
## NIST Tests class
##
###############################################################################
###############################################################################


def approximateentropytest(binin, m=10):
    ##
    ## Focus:
    ##  test the frequency of each and every overlapping m-bit pattern. 
    ##
    ## Purpose:
    ##  compare the frequency of overlapping blocks of two 
    ##  consecutive/adjacent lengths (m and m+1) against the expected 
    ##  result for a random sequence.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence 
    ##  is non-random. Otherwise, conclude that the sequence is random.
    ##

    n = len(binin)
    f1a = [(binin + binin[0:m - 1:])[xs:m + xs:] for xs in xrange(n)]
    f1 = [[xs, f1a.count(xs)] for xs in sorted(set(f1a))]
    f2a = [(binin + binin[0:m:])[xs:m + 1 + xs:] for xs in xrange(n)]
    f2 = [[xs, f2a.count(xs)] for xs in sorted(set(f2a))]
    c1 = [1.0 * f1[xs][1] / n for xs in xrange(len(f1))]
    c2 = [1.0 * f2[xs][1] / n for xs in xrange(len(f2))]
    phi1 = reduce(Util.su, map(Util.logo, c1))
    phi2 = reduce(Util.su, map(Util.logo, c2))
    apen = phi1 - phi2
    chisqr = 2.0 * n * (np.log(2) - apen)
    pval = spc.gammaincc(2 ** (m - 1), chisqr / 2.0)
    return pval


def mrank(matrix): 
    ##
    ## matrix rank as defined in the NIST specification
    ##
    m=len(matrix)
    leni=len(matrix[0])
    def proc(mat):
        for i in xrange(m):
            if mat[i][i]==0:
                for j in xrange(i+1,m):
                    if mat[j][i]==1:
                        mat[j],mat[i]=mat[i],mat[j]
                        break
            if mat[i][i]==1:
                for j in xrange(i+1,m):
                    if mat[j][i]==1: mat[j]=[mat[i][x]^mat[j][x] for x in xrange(leni)]
        return mat
    maa=proc(matrix)
    maa.reverse()
    mu=[i[::-1] for i in maa]
    muu=proc(mu)
    ra=np.sum(np.sign([xx.sum() for xx in np.array(mu)]))
    return ra


def binarymatrixranktest(binin,m=32,q=32):
    ##
    ## Focus:
    ##  test is the rank of disjoint sub-matrices of the entire sequence. 
    ##
    ## Purpose: 
    ##  check for linear dependence among fixed 
    ##  length substrings of the original sequence.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence 
    ##  is non-random. Otherwise, conclude that the sequence is random.
    ##

    p1 = 1.0
    for x in xrange(1,50): p1*=1-(1.0/(2**x))
    p2 = 2*p1
    p3 = 1-p1-p2;
    n=len(binin)

    ##
    ## the input string as numbers, to generate the dot product 
    ##
    u=[int(el) for el in binin] 
    f1a = [u[xs*m:xs*m+m:] for xs in xrange(n/m)]
    n=len(f1a)
    f2a = [f1a[xs*q:xs*q+q:] for xs in xrange(n/q)]
    r=map(mrank,f2a)
    n=len(r)
    fm=r.count(m);
    fm1=r.count(m-1);
    chisqr=((fm-p1*n)**2)/(p1*n)+((fm1-p2*n)**2)/(p2*n)+((n-fm-fm1-p3*n)**2)/(p3*n);
    pval=np.exp(-0.5*chisqr)
    return pval


def blockfrequencytest(binin, nu=128):
    ##
    ## Focus:
    ##  test the proportion of zeroes and ones within M-bit blocks. 
    ##
    ## Purpose:
    ##   determine whether the frequency of ones is an M-bit block is approximately M/2
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence is non-random. 
    ##  Otherwise, conclude that the sequence is random.
    ##

    ss = [int(el) for el in binin]
    tt = [1.0 * sum(ss[xs * nu:nu + xs * nu:]) / nu for xs in xrange(len(ss) / nu)]
    uu = map(Util.sus, tt)
    chisqr = 4 * nu * reduce(Util.su, uu)
    pval = spc.gammaincc(len(tt) / 2.0, chisqr / 2.0)
    return pval

def cumulativesumstest(binin):
    ##
    ## Focus:
    ##  test the maximal excursion (from zero) of the random walk 
    ##  defined by the cumulative sum of adjusted (-1, +1) digits 
    ##  in the sequence.
    ## 
    ## Purpose:
    ##  determine whether the cumulative sum of the partial sequences 
    ##  occurring in the tested sequence is too large or too small 
    ##  relative to the expected behavior of that cumulative sum for 
    ##  random sequences.  This cumulative sum may be considered as a 
    ##  random walk. For a random sequence, the random walk should be 
    ##  near zero. For non-random sequences, the excursions of this random 
    ##  walk away from zero will be too large.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence 
    ##  is non-random. Otherwise, conclude that the sequence is random.
    ##

    n = len(binin)
    ss = [int(el) for el in binin]
    sc = map(Util.sumi, ss)
    cs = np.cumsum(sc)
    z = max(abs(cs))
    ra = 0
    start = int(np.floor(0.25 * np.floor(-n / z) + 1))
    stop = int(np.floor(0.25 * np.floor(n / z) - 1))
    pv1 = []
    for k in xrange(start, stop + 1):
        pv1.append(sst.norm.cdf((4 * k + 1) * z / np.sqrt(n)) - sst.norm.cdf((4 * k - 1) * z / np.sqrt(n)))
    start = int(np.floor(0.25 * np.floor(-n / z - 3)))
    stop = int(np.floor(0.25 * np.floor(n / z) - 1))
    pv2 = []
    for k in xrange(start, stop + 1):
        pv2.append(sst.norm.cdf((4 * k + 3) * z / np.sqrt(n)) - sst.norm.cdf((4 * k + 1) * z / np.sqrt(n)))
    pval = 1
    pval -= reduce(Util.su, pv1)
    pval += reduce(Util.su, pv2)

    return pval


def cumulativesumstestreverse(binin):
    ## 
    ## Focus:
    ##  test the maximal excursion (from zero) of the random walk defined by 
    ##  the cumulative sum of adjusted (-1, +1) digits in the sequence.
    ##
    ## Purpose:
    ##  determine whether the cumulative sum of the partial sequences occurring 
    ##  in the tested sequence is too large or too small relative to the expected 
    ##  behavior of that cumulative sum for random sequences.  This cumulative 
    ##  sum may be considered as a random walk. For a random sequence, the random 
    ##  walk should be near zero. For non-random sequences, the excursions of 
    ##  this random walk away from zero will be too large.
    ##

    pval=cumulativesumstest(binin[::-1])
    return pval


def lincomplex(binin):
    lenn=len(binin)
    c=b=np.zeros(lenn)
    c[0]=b[0]=1
    l=0
    m=-1
    n=0

    ##
    ## the input string as numbers, to generate the dot product
    ##
    u=[int(el) for el in binin] 
    p=99
    while n<lenn:
        v=u[(n-l):n] # was n-l..n-1
        v.reverse()
        cc=c[1:l+1] # was 2..l+1
        d=(u[n]+np.dot(v,cc))%2
        if d==1:
            tmp=c
            p=np.zeros(lenn)
            for i in xrange(0,l): # was 1..l+1
                 if b[i]==1: 
                     p[i+n-m]=1
            c=(c+p)%2;
            if l<=0.5*n: # was if 2l <= n
                 l=n+1-l
                 m=n
                 b=tmp
        n+=1
    return l

def linearcomplexitytest(binin,m=500):
    ##
    ## Focus:
    ##  test the length of a generating feedback register.
    ##
    ## Purpose:
    ##  determine whether or not the sequence is complex enough to 
    ##  be considered random. Random sequences are characterized by a longer 
    ##  feedback register. A short feedback register implies non-randomness.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence 
    ##  is non-random. Otherwise, conclude that the sequence is random.
    ##

    k = 6
    pi = [0.01047, 0.03125, 0.125, 0.5, 0.25, 0.0625, 0.020833]
    avg = 0.5*m + (1.0/36)*(9 + (-1)**(m + 1)) - (m/3.0 + 2.0/9)/2**m
    blocks = Util.stringpart(binin, m)
    bign = len(blocks)
    lc = ([lincomplex(chunk) for chunk in blocks])
    t = ([-1.0*(((-1)**m)*(chunk-avg)+2.0/9) for chunk in lc])
    vg=np.histogram(t,bins=[-9999999999,-2.5,-1.5,-0.5,0.5,1.5,2.5,9999999999])[0][::-1]
    im=([((vg[ii]-bign*pi[ii])**2)/(bign*pi[ii]) for ii in xrange(7)])
    chisqr=reduce(Util.su,im)
    pval=spc.gammaincc(k/2.0,chisqr/2.0)
    return pval


def longestrunonestest(binin):
    ##
    ## Focus:
    ##  test the longest run of ones within M-bit blocks.
    ##
    ## Purpose:
    ##  determine whether the length of the longest run of ones 
    ##  within the tested sequence is consistent with the length 
    ##  of the longest run of ones that would be expected in a 
    ##  random sequence. Note that an irregularity in the expected 
    ##  length of the longest run of ones implies that there is also 
    ##  an irregularity in the expected length of the longest run of 
    ##  zeroes. Long runs of zeroes were not evaluated separately due 
    ##  to a concern about statistical independence among the tests.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the 
    ##  sequence is non-random. Otherwise, conclude that the sequence 
    ##  is random.
    ##

    m = 8
    k = 3
    pik = [0.2148, 0.3672, 0.2305, 0.1875]
    blocks = [binin[xs*m:m+xs*m:] for xs in xrange(len(binin) / m)]
    n = len(blocks)

    ##
    ## append the string 01 to guarantee the length of 1
    ##
    counts1 = [xs+'01' for xs in blocks] 

    ##
    ## split into all parts
    ##
    counts = [xs.replace('0',' ').split() for xs in counts1] 
    counts2 = [map(len, xx) for xx in counts]
    counts4 = [(4 if xx > 4 else xx) for xx in map(max,counts2)]
    freqs = [counts4.count(spi) for spi in [1, 2, 3, 4]]
    chisqr1 = [(freqs[xx]-n*pik[xx])**2/(n*pik[xx]) for xx in xrange(4)]
    chisqr = reduce(Util.su, chisqr1)
    pval = spc.gammaincc(k / 2.0, chisqr / 2.0)
    return pval

def maurersuniversalstatistictest(binin,l=7,q=1280):
    ##
    ## Focus:
    ##   test the number of bits between matching patterns.
    ##
    ## Purpose:
    ##  detect whether or not the sequence can be significantly compressed 
    ##  without loss of information. An overly compressible sequence is 
    ##  considered to be non-random.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence 
    ##  is non-random. Otherwise, conclude that the sequence is random.
    ##

    ru = [
        [0.7326495, 0.690],
        [1.5374383, 1.338],
        [2.4016068, 1.901],
        [3.3112247, 2.358],
        [4.2534266, 2.705],
        [5.2177052, 2.954],
        [6.1962507, 3.125],
        [7.1836656, 3.238],
        [8.1764248, 3.311],
        [9.1723243, 3.356],
        [10.170032, 3.384],
        [11.168765, 3.401],
        [12.168070, 3.410],
        [13.167693, 3.416],
        [14.167488, 3.419],
        [15.167379, 3.421],
        ]
    blocks = [int(li, 2) + 1 for li in Util.stringpart(binin, l)]
    k = len(blocks) - q
    states = [0 for x in xrange(2**l)]
    for x in xrange(q):
        states[blocks[x]-1]=x+1
    sumi=0.0
    for x in xrange(q,len(blocks)):
        sumi+=np.log2((x+1)-states[blocks[x]-1])
        states[blocks[x]-1] = x+1
    fn = sumi / k
    c=0.7-(0.8/l)+(4+(32.0/l))*((k**(-3.0/l))/15)
    sigma=c*np.sqrt((ru[l-1][1])/k)
    pval = spc.erfc(abs(fn-ru[l-1][0]) / (np.sqrt(2)*sigma))
    return pval

def monobitfrequencytest(binin):
    ##
    ## Focus: 
    ##  test the proportion of zeroes and ones for the entire sequence. 
    ##
    ## Purpose: 
    ##  determine whether that number of ones and zeros in a sequence 
    ##  are approximately the same as would be expected for a truly 
    ##  random sequence. 
    ##
    ## Outcome:
    ##  The test assesses the closeness of the fraction of ones to 1/2, 
    ##  that is, the number of ones and zeroes in a sequence should be about the same.
    ##
    ##  If the computed P-value is < 0.01, then conclude that the sequence is non-random. 
    ##  Otherwise, conclude that the sequence is random. 
    ##

    ss = [int(el) for el in binin]
    sc = map(Util.sumi, ss)
    sn = reduce(Util.su, sc)
    sobs = np.abs(sn) / np.sqrt(len(binin))
    pval = spc.erfc(sobs / np.sqrt(2))
    return pval


def nonoverlappingtemplatematchingtest(binin, mat="000000001", num=8):
    ##
    ## Focus:
    ##  test the number of occurrences of pre-defined target substrings. 
    ##
    ## Purpose: 
    ##  reject sequences that exhibit too many occurrences of a given 
    ##  non-periodic (aperiodic) pattern. For this test and for the 
    ##  Overlapping Template Matching test, an m-bit window is used to 
    ##  search for a specific m-bit pattern. If the pattern is not found, 
    ##  the window slides one bit position. For this test, when the pattern 
    ##  is found, the window is reset to the bit after the found pattern,
    ##   and the search resumes.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence is 
    ##  non-random. Otherwise, conclude that the sequence is random.
    ##

    n = len(binin)
    m = len(mat)
    M = n/num
    blocks = [binin[xs*M:M+xs*M:] for xs in xrange(n/M)]
    counts = [xx.count(mat) for xx in blocks]
    avg = 1.0 * (M-m+1)/2 ** m
    var = M*(2**-m -(2*m-1)*2**(-2*m))
    chisqr = reduce(Util.su, [(xs - avg) ** 2 for xs in counts]) / var
    pval = spc.gammaincc(1.0 * len(blocks) / 2, chisqr / 2)
    return pval


def overlappingtemplatematchingtest(binin,mat="111111111",num=1032,numi=5):
    ##
    ## Focus:
    ##   test the number of pre-defined target substrings.
    ##
    ## Purpose: 
    ##  to reject sequences that show deviations from the expected number of 
    ##  runs of ones of a given length. Note that when there is a deviation 
    ##  from the expected number of ones of a given length, there is also a 
    ##  deviation in the runs of zeroes. Runs of zeroes were not evaluated 
    ##  separately due to a concern about statistical independence among the 
    ##  tests. For this test and for the Non-overlapping Template Matching 
    ##  test, an m-bit window is used to search for a specific m-bit pattern. 
    ##  If the pattern is not found, the window slides one bit position. For 
    ##  this test, when the pattern is found, the window again slides one bit, 
    ##  and the search is resumed.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence is 
    ##  non-random. Otherwise, conclude that the sequence is random.
    ##

    n = len(binin)
    bign = int(n / num)
    m = len(mat)
    lamda = 1.0 * (num - m + 1) / 2 ** m
    eta = 0.5 * lamda
    pi = [Util.pr(i, eta) for i in xrange(numi)]
    pi.append(1 - reduce(Util.su, pi))
    v = [0 for x in xrange(numi + 1)]
    blocks = Util.stringpart(binin, num)
    blocklen = len(blocks[0])
    counts = [Util.occurances(i,mat) for i in blocks]
    counts2 = [(numi if xx > numi else xx) for xx in counts]
    for i in counts2: v[i] = v[i] + 1
    chisqr = reduce(Util.su, [(v[i]-bign*pi[i])** 2 / (bign*pi[i]) for i in xrange(numi + 1)])
    pval = spc.gammaincc(0.5*numi, 0.5*chisqr)
    return pval

def randomexcursionstest(binin):
    ##
    ## Focus:
    ##  test the number of cycles having exactly K visits in a cumulative 
    ##  sum random walk. The cumulative sum random walk is found if partial 
    ##  sums of the (0,1) sequence are adjusted to (-1, +1). A random 
    ##  excursion of a random walk consists of a sequence of n steps of unit 
    ##  length taken at random that begin at and return to the origin.
    ##
    ## Purpose:
    ##  determine if the number of visits to a state within a random walk 
    ##  exceeds what one would expect for a random sequence.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence is 
    ##  non-random. Otherwise, conclude that the sequence is random.
    ##

    xvals=[-4, -3, -2, -1, 1, 2, 3, 4]
    ss = [int(el) for el in binin]
    sc = map(Util.sumi,ss)
    cumsum = np.cumsum(sc)
    cumsum = np.append(cumsum,0)
    cumsum = np.append(0,cumsum)
    posi=np.where(cumsum==0)[0]
    cycles=([cumsum[posi[x]:posi[x+1]+1] for x in xrange(len(posi)-1)])
    j=len(cycles)
    sct=[]
    for ii in cycles:
        sct.append(([len(np.where(ii==xx)[0]) for xx in xvals]))
    sct=np.transpose(np.clip(sct,0,5))
    su=[]
    for ii in xrange(6):
        su.append([(xx==ii).sum() for xx in sct])
    su=np.transpose(su)
    pikt=([([Util.pik(uu,xx) for uu in xrange(6)]) for xx in xvals])
    # chitab=1.0*((su-j*pikt)**2)/(j*pikt)
    chitab=np.sum(1.0*(np.array(su)-j*np.array(pikt))**2/(j*np.array(pikt)),axis=1)
    pval=([spc.gammaincc(2.5,cs/2.0) for cs in chitab])
    return pval


def randomexcursionsvarianttest(binin):
    ##
    ## Focus:
    ##  test the number of times that a particular state occurs in a 
    ##  cumulative sum random walk.
    ##
    ## Purpose: 
    ##  of this test is to detect deviations from the expected number 
    ##  of occurrences of various states in the random walk.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence
    ##  is non-random. Otherwise, conclude that the sequence is random.
    ##

    ss = [int(el) for el in binin]
    sc = map(Util.sumi, ss)
    cs = np.cumsum(sc)
    li = []
    for xs in sorted(set(cs)):
        if np.abs(xs) <= 9:
            li.append([xs, len(np.where(cs == xs)[0])])
    j = Util.getfreq(li, 0) + 1
    pval = []
    for xs in xrange(-9, 9 + 1):
        if not xs == 0:
            pval.append(spc.erfc(np.abs(Util.getfreq(li, xs) - j) / np.sqrt(2 * j * (4 * np.abs(xs) - 2))))
    return pval


def runstest(binin):
    ##
    ## Focus:
    ##  test the total number of zero and one runs in the entire sequence, 
    ##  where a run is an uninterrupted sequence of identical bits. 
    ##  A run of length k means that a run consists of exactly k identical 
    ##  bits and is bounded before and after with a bit of the opposite value. 
    ##
    ## Purpose: 
    ##  determine whether the number of runs of ones and zeros of various 
    ##  lengths is as expected for a random sequence. In particular, this 
    ##  test determines whether the oscillation between such substrings is 
    ##  too fast or too slow.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence 
    ##  is non-random. Otherwise, conclude that the sequence is random.
    ##

    ss = [int(el) for el in binin]
    n = len(binin)
    pi = 1.0 * reduce(Util.su, ss) / n
    vobs = len(binin.replace('0', ' ').split()) + len(binin.replace('1' , ' ').split())
    pval = spc.erfc(abs(vobs-2*n*pi*(1-pi)) / (2 * pi * (1 - pi) * np.sqrt(2*n)))
    return pval


def serialtest(binin, m=16):
    ##
    ## Focus:
    ##  test the frequency of each and every overlapping m-bit pattern 
    ##  across the entire sequence.
    ##
    ## Purpose:
    ##  determine whether the number of occurrences of the 2m m-bit 
    ##  overlapping patterns is approximately the same as would be 
    ##  expected for a random sequence. The pattern can overlap.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence 
    ##  is non-random. Otherwise, conclude that the sequence is random.
    ##

    n = len(binin)
    hbin=binin+binin[0:m-1:]
    f1a = [hbin[xs:m+xs:] for xs in xrange(n)]
    oo=set(f1a)
    f1 = [f1a.count(xs)**2 for xs in oo]
    f1 = map(f1a.count,oo)
    cou=f1a.count
    f2a = [hbin[xs:m-1+xs:] for xs in xrange(n)]
    f2 = [f2a.count(xs)**2 for xs in set(f2a)]
    f3a = [hbin[xs:m-2+xs:] for xs in xrange(n)]
    f3 = [f3a.count(xs)**2 for xs in set(f3a)]
    psim1 = 0
    psim2 = 0
    psim3 = 0
    if m >= 0:
        suss = reduce(Util.su,f1)
        psim1 = 1.0 * 2 ** m * suss / n - n
    if m >= 1:
        suss = reduce(Util.su,f2)
        psim2 = 1.0 * 2 ** (m - 1) * suss / n - n
    if m >= 2:
        suss = reduce(Util.su,f3)
        psim3 = 1.0 * 2 ** (m - 2) * suss / n - n
    d1 = psim1-psim2
    d2 = psim1-2 * psim2 + psim3
    pval1 = spc.gammaincc(2 ** (m - 2), d1 / 2.0)
    pval2 = spc.gammaincc(2 ** (m - 3), d2 / 2.0)
    return [pval1, pval2]


def spectraltest(binin):
    ##
    ## Focus:
    ##  test the peak heights in the discrete Fast Fourier Transform. 
    ##
    ## Purpose:
    ##  detect periodic features (i.e., repetitive patterns that 
    ##  are near each other) in the tested sequence that would indicate 
    ##  a deviation from the assumption of randomness.
    ##
    ## Outcome:
    ##  If the computed P-value is < 0.01, then conclude that the sequence is 
    ##  non-random. Otherwise, conclude that the sequence is random.
    ##

    n = len(binin)
    ss = [int(el) for el in binin]
    sc = map(Util.sumi, ss)
    ft = sff.fft(sc)
    af = abs(ft)[1:n/2+1:]
    t = np.sqrt(np.log(1/0.05)*n)
    n0 = 0.95*n/2
    n1 = len(np.where(af<t)[0])
    d = (n1 - n0)/np.sqrt(n*0.95*0.05/4)
    pval = spc.erfc(abs(d)/np.sqrt(2))
    return pval

