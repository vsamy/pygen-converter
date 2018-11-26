CMAKE_MINIMUM_REQUIRED(VERSION 3.0.2)
include(cmake/base.cmake)
include(cmake/eigen.cmake)
include(cmake/boost.cmake)
include(cmake/python.cmake)
include(cmake/msvc-specific.cmake)

set(PROJECT_NAME pygen)
set(PROJECT_DESCRIPTION "This is an header only library that provides list to eigen and numpy to eigen converters for boost python.")
set(PROJECT_URL https://github.com/vsamy/pygen-converter.git)

project(${PROJECT_NAME} CXX)

setup_project()

option(HEADER_ONLY "Install header-only lib." OFF)
option(DISABLE_TESTS "Disable unit tests." OFF)

if(NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wno-sign-conversion -std=c++0x -pedantic")
endif()

if(MSVC)
    set(CMAKE_MSVCIDE_RUN_PATH "\$(SolutionDir)/src/\$(Configuration)")
    add_compile_options("/bigobj")
endif(MSVC)

findpython()
if(NOT PYTHON_INSTALL_PATH)
    set(PYTHON_INSTALL_PATH ${PYTHON_SITELIB})
endif()

set(BOOST_REQUIRED 1.63)
set(BOOST_COMPONENTS numpy)
set(Eigen_REQUIRED "eigen3 >= 3.3")
search_for_boost()
search_for_eigen()

add_subdirectory(src)

if(NOT ${DISABLE_TESTS})
    add_subdirectory(tests)
endif()

setup_project_finalize()