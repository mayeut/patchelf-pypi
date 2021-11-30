cmake_minimum_required(VERSION 3.6)

project(PatchelfPythonDistributions)

set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_MODULE_PATH})

#-----------------------------------------------------------------------------
include(ExternalProject)

#-----------------------------------------------------------------------------
# Build from source
#-----------------------------------------------------------------------------
set(Patchelf_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/patchelf-upstream)
find_program(MAKE_EXE NAMES gmake make)
ExternalProject_add(build_patchelf
  SOURCE_DIR ${Patchelf_SOURCE_DIR}
  DOWNLOAD_COMMAND ""
  UPDATE_COMMAND ""
  PATCH_COMMAND ./bootstrap.sh
  CONFIGURE_COMMAND ./configure
  BUILD_COMMAND ${MAKE_EXE} check
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

install(PROGRAMS ${patchelf_executable} DESTINATION bin)
