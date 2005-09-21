# Check availability of Qt's msg2qm tool binary distribution
#
# Author : Jerome Roy (CEA, 2003)
#

AC_DEFUN([CHECK_MSG2QM],[
AC_CHECKING(for msg2qm)

msg2qm_ok=no

AC_ARG_WITH(msg2qm,
	    [ --with-msg2qm=root_directory_path_of_MSG2QM_installation],
	    MSG2QM_DIR="$withval",MSG2QM_DIR="")

if test "x$MSG2QM_DIR" == "x" ; then
   # no --with-MSG2QM-dir option used
   if test "x$MSG2QM_ROOT" != "x" ; then
      # MSG2QM_ROOT environment variable defined
      MSG2QM_DIR=$MSG2QM_ROOT
   else
      # search MSG2QM binaries in PATH variable
      AC_PATH_PROG(TEMP, msg2qm)
      if test "x$TEMP" != "x" ; then
         MSG2QM_DIR=`dirname $TEMP`
      fi
   fi
fi

# look for msg2qm in ${MSG2QM_DIR} directory
if test -f ${MSG2QM_DIR}/msg2qm ; then
   msg2qm_ok=yes
   MSG2QM="${MSG2QM_DIR}/msg2qm"
   AC_MSG_RESULT(Using MSG2QM executable in ${MSG2QM_DIR})
else
   # if not found, look for msg2qm in ${MSG2QM_DIR}/bin directory
   if test -f ${MSG2QM_DIR}/bin/msg2qm ; then
      msg2qm_ok=yes
      MSG2QM="${MSG2QM_DIR}/bin/msg2qm"
      AC_MSG_RESULT(Using MSG2QM executable in ${MSG2QM_DIR}/bin)
   fi
fi

if test "$msg2qm_ok" == "no"; then
   # At last, let's have a look in SALOME (until V2.2.X)
   SALOME_MSG2QM=${KERNEL_ROOT_DIR}/bin/salome/msg2qm   
   if test -f $SALOME_MSG2QM ; then
      msg2qm_ok=yes
      MSG2QM=${SALOME_MSG2QM}
      AC_MSG_RESULT(Using MSG2QM executable provided with SALOME KERNEL)
   else
      AC_MSG_WARN("Cannot find MSG2QM executable in SALOME")
   fi
fi

AC_SUBST(MSG2QM)
AC_MSG_RESULT(for MSG2QM: $msg2qm_ok)
 
])dnl
 
