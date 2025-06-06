cmake_minimum_required(VERSION 3.15)

project(PatchelfPythonDistributions)

option(RUN_PATCHELF_TEST "Run patchelf test suite" OFF)

set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_MODULE_PATH})

#-----------------------------------------------------------------------------
include(ExternalProject)

#-----------------------------------------------------------------------------
# Build from source
#-----------------------------------------------------------------------------
set(Patchelf_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/patchelf-upstream)
find_program(MAKE_EXE NAMES gmake make)

if(RUN_PATCHELF_TEST)
  set(PATCHELF_BUILD_COMMAND "${MAKE_EXE}" check)
else()
  set(PATCHELF_BUILD_COMMAND "${MAKE_EXE}")
endif()

ExternalProject_add(build_patchelf
  SOURCE_DIR ${Patchelf_SOURCE_DIR}
  DOWNLOAD_COMMAND ""
  UPDATE_COMMAND ""
  PATCH_COMMAND ./bootstrap.sh
  CONFIGURE_COMMAND ./configure
  BUILD_COMMAND ${PATCHELF_BUILD_COMMAND}
  BUILD_IN_SOURCE 1
  INSTALL_COMMAND ""
)
set(patchelf_executable ${Patchelf_SOURCE_DIR}/src/patchelf${CMAKE_EXECUTABLE_SUFFIX})

find_program(STRIP_EXECUTABLE strip)
if(STRIP_EXECUTABLE)
  add_custom_target(strip_patchelf_executable ALL
    COMMAND ${STRIP_EXECUTABLE} ${patchelf_executable}
    WORKING_DIRECTORY ${Patchelf_SOURCE_DIR}
    COMMENT "Stripping patchelf executable"
    )
  add_dependencies(strip_patchelf_executable build_patchelf)
endif()

install(PROGRAMS "${patchelf_executable}" COMPONENT python DESTINATION "${SKBUILD_SCRIPTS_DIR}")
