# Check availability of Salome's VISU binary distribution
#
# Author : Jerome Roy (CEA, 2003)
#

AC_DEFUN([CHECK_VISU],[

AC_CHECKING(for Visu)

Visu_ok=no

AC_ARG_WITH(visu,
	    [  --with-visu=DIR               root directory path of VISU build or installation],
	    VISU_DIR="$withval",VISU_DIR="")

if test "x$VISU_DIR" = "x" ; then

# no --with-visu-dir option used

   if test "x$VISU_ROOT_DIR" != "x" ; then

    # VISU_ROOT_DIR environment variable defined
      VISU_DIR=$VISU_ROOT_DIR

   else

    # search Visu binaries in PATH variable
      AC_PATH_PROG(TEMP, runSalome)
      if test "x$TEMP" != "x" ; then
         VISU_BIN_DIR=`dirname $TEMP`
         VISU_DIR=`dirname $VISU_BIN_DIR`
      fi
      
   fi
# 
fi

if test -f ${VISU_DIR}/bin/salome/visu.py ; then
   Visu_ok=yes
   AC_MSG_RESULT(Using Visu module distribution in ${VISU_DIR})

   if test "x$VISU_ROOT_DIR" = "x" ; then
      VISU_ROOT_DIR=${VISU_DIR}
   fi
   if test "x$VISU_SITE_DIR" = "x" ; then
      VISU_SITE_DIR=${VISU_ROOT_DIR}
   fi
   AC_SUBST(VISU_ROOT_DIR)
   AC_SUBST(VISU_SITE_DIR)

else
   AC_MSG_WARN("Cannot find compiled Visu module distribution")
fi

AC_MSG_RESULT(for Visu: $Visu_ok)
 
])dnl
 
