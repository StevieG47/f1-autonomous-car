# Install script for directory: /home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/read_Laser

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_move/msg" TYPE FILE FILES
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/read_Laser/msg/drive_param.msg"
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/read_Laser/msg/drive_values.msg"
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/read_Laser/msg/pid_input.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_move/cmake" TYPE FILE FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/build/read_Laser/catkin_generated/installspace/lidar_move-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/devel/include/lidar_move")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/devel/share/roseus/ros/lidar_move")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/devel/share/common-lisp/ros/lidar_move")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/devel/share/gennodejs/ros/lidar_move")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/devel/lib/python2.7/dist-packages/lidar_move")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/devel/lib/python2.7/dist-packages/lidar_move")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/build/read_Laser/catkin_generated/installspace/lidar_move.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_move/cmake" TYPE FILE FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/build/read_Laser/catkin_generated/installspace/lidar_move-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_move/cmake" TYPE FILE FILES
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/build/read_Laser/catkin_generated/installspace/lidar_moveConfig.cmake"
    "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/build/read_Laser/catkin_generated/installspace/lidar_moveConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lidar_move" TYPE FILE FILES "/home/steve/Documents/ROS/Docker/f1-autonomous-car/catkin_ws/src/read_Laser/package.xml")
endif()

