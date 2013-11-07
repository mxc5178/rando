#!/usr/bin/env python

##
## Rando/Util/Archiver.py
##

###############################################################################
###############################################################################
## DEPENDENCIES:
###############################################################################
###############################################################################
##
##
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
## import RANDO.Util.Archiver as Archiver
##
###############################################################################
###############################################################################

import subprocess
import os
import time
import datetime

import Rando.Util as Util

###############################################################################
###############################################################################
##
## RANDO.Util.Archiver
##
###############################################################################
###############################################################################


def archive(pathlist, verbose):
    archivelist = []
    path = reduce(os.path.join, pathlist)
    for root, dirs, files in os.walk(path):
        for i in files:
            p = os.path.join(path, i)

            atime = datetime.datetime.strptime(time.ctime(os.path.getmtime(p)), "%a %b %d %H:%M:%S %Y")
            now = datetime.datetime.strptime(time.ctime(int(time.time())), "%a %b %d %H:%M:%S %Y")

            if now - atime > datetime.timedelta(hours = 8):
                ##
                ## file is older than a day ... add to archive list
                ##
                #print 'FILES OLDER THAN 8 hours'
                archivelist.append(p)

    if len(archivelist) > 0:
        ##
        ## check for existing arhive directory
        ##

        dir = str(datetime.datetime.now()-datetime.timedelta(days=1)).split(' ')[0]

        if not os.path.isdir(os.path.join(path, 'archive')):
            ##
            ## create the archive directory (return false after first run)
            ##
            cmd = ['mkdir', os.path.join(path, 'archive')]
            (out, err) = Util.call(cmd, False, None, None)
        
        dir1 = dir.split('-')[0]
        dir2 = dir.split('-')[1]
        dir3 = dir.split('-')[2]

        if not os.path.isdir(os.path.join(path, 'archive', dir1)):
            ##
            ## create the year directory
            ##
            cmd = ['mkdir', os.path.join(path, 'archive', dir1)]
            (out, err) = Util.call(cmd, False, None, None)
            
        if not os.path.isdir(os.path.join(path, 'archive', dir1, dir2)):
            ##
            ## create the month directory
            ##
            cmd = ['mkdir', os.path.join(path, 'archive', dir1, dir2)]
            (out, err) = Util.call(cmd, False, None, None)
            
        if not os.path.isdir(os.path.join(path, 'archive', dir1, dir2, dir3)):
            ##
            ## create the day directory
            ##
            cmd = ['mkdir', os.path.join(path, 'archive', dir1, dir2, dir3)]
            (out, err) = Util.call(cmd, False, None, None)

        for f in archivelist:
            Util.verb(verbose, '[+]\n[+] Archiving %s\n[+]\n'%f, False)
            cmd = ['mv', f, os.path.join(path, 'archive', dir1, dir2, dir3)]
            (out, err) = Util.call(cmd, False, None, None)
