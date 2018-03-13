cmake_minimum_required(VERSION 2.8.3)
project(f1-vision)


find_package(OpenCV)

find_package(catkin REQUIRED COMPONENTS message_generation rospy std_msgs cv_bridge sensor_msgs)
catkin_package()

