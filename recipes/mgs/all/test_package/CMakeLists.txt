cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(mgs REQUIRED base64 CONFIG)
add_executable(example example.cpp)
target_link_libraries(example mgs::base64)
set_property(TARGET example PROPERTY CXX_STANDARD 14)
