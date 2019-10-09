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
