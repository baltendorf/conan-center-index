cmake_minimum_required(VERSION 2.8.12)
project(TestPackage CXX)

add_definitions(-DOPENTRACING_STATIC)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(${PROJECT_NAME} TestPackage.cpp)
target_link_libraries(${PROJECT_NAME} CONAN_PKG::opentracing-cpp)
