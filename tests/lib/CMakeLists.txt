set(target pygenTestLib)

configure_file(__init__.py ${target}/__init__.py COPYONLY)
set(HEADERS
    functions.h
)

set(SRC
    bindings.cpp
)

include_directories(${Boost_INCLUDE_DIRS})
include_directories(${PYTHON_INCLUDE_DIRS})

add_library(${target} SHARED ${HEADERS} ${SRC})
target_link_libraries(${target} ${PROJECT_NAME} ${PYTHON_LIBRARY} ${Boost_PYTHON_LIBRARIES})

if(WIN32)
    set_target_properties(${target} PROPERTIES SUFFIX ".pyd")
else()
    set_target_properties(${target} PROPERTIES PREFIX "")
endif()

install(TARGETS ${target}
    RUNTIME DESTINATION ${PYTHON_INSTALL_PATH}/${target}
)

PYTHON_INSTALL_BUILD(${target} __init__.py "${PYTHON_INSTALL_PATH}")