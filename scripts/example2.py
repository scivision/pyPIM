
if __name__ == '__main__':

    from pypim.pypim import PIMSub
    from scipy import arange


    def example2():

        """ height-profile example """

        uthr = 23.
        idn = 323
        iyr = 2003

        xlat = -11.95
        xlon = 283.11
        fkp = 1.0
        F107 = 144.0
        first = 1.

        print( '\n' )
        print( 'YEAR = {:d}, DOY = {:d}, TIME = {:8.3f}'.format(iyr, idn, uthr) )
        print( '\n' )
        for alt in arange(100., 1000., 50):

            # Ne in cm-3
            denp = PIMSub(uthr, idn, iyr, alt, xlat, xlon, fkp, F107, first)

            print( 'GLON = {:8.3f}, ALT = {:8.3f}, GLAT = {:8.3f}, NE = {:12.7e} cm-3'.format(xlon, alt, xlat, denp) )

        print( '\n' )
        #
        # End of 'example2'
        #####

    example2()
        