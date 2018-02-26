#include "ros/ros.h"
#include "nav_msgs/OccupancyGrid.h"
#include "std_msgs/Header.h"
#include "nav_msgs/MapMetaData.h"
#include <bits/stdc++.h>
#include <vector>
#include <algorithm> 
#include <iostream>

//ros::Publisher map_pub;

void mapCallback(const nav_msgs::OccupancyGrid::ConstPtr& msg) {

  std_msgs::Header header = msg->header;
  nav_msgs::MapMetaData info = msg->info;
  ROS_INFO("Got map %d %d", info.width, info.height);


  // Keep track of nodes that are free
  std::vector<int> Nodes;

  // The map data, in row-major order, starting with (0,0).  Occupancy
  // probabilities are in the range [0,100].  Unknown is -1.
  ROS_INFO_STREAM("sizeof(map data): " << sizeof(msg->data));
  ROS_INFO_STREAM("msg->data.size(): " << msg->data.size());
  //ROS_INFO_STREAM("Value: " << msg->data.front());

  // Get indexes of map data that aren't unknown
  for (unsigned int i = 0; i!= msg->data.size(); ++i) {
	//int val = msg->data[i];
	if (msg->data[i] > -1) {
		Nodes.push_back(i);
		//ROS_INFO_STREAM("index: " << i);
	}
  }
  
}


int main(int argc, char **argv){

  ros::init(argc, argv, "occ_reader");
  ros::NodeHandle n;

  //map_pub = n.advertise<nav_msgs::OccupancyGrid>("map_out",10);
  ros::Subscriber map_sub = n.subscribe("/map", 10, mapCallback);
  
  ros::spin();
  return 0;

}
