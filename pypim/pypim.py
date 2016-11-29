from os.path import dirname, join, realpath
from .pimne import pimsub, pimsubl
from scipy import linspace

# Defines folder location of PIM data files 
dirdata = join(dirname(realpath(__file__)), 'data')

    
def PIMSub(uthr=23., idn=323, iyr=2003, alt=100., xlat=-11.95,
    xlon=283.11, fkp=1., F107=144., first=1.):

    """ PIM single value """

    return pimsub(uthr, idn, iyr, alt, xlat, xlon, fkp, F107, first, dirdata)


def PIMSubl(uthr=23., idn=323, iyr=2003, 
    alt=linspace(100.,1000.,10), 
    xlat=[-11.95]*10,
    xlon=[-76.77]*10, 
    fkp=1., F107=144., first=1.):

    """ PIM 1D array values """

    return pimsubl(uthr, idn, iyr, alt, xlat, xlon, fkp, F107, first, dirdata)
