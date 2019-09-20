set(target pygenTestLib)

configure_file(__init__.py ${target}/__init__.py COPYONLY)
set(HEADERS
    functions.h
)

set(SRC
    bindings.cpp
)

set(Boost_USE_STATIC_LIBS ON)
find_package(Python REQUIRED COMPONENTS Development)
find_package(Boost REQUIRED COMPONENTS python${Python_VERSION_MAJOR}${Python_VERSION_MINOR} numpy)

add_library(${target} SHARED ${HEADERS} ${SRC})
target_compile_definitions(${target} PUBLIC -DBOOST_PYTHON_STATIC_LIB -DBOOST_NUMPY_STATIC_LIB)
target_link_libraries(${target} PUBLIC Python::Python Boost::python${Python_VERSION_MAJOR}${Python_VERSION_MINOR} Boost::numpy)
if(TARGET Eigen3::Eigen) 
  target_link_libraries(${target} PUBLIC Eigen3::Eigen) 
else() 
  target_include_directories(${target} SYSTEM PUBLIC "${EIGEN3_INCLUDE_DIR}") 
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