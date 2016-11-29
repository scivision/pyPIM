
if __name__ == '__main__':

    from pypim.pypim import PIMSub

    def example1():

        """ single-point example """

        uthr = 23.
        idn = 323
        iyr = 2003
        alt = 100.
        xlat = -11.95
        xlon = 283.11
        fkp = 1.
        F107 = 144.
        first = 1.

        # Ne in cm-3
        denp = PIMSub(uthr, idn, iyr, alt, xlat, xlon, fkp, F107, first)

        print( '\n' )
        print( 'YEAR = %04i, DOY = %03i, TIME = %8.3f' % (iyr, idn, uthr) )
        print( 'GLON = %8.3f, ALT = %8.3f, GLAT = %8.3f, NE = %12.7e cm-3' % (xlon, alt, xlat, denp) )

    #
    # End of 'example1'
    #####

    example1()
