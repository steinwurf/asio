cmake_minimum_required(VERSION 3.10)
project(asio)

find_package(Python COMPONENTS Interpreter)

# Include common CMake settings
include("${STEINWURF_RESOLVE}/toolchains/common_settings.cmake")

# Use waf to resolve dependencies
if(NOT DEFINED STEINWURF_RESOLVE)
  message(STATUS "Resolving dependencies...")
  execute_process(
    COMMAND ${Python_EXECUTABLE} waf resolve ${STEINWURF_RESOLVE_OPTIONS}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    RESULT_VARIABLE STATUS)

  if(STATUS AND NOT STATUS EQUAL 0)
    message(FATAL_ERROR "Failed: ${STATUS}")
  endif()

  set(STEINWURF_RESOLVE "${CMAKE_CURRENT_SOURCE_DIR}/resolve_symlinks")
endif()

# Define library
add_library(asio INTERFACE)
target_compile_features(asio INTERFACE cxx_std_14)

target_compile_options(asio INTERFACE -DASIO_STANDALONE)

target_include_directories(
  asio INTERFACE "${STEINWURF_RESOLVE}/asio-source/asio/include")

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(asio INTERFACE Threads::Threads)

add_library(steinwurf::asio ALIAS asio)

# Install headers
install(
  DIRECTORY "${STEINWURF_RESOLVE}/asio-source/include"
  DESTINATION ${CMAKE_INSTALL_PREFIX}/include
  FILES_MATCHING
  PATTERN *.hpp)

# Is top level project?
if(${CMAKE_PROJECT_NAME} STREQUAL ${PROJECT_NAME})
  # Build executables
  #add test
  enable_testing()
  add_executable(hello_asio examples/hello_asio.cpp)
  target_link_libraries(hello_asio asio)
  add_test(hello_asio  hello_asio)
endif()
