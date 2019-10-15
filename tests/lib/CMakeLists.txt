set(target pygenTestLib)

configure_file(__init__.py ${target}/__init__.py COPYONLY)
set(HEADERS
    functions.h
)

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

set(SRC
    bindings.cpp
)

find_package(Python REQUIRED COMPONENTS Development)

if(${BUILD_TEST_STATIC_BOOST})
    set(Boost_USE_STATIC_LIBS ON)
    set(BUILD_SHARED_LIBS OFF)
    set(BOOST_DEFS "")
    set(BUILD_TYPE STATIC)
else()
    set(Boost_USE_STATIC_LIBS OFF)
    set(BUILD_SHARED_LIBS ON)
    set(BOOST_DEFS Boost::dynamic_linking)
    set(BUILD_TYPE SHARED)
endif()
set(Boost_USE_STATIC_RUNTIME OFF)
find_package(Boost REQUIRED COMPONENTS python numpy)

add_library(${target} ${BUILD_TYPE} ${HEADERS} ${SRC})
target_link_libraries(${target} PUBLIC Python::Python Boost::python Boost::numpy Boost::disable_autolinking ${BOOST_DEFS})
target_include_directories(${target} SYSTEM PUBLIC "${EIGEN3_INCLUDE_DIR}")
if (MSVC)
    target_compile_options(${target} PRIVATE "/bigobj")
endif()

if(WIN32)
    set_target_properties(${target} PROPERTIES SUFFIX ".pyd")
else()
    set_target_properties(${target} PROPERTIES PREFIX "")
endif()

install(TARGETS ${target}
    RUNTIME DESTINATION ${PYTHON_INSTALL_PATH}/${target}
)

install(FILES __init__.py DESTINATION "${PYTHON_INSTALL_PATH}/__init__.py")