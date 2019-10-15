# MIT License

# Copyright (c) 2019 Vincent SAMY

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

CMAKE_MINIMUM_REQUIRED(VERSION 3.12.4)

include(cmake/base.cmake)
include(cmake/msvc-specific.cmake)

set(PROJECT_NAME pygen)
set(PROJECT_DESCRIPTION "This is an header only library that provides list to eigen and numpy to eigen converters for boost python.")
set(PROJECT_URL https://github.com/vsamy/pygen-converter.git)
set(INSTALL_GENERATED_HEADERS OFF CACHE BOOL "Generate and install standard headers")

setup_project()
set(CMAKE_CXX_STANDARD 17)

option(BUILD_TESTING "Build unit tests." ON)
option(BUILD_TEST_STATIC_BOOST "Build unit tests with static boost libraries" OFF)

if(MSVC)
    set(CMAKE_MSVCIDE_RUN_PATH "\$(SolutionDir)/src/\$(Configuration)")
endif(MSVC)

add_project_dependency(Eigen3 REQUIRED)
add_library(${PROJECT_NAME} INTERFACE)
target_include_directories(${PROJECT_NAME} INTERFACE
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include/${PROJECT_NAME}>
)
install(TARGETS ${PROJECT_NAME}
    EXPORT ${TARGETS_EXPORT_NAME}
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    INCLUDES DESTINATION ${INCLUDE_INSTALL_DIR}
)
install(FILES "include/converters.h" DESTINATION ${INCLUDE_INSTALL_DESTINATION})

if(${BUILD_TESTING})
    add_subdirectory(tests)
endif()

setup_project_finalize()
setup_project_package_finalize()
