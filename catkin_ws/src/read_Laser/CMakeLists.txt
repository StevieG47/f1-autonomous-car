cmake_minimum_required(VERSION 2.8.3)
project(lidar_move)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  std_msgs
  message_generation
  geometry_msgs
  tf
)

add_message_files(
	FILES
	drive_param.msg
	drive_values.msg
    	pid_input.msg
	)

 generate_messages(
   DEPENDENCIES
   sensor_msgs#   std_msgs
 )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES race
  CATKIN_DEPENDS roscpp rospy sensor_msgs std_msgs geometry_msgs
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)



