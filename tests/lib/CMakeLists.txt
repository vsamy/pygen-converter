set(target pygenTestLib)

configure_file(__init__.py ${target}/__init__.py COPYONLY)
set(HEADERS
    functions.h
)

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