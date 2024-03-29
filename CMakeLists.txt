cmake_minimum_required(VERSION 3.12)
#-------------------------------------------------------------------------------------------
# I'm going to use vcpk in most cases for our install of 3rd party libs
# this is going to check the environment variable for CMAKE_TOOLCHAIN_FILE and this must point to where
# vcpkg.cmake is in the University this is set in your .bash_profile to
# export CMAKE_TOOLCHAIN_FILE=/public/devel/2020/vcpkg/scripts/buildsystems/vcpkg.cmake
#-------------------------------------------------------------------------------------------
if(NOT DEFINED CMAKE_TOOLCHAIN_FILE AND DEFINED ENV{CMAKE_TOOLCHAIN_FILE})
   set(CMAKE_TOOLCHAIN_FILE $ENV{CMAKE_TOOLCHAIN_FILE})
endif()
# Name of the project
project(EmbedPythonBuild)
# This is the name of the Exe change this and it will change everywhere
set(TargetName EmbedPython)
# find Qt libs first we check for Version 6
find_package(Qt6 COMPONENTS OpenGL Widgets QUIET )
if ( Qt6_FOUND )
    message("Found Qt6 Using that")
else()
    message("Found Qt5 Using that")
    find_package(Qt5 COMPONENTS OpenGL Widgets REQUIRED)
endif()
find_package(NGL CONFIG REQUIRED)
# use C++ 17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)
find_package (Python COMPONENTS Interpreter Development)


# Set the name of the executable we want to build
add_executable(${TargetName})
## as we are using python we can't use the keyword slots	
ADD_DEFINITIONS(-DQT_NO_KEYWORDS)
# Add NGL include path
include_directories(include $ENV{HOME}/NGL/include)



target_sources(${TargetName} PRIVATE ${PROJECT_SOURCE_DIR}/src/main.cpp  
			${PROJECT_SOURCE_DIR}/src/NGLScene.cpp  
			${PROJECT_SOURCE_DIR}/src/Agent.cpp  
			${PROJECT_SOURCE_DIR}/include/Agent.h  
			${PROJECT_SOURCE_DIR}/include/NGLScene.h  
)
target_link_libraries(${TargetName} PRIVATE NGL  Qt::Widgets Qt::OpenGL )
 target_link_libraries(${TargetName} PRIVATE ${PROJECT_LINK_LIBS}  Python::Python -lpthread -ldl  -lutil -lm -L/opt/homebrew/lib -lgettextpo )


add_custom_target(EmbedPythonCopyShaders ALL
    COMMAND ${CMAKE_COMMAND} -E copy_directory
    ${CMAKE_CURRENT_SOURCE_DIR}/python
    ${CMAKE_BINARY_DIR}/python
		) 
