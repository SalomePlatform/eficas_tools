# Check availability of Salome's PAL binary distribution
#
# Author : Guillaume Boulant (CSSI - 03/08/2005)
#

AC_DEFUN([CHECK_PAL],[

AC_CHECKING(for Pal)

pal_ok=no

AC_ARG_WITH(pal,
	    [  --with-pal=DIR               root directory path of PAL build or installation],
	    PAL_DIR="$withval",PAL_DIR="")

if test "x$PAL_DIR" = "x" ; then

# no --with-pal-dir option used

   if test "x$PAL_ROOT_DIR" != "x" ; then

    # PAL_ROOT_DIR environment variable defined
      PAL_DIR=$PAL_ROOT_DIR

   else
      AC_MSG_WARN("PAL_ROOT_DIR is not defined")
   fi
fi

if test -f ${PAL_DIR}/bin/salome/testAppli ; then
   pal_ok=yes
   AC_MSG_RESULT(Using Pal module distribution in ${PAL_DIR})

   if test "x$PAL_ROOT_DIR" = "x" ; then
      PAL_ROOT_DIR=${PAL_DIR}
   fi
   if test "x$PAL_SITE_DIR" = "x" ; then
      PAL_SITE_DIR=${PAL_ROOT_DIR}
   fi
   AC_SUBST(PAL_ROOT_DIR)
   AC_SUBST(PAL_SITE_DIR)

else
   AC_MSG_WARN("Cannot find compiled Pal module distribution")
fi

AC_MSG_RESULT(for Pal: $pal_ok)
 
])dnl
 
