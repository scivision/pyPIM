

      program pim_driver

       real uthr,alt,xlat,xlon,fkp,F107,denp
       integer idn,iyr
       integer first
       character*256 dirdata

       uthr = 23.0
       idn = 323
       iyr = 2003
       alt = 100.0
       xlat = -11.95
       xlon = 283.11
       fkp = 1.0
       F107 = 144.0
       first = 1
       dirdata =
     &  '/home/rilma/work/programs/fortran/pim/version-0.0.2/data'

       call pimsub(uthr,idn,iyr,alt,xlat,xlon,fkp,F107,first,
     &  dirdata,denp)

       write(*,*) denp

      end


      subroutine pimsub(uthr,idn,iyr,alt,xlat,xlon,fkp,F107,first,
     & dirdata,denp)

       real uthr,alt,xlat,xlon,fkp,F107,denp
       integer idn,iyr
       integer first
       character*256 dirdata, dirdata1

Cf2py  intent(in) uthr,alt,xlat,xlon,fkp,F107,idn,iyr,first,dirdata
Cf2py  intent(out) denp

       common /folders/ dirdata1

       dirdata1 = trim(dirdata)

       call pim(uthr,idn,iyr,alt,xlat,xlon,fkp,F107,denp,1,first) 

       return

      end


      subroutine pimsubl(uthr,idn,iyr,alt,nalt,xlat,nxlat,xlon,nxlon,
     & fkp,F107,first,dirdata,denp)

       real uthr,fkp,F107
       integer nalt,nxlat,nxlon
       real alt(nalt),xlat(nxlat),xlon(nxlon),denp(nalt)
       integer idn,iyr,first
       character*256 dirdata,dirdata1

Cf2py  intent(in) uthr,idn,iyr,alt,xlat,xlon,fkp,F107,first,dirdata
Cf2py  integer intent(hide),depend(alt) :: nalt=shape(alt,0)
Cf2py  integer intent(hide),depend(xlat) :: nxlat=shape(xlat,0)
Cf2py  integer intent(hide),depend(xlon) :: nxlon=shape(xlon,0)
Cf2py  intent(out) denp

       common /folders/ dirdata1

       dirdata1 = trim(dirdata)

       call pim(uthr,idn,iyr,alt,xlat,xlon,fkp,F107,denp,nalt,first) 

       return       

      end
