
from os.path import dirname, join, realpath
from pypim.pimne import pimsub
from pypim import pimne

# Defines folder location of PIM data files 
dirdata = join(dirname(realpath(__file__)), 'data')


class pypim(object):
    
    def __init__(self, uthr=23., idn=323, iyr=2003, alt=100., xlat=-11.95,
        xlon=283.11, fkp=1., F107=144., first=1.):

        """ PIM single value """

        return pimne.pimsub(uthr, idn, iyr, alt, xlat, xlon, fkp, F107, first, dirdata)
