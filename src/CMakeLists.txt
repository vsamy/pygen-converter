set(HEADERS
    ../include/converters.h
)

if(NOT ${HEADER_ONLY})
    configure_file(__init__.py pygenTest/__init__.py COPYONLY)
    set(HEADERS_TEST
        ../include/functions.h
        ../include/functions.inl
    )
    set(SRC
        bindings.cpp
    )

    include_directories(${Boost_INCLUDE_DIRS})
    include_directories(${PYTHON_INCLUDE_DIRS})

    add_library(pygenTest SHARED ${HEADERS} ${HEADERS_TEST} ${SRC})
    target_link_libraries(pygenTest ${PYTHON_LIBRARY} ${Boost_PYTHON_LIBRARIES})

    if(WIN32)
        set_target_properties(pygenTest PROPERTIES SUFFIX ".pyd")
    else()
        set_target_properties(pygenTest PROPERTIES PREFIX "")
    endif()

    install(TARGETS pygenTest
        RUNTIME DESTINATION ${PYTHON_INSTALL_PATH}/pygenTest
    )

    PYTHON_INSTALL_BUILD(pygenTest __init__.py "${PYTHON_INSTALL_PATH}")
endif()

install(FILES ${HEADERS} DESTINATION ${INCLUDE_INSTALL_DESTINATION})