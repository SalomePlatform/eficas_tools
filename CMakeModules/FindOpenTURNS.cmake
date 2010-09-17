# - Try to find OpenTURNS
# Once done this will define
#
#  OpenTURNS_FOUND - system has OT
#  OpenTURNS_INCLUDE_DIR - the OT include directory
#  OpenTURNS_INCLUDE_DIRS - the OT include directory and dependencies include directories
#  OpenTURNS_LIBRARY - Where to find the OT library
#  OpenTURNS_LIBRARIES - Link these to use OT
#  OpenTURNS_WRAPPER_DIR - Wrappers directory
#  OpenTURNS_WRAPPER_DEFINITIONS - Compiler switches required for using OT wrapper
#  OpenTURNS_MODULE_DIR - OT module directory
#  OpenTURNS_MODULE_DEFINITIONS - Compiler switches required for using OT module
#  OpenTURNS_SWIG_INCLUDE_DIR - the OT include directory to swig interface
#
#  Copyright (c) 2009 Mathieu Lapointe <lapointe@phimeca.com>
#  Copyright (c) 2010 Julien Schueller <schueller@phimeca.com>
#
#  Redistribution and use is allowed according to the terms of the New
#  BSD license.
#  For details see the accompanying COPYING-CMAKE-SCRIPTS file.
#

include (CheckFunctionExists)
include (CheckIncludeFile)
include (CheckIncludeFileCXX)
include (FindPackageHandleStandardArgs)

# check dependencies
find_package(LibXml2 2.6.27)
find_package(PythonLibs ${PYTHON_VERSION})

# test if variables are not already in cache
if (NOT (OpenTURNS_INCLUDE_DIR
          AND OpenTURNS_SWIG_INCLUDE_DIR
          AND OpenTURNS_INCLUDE_DIRS
          AND OpenTURNS_LIBRARY
          AND OpenTURNS_LIBRARIES
          AND OpenTURNS_WRAPPER_DIR
          AND OpenTURNS_PYTHON_MODULE_DIR
          AND OpenTURNS_MODULE_DIR))

  # set include dir
  if (NOT OpenTURNS_INCLUDE_DIR)
    find_path (OpenTURNS_INCLUDE_DIR
      NAMES
        OT.hxx
      HINTS
        ${OPENTURNS_DIR}
        /usr
        /usr/local
        /opt
      PATH_SUFFIXES
        include/openturns
      DOC
        "OpenTURNS include directory"
    )
  endif ()

  # set swig include dir
  if (NOT OpenTURNS_SWIG_INCLUDE_DIR)
    set(OpenTURNS_SWIG_INCLUDE_DIR "${OpenTURNS_INCLUDE_DIR}/swig")
  endif ()

  # dependencies includes
  if (NOT OpenTURNS_INCLUDE_DIRS)
    set (OpenTURNS_INCLUDE_DIRS ${OpenTURNS_INCLUDE_DIR})
    list (APPEND OpenTURNS_INCLUDE_DIRS ${LIBXML2_INCLUDE_DIR})
    list (APPEND OpenTURNS_INCLUDE_DIRS ${PYTHON_INCLUDE_DIRS})
  endif ()

  # check for library directory
  if (NOT OpenTURNS_LIBRARY)
    find_library (OpenTURNS_LIBRARY
      NAMES
        OT
      HINTS
        ${OPENTURNS_DIR}
        /usr
        /usr/local
        /opt
      PATH_SUFFIXES
        lib/openturns
      DOC
        "OpenTURNS library location"
    )
  endif ()

  # find dependent libraries
  if (NOT OpenTURNS_LIBRARIES)
    set (OpenTURNS_LIBRARIES ${OpenTURNS_LIBRARY} ${LIBXML2_LIBRARIES} ${PYTHON_LIBRARIES})
    list (APPEND OpenTURNS_LIBRARIES ${LIBXML2_LIBRARIES})
    list (APPEND OpenTURNS_LIBRARIES ${PYTHON_LIBRARIES})
  endif ()

  # retrieve path to lib
  get_filename_component (OpenTURNS_LIBRARY_PATH ${OpenTURNS_LIBRARY} PATH)

  # retrieve install path
  set (OpenTURNS_INSTALL_PATH "${OpenTURNS_LIBRARY_PATH}/../..")

  # find wrappers dir
  if (NOT OpenTURNS_WRAPPER_DIR)
    find_path (OpenTURNS_WRAPPER_DIR
      NAMES
        wrapper.xml wrapper.dtd
      HINTS
        ${OPENTURNS_DIR}
        ${OpenTURNS_INSTALL_PATH}
        /usr
        /usr/local
        /opt
      PATH_SUFFIXES
        share/openturns/wrappers
      DOC
        "OpenTURNS wrappers location"
    )
  endif ()

  # set wrapper definitions
  if (NOT OpenTURNS_WRAPPER_DEFINITIONS)
    set(OpenTURNS_WRAPPER_DEFINITIONS)
    check_include_file_cxx (pthread.h HAVE_PTHREAD_H)
    if (HAVE_PTHREAD_H)
      list (APPEND OpenTURNS_WRAPPER_DEFINITIONS -DHAVE_PTHREAD_H)
    endif ()
  endif ()

  # find python module dir
  if (NOT OpenTURNS_PYTHON_MODULE_DIR)
    find_path (OpenTURNS_PYTHON_MODULE_DIR
      NAMES
        openturns.pth
      HINTS
        ${OPENTURNS_DIR}
        ${OpenTURNS_INSTALL_PATH}
        /usr
        /usr/local
        /opt
      PATH_SUFFIXES
        lib/python${PYTHON_VERSION}/site-packages
      DOC
        "OpenTURNS python module location"
    )
  endif ()


  # find module directory
  if (NOT OpenTURNS_MODULE_DIR)
    set (OpenTURNS_MODULE_DIR
      ${OpenTURNS_LIBRARY_PATH}/module
    )
  endif ()

  # set module definitions
  if (NOT OpenTURNS_MODULE_DEFINITIONS)
    set (OpenTURNS_MODULE_DEFINITIONS)

    # check for STDC_HEADERS
    check_include_file (stdlib.h HAVE_STDLIB_H)
    check_include_file (stdarg.h HAVE_STDARG_H)
    check_include_file (string.h HAVE_STRING_H)
    check_include_file (float.h HAVE_FLOAT_H)
    check_function_exists (memchr HAVE_MEMCHR)
    check_function_exists (free HAVE_FREE)
    check_include_file (ctype.h HAVE_CTYPE_H)
    if(HAVE_STDLIB_H AND HAVE_STDARG_H AND HAVE_STRING_H AND HAVE_FLOAT_H AND HAVE_MEMCHR AND HAVE_FREE AND HAVE_CTYPE_H)
      list (APPEND OpenTURNS_MODULE_DEFINITIONS -DSTDC_HEADERS_H=1)
    else ()
      list (APPEND OpenTURNS_MODULE_DEFINITIONS -DSTDC_HEADERS_H=0)
    endif ()

    # this macro checks a header and defines the corresponding macro
    macro(check_include_files_define_macro header_file)
      # get macro name from header_file
      string(TOUPPER ${header_file} macro_name)
      string(REGEX REPLACE "[/.]" "_" macro_name ${macro_name})
      set(macro_name HAVE_${macro_name})
      # check for header
      check_include_file(${header_file} ${macro_name})
      # define macro
      if(${macro_name})
        list (APPEND OpenTURNS_MODULE_DEFINITIONS -D${macro_name}=1)
      else()
        list (APPEND OpenTURNS_MODULE_DEFINITIONS -D${macro_name}=0)
      endif()
    endmacro()

    # check for some headers
    check_include_files_define_macro(sys/types.h)
    check_include_files_define_macro(sys/stat.h)
    check_include_files_define_macro(stdlib.h)
    check_include_files_define_macro(string.h)
    check_include_files_define_macro(memory.h)
    check_include_files_define_macro(strings.h)
    check_include_files_define_macro(inttypes.h)
    check_include_files_define_macro(stdint.h)
    check_include_files_define_macro(unistd.h)
    check_include_files_define_macro(dlfcn.h)
    check_include_files_define_macro(stdbool.h)
    check_include_files_define_macro(regex.h)

  endif ()

endif ()

# handle the QUIETLY and REQUIRED arguments and set OpenTURNS_FOUND to TRUE if
# all listed variables are TRUE
find_package_handle_standard_args (OpenTURNS DEFAULT_MSG
  OpenTURNS_LIBRARY
  OpenTURNS_INCLUDE_DIR
  OpenTURNS_SWIG_INCLUDE_DIR
  OpenTURNS_INCLUDE_DIRS
  OpenTURNS_LIBRARIES
  OpenTURNS_WRAPPER_DIR
  OpenTURNS_PYTHON_MODULE_DIR
  OpenTURNS_MODULE_DIR
)

mark_as_advanced (
  OpenTURNS_LIBRARY
  OpenTURNS_INCLUDE_DIR
  OpenTURNS_SWIG_INCLUDE_DIR
  OpenTURNS_INCLUDE_DIRS
  OpenTURNS_LIBRARIES
  OpenTURNS_WRAPPER_DIR
  OpenTURNS_WRAPPER_DEFINITIONS
  OpenTURNS_MODULE_DIR
  OpenTURNS_PYTHON_MODULE_DIR
  OpenTURNS_MODULE_DEFINITIONS
)


### Local Variables:
### mode: cmake
### End:
