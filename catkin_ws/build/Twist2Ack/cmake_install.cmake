# Install script for directory: /home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/Twist2Ack

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/build/Twist2Ack/catkin_generated/installspace/Twist2Ack.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/Twist2Ack/cmake" TYPE FILE FILES
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/build/Twist2Ack/catkin_generated/installspace/Twist2AckConfig.cmake"
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/build/Twist2Ack/catkin_generated/installspace/Twist2AckConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/Twist2Ack" TYPE FILE FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/Twist2Ack/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/Twist2Ack" TYPE DIRECTORY FILES
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/Twist2Ack/launch"
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/Twist2Ack/cfg"
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/Twist2Ack/maps"
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/Twist2Ack/stage"
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/Twist2Ack/scripts"
    REGEX "/\\.svn$" EXCLUDE)
endif()

