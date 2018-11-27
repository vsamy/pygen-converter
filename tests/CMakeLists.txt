include(../cmake/eigen.cmake)
include(../cmake/boost.cmake)
include(../cmake/python.cmake)
include(../cmake/msvc-specific.cmake)

if(NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wno-sign-conversion -std=c++0x -pedantic")
endif()

findpython()
if(NOT PYTHON_INSTALL_PATH)
    set(PYTHON_INSTALL_PATH ${PYTHON_SITELIB})
endif()

set(BOOST_REQUIRED 1.63)
set(BOOST_COMPONENTS numpy)
set(Eigen_REQUIRED "eigen3 >= 3.3")
search_for_boost()
search_for_eigen()

add_subdirectory(lib)
add_test(NAME python-tests
    COMMAND ${PYTHON_EXECUTABLE} -m pyTests # Or just COMMAND pytest
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)