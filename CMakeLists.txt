cmake_minimum_required(VERSION 3.10.0)

project(helloworldqtconan)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(Qt5 COMPONENTS Core Gui Widgets REQUIRED)

qt5_wrap_cpp(MOC_SOURCES window.h)

add_executable(helloworldqtconan
	hello.cpp
	window.cpp
	${MOC_SOURCES}
)

unset(MOC_SOURCES)

set_target_properties(helloworldqtconan
	PROPERTIES
	RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)

target_link_libraries(helloworldqtconan Qt5::Core Qt5::Gui Qt5::Widgets)
