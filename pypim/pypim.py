from os.path import dirname, join, realpath
from .pimne import pimsub

# Defines folder location of PIM data files 
dirdata = join(dirname(realpath(__file__)), 'data')

    
def PIMSub(uthr=23., idn=323, iyr=2003, alt=100., xlat=-11.95,
    xlon=283.11, fkp=1., F107=144., first=1.):

    """ PIM single value """

    return pimsub(uthr, idn, iyr, alt, xlat, xlon, fkp, F107, first, dirdata)