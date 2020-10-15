c-----------------------------------------------------------------------
c   
c   This is a small 2D example of conjugate heat transfer in Nek5000.
c   
c   The domain consists of two plates of finite thickness (h=0.5) 
c   with plane Poiseiulle flow moving between the plates from left 
c   to right (x=0 to 8).
c   
c   The gap height is 1.0 (y=0 to 1).
c   
c   The flow inlet temperature is T=0 and the plates are heated
c   with volumetric heat source, qvol = 1.
c
c   Insulated boundary conditions are applied on the solid
c   surfaces that are not interior to the computational domain,
c   so heat leaves only through advection at the flow outlet.
c
c-----------------------------------------------------------------------
      subroutine uservp (ix,iy,iz,ieg)
      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

c      if (ifield.eq.1) then
c         utrans  = param(1)
c         udiff   = param(2)
c
c      else
c         utrans  = param(7)        ! thermal properties
c         udiff   = param(8)

c         if (ieg .gt. nelgv) then  ! properties in the solid
c            udiff   = 0.1*param(8) ! conductivity
c            utrans  = 1.0
c         endif
c      endif

      utrans = 0.0
      udiff = 0.0

      return
      end
c-----------------------------------------------------------------------
      subroutine userf  (ix,iy,iz,ieg)
      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

      ffx = 0.0
      ffy = 6.25*(temp-ps(1))
      ffz = 0.0

      return
      end
c-----------------------------------------------------------------------
      subroutine userq  (ix,iy,iz,ieg)
      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

c      qvol = 0.0
c     if (ieg.gt.nelgv) qvol = 1.0
      if (ifield.eq.2) then
	qvol = -uy
      elseif (ifield.eq.3) then
	qvol = -uy/1.1
      endif

      return
      end
c-----------------------------------------------------------------------
      subroutine userchk()
      include 'SIZE'
      include 'TOTAL'
      include 'RESTART'

      character*80 filename(9999)
      parameter (lt=lx1*ly1*lz1*lelt)
      common /defvar/ wT1(lt)
      ifreguo = .false.
      if (nsteps.eq.0) then
	if (nid.eq.0) then
		open(unit=199,file='filename.list',form='formatted',status='old')
		read(199,*) nfiles
		read(199,'(A80)')(filename(i),i=1,nfiles)
		close(199)
	endif
	call bcast(nfiles,isize)
	call bcast(filename,nfiles*80)
	open(1, file = 'WT.dat', status = 'unknown')
	write(1,'(4a12)') 'time','wTav'
	do i=1,nfiles
		call load_fld(filename(i))
		call col3(wT1,vy,t(1,1,1,1,1),lt)
		wTav = glsc2(wT1,bm1,lt)/voltm1
c		wTav = glsc2(wT1,bm1,lt)/voltm1
c Write this computed flux at each time step to .dat file
		write(1,*) time, wTav
	enddo
	close(1)
      endif

      return
      end
c-----------------------------------------------------------------------
      subroutine userbc (ix,iy,iz,iside,ieg)
c     NOTE ::: This subroutine MAY NOT be called by every process

C     Set boundary conditions

      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

c      ux   = 4.0*y*(1. - y)
c      uy   = 0.0
c      uz   = 0.0

c      temp = 0.0

      return
      end
c-----------------------------------------------------------------------
      subroutine useric (ix,iy,iz,ieg)

C     Set initial conditions

      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

      ux   = 0.0
      uy   = 0.0
      uz   = 0.0

      eps = 1e-4
      beta = 13.*2.*pi/500.
      alpha = 23.*2.*pi/300.

c      temp = -0.001*z
      if (ifield.eq.2) then
c         temp=-0.0002*y
          temp = eps*sin(alpha*x)*cos(beta*y)
      elseif (ifield.eq.3) then
c         temp = -(0.0002/3.)*y
          temp = eps*sin(alpha*x)*cos(beta*y)
      endif

c      if (ifield.eq.2) then
c         if (y>=400) then
c		 temp=-0.125*tanh(2.0*(y-0.5*(500.-400.))/6.)
c         elseif (y>=300 .AND. y<400) then 
c		temp=-0.125*tanh(2.0*(y-0.5*(400.-300.))/6.)
c         elseif (y>=200 .AND. y<300) then
c                temp=-0.125*tanh(2.0*(y-0.5*(300.-200.))/6.)
c         elseif (y>=100 .AND. y<200) then
c                temp=-0.125*tanh(2.0*(y-0.5*(200.-100.))/6.)
c         elseif (y<100) then
c                temp=-0.125*tanh(2.0*(y-0.5*(100.))/6.)
c         endif 
c      elseif (ifield.eq.3) then
c         if (y>=400) then
c                 temp=-(0.125/3.)*tanh(2.0*(y-0.5*(500.-400.))/9.)
c         elseif (y>=300 .AND. y<400) then
c                temp=-(0.125/3.)*tanh(2.0*(y-0.5*(400.-300.))/9.)
c         elseif (y>=200 .AND. y<300) then
c                temp=-(0.125/3.)*tanh(2.0*(y-0.5*(300.-200.))/9.)
c         elseif (y>=100 .AND. y<200) then
c                temp=-(0.125/3.)*tanh(2.0*(y-0.5*(200.-100.))/9.)
c         elseif (y<100) then
c                temp=-(0.125/3.)*tanh(2.0*(y-0.5*(100.))/9.)
c         endif
c      endif


      return
      end
c-----------------------------------------------------------------------
      subroutine usrdat
      include 'SIZE'
      include 'TOTAL'

      return
      end
c-----------------------------------------------------------------------
      subroutine usrdat2
      include 'SIZE'
      include 'TOTAL'

      return
      end
c-----------------------------------------------------------------------
      subroutine usrdat3
      return
      end
c-----------------------------------------------------------------------

c automatically added by makenek
      subroutine usrdat0() 

      return
      end

c automatically added by makenek
      subroutine usrsetvert(glo_num,nel,nx,ny,nz) ! to modify glo_num
      integer*8 glo_num(1)

      return
      end

c automatically added by makenek
      subroutine userqtl

      call userqtl_scig

      return
      end
