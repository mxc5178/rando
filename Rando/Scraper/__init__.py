#!/usr/bin/env python

##
## Rando/Scraper/__init__.py
##

###############################################################################
###############################################################################
## DEPENDENCIES:
###############################################################################
###############################################################################
##
##  mechanize
##      http://wwwsearch.sourceforge.net/mechanize/
##
##  BeautifulSoup
##      http://www.crummy.com/software/BeautifulSoup/
##
##  Rando/Util/__init__.py 
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
## import Rando.Scraper as Scraper
##
###############################################################################
###############################################################################

import mechanize 
import os
import hashlib
import time
import Rando.Util as Util
from BeautifulSoup import BeautifulSoup

###############################################################################
###############################################################################
##
## Rando.Scraper.Scraper class
##
###############################################################################
###############################################################################

class Scraper(object):

    def __init__(self, len):
        self.len = len
        userAgent = [('User-agent','Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01')]
        self.browser = mechanize.Browser()
        self.browser.addheaders = userAgent
        self.browser.set_handle_redirect(True)
        self.browser.set_handle_referer(False)
        self.browser.set_handle_refresh(False)
        self.browser.set_handle_robots(False)
        return

    def scrape(self, path, verbose):

        ##
        ## read input file of URLs, scrape and hash.  Return hashes
        ##
        hashes = {}
        with open(path, 'r') as f:
            i = 0;
            for line in f.readlines():

                try:
                    html = self.viewpage(line)
                    hashes[i] = hashlib.sha512(html).hexdigest()
                    Util.verb(verbose, '[+] Hash %s --> %s\n'%(i,hashes[i]), False)
                    i += 1

                except Exception, e:
                    #print e
                    pass

        return hashes

    def genhash(self, hashes, verbose):

        Util.verb(verbose, '[+]\n[+] Preparing to xor hashes and create a random number\n[+]', False)
        
        ##
        ## string the hashes together and xor
        ##
        ## each hash SHA512 hash is 128 hex words == 512 binary bits
        ## divide len by 512 to arrive at stringin pattern
        ##
        ## Example:
        ##  if len = 16384 then 16384/512 = 32
        ##  so, 32 hashes need to be concatenated to create
        ##  a string of 16384 bits long
        ##
        ##  if len = 1024 then 1024/512 = 2
        ##  so, 2 hashes need to be concatenated to create
        ##  a string of 1024 bits long
        ##
        
        longhashes = {}
        r = self.len/512
        
        ##
        ##  - r hashes are needed to create a hash of sufficient length
        ##  - at least r*2 hashes are needed for xor
        ##  - verify that len(hashes) > r*2
        ##  - modulo len(hashes) by r to determine number of extra hashes
        ##  - use extra hashes in clever way
        ##

        if len(hashes) > r*2:
            ##
            ## there are enough hashes
            ##

            residue = len(hashes)%r

            ##
            ## r devides into len(hashes) with remainder residue
            ## therefore len(hashes) = r*n + residue
            ## so loop through r - residue hashes
            ##

            r1 = ''

            for k in range(0, len(hashes)/r):
                #print 'K == %s'%k
                if not k in longhashes:
                    longhashes[k] = ''

                for i in range(k*r, k*r+r):
                    #print 'I == %s'%i
                    longhashes[k] += hashes[i]

                ##
                ## xor the hashes
                ##
                if k < 1:
                    r1 = Util.hex2bin(longhashes[k])
                else:
                    r1 = Util.xor(r1, Util.hex2bin(longhashes[k]))
                
            ##
            ## residue hashes have not been xor'd yet
            ## break r1 into chunks of 512 bits, then xor the chunks 
            ## with all the hashes
            ##
            ## len(hashes)-residue --> pick up where last loop left off
            ##
            for j in range(len(hashes)-residue, len(hashes)):

                stream = ''
                splithash=[r1[x:x+512] for x in range(0,len(r1),512)]
                for h in splithash:
                    stream += Util.xor(h, Util.hex2bin(hashes[j]))

                r1 = stream


            return r1

        else:

            Util.verb(verbose, '[-]\n[-] There are not sufficient hashes to continue\n[-]\n', True)
            return


    def viewpage(self, url):
        page = self.browser.open(url)
        source_code = page.read() 
        return source_code


