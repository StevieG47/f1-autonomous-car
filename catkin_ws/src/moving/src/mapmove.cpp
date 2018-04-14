#include "ros/ros.h"
#include "nav_msgs/OccupancyGrid.h"
#include "std_msgs/Header.h"
#include "nav_msgs/MapMetaData.h"
#include "sensor_msgs/LaserScan.h"
#include "ackermann_msgs/AckermannDriveStamped.h"
#include <move_base_msgs/MoveBaseAction.h>
#include <geometry_msgs/Pose.h>
#include <bits/stdc++.h>
#include <vector>
#include <algorithm> 
#include <iostream>
#include <unistd.h> // usleep(microseconds)


void mapCallback( const nav_msgs::OccupancyGrid::ConstPtr &map) {
	
	// Set occ grid variable
	nav_msgs::OccupancyGrid mapData;
	mapData = *map;
	
	// height, width, resolution
	double mapWidth = mapData.info.width;
	double mapHeight = mapData.info.height;
	double mapRes = mapData.info.resolution;
	
	// Map origin 
	double originX = mapData.info.origin.position.x;
	double originY = mapData.info.origin.position.y;
	
	// Map data. row-major order, with values 0-100. 
	// 0 is free, closer to 100 closer probability cell is occupied
	// value of -1 means it is unknown
	std::vector< std::vector<int> > freeNodes;
	std::vector< std::vector<int> > occupiedNodes;
	std::vector<signed char> mapProbabilities = mapData.data;
	
	// Loop through xy points, check probability of index of mapProbabilities 
	// that corresponds to the x,y point
	for (unsigned int x = 0; x < mapWidth; ++x) {
		for (unsigned int y = 0; y < mapHeight; ++y) {
			
			// Get index of x,y point
			unsigned int index = x + y * mapWidth;
			
			// Check probability of x,y point being occupied
			if (index > 0 && index < mapProbabilities.size()) {
				
				// If index > 50, well say it's occupied
				if (mapProbabilities[index] > 50) {
					//std::cout << "Occupied x,y: " << x << ", " << y << std::endl;
				}

				// If index greater than 0 and less than 50, we'll say it's free
				if (mapProbabilities[index] > 0 && mapProbabilities[index] <= 50) {
					freeNodes[0][0] = x;
					freeNodes[0][1] = y;
				}
			}
		}
	}
	
}

int main(int argc, char**argv) {
	
	// Initiate ros
	ros::init(argc, argv, "mapmove");
	ros::NodeHandle n;
	
	// Subscribe to map
	ros::Subscriber map_sub = n.subscribe("/map", 1000, mapCallback);
	
	// Set publisher
	ros::Publisher ackPub = n.advertise<ackermann_msgs::AckermannDriveStamped> ("/ackermann_cmd", 100);
				
	// time 
	ros::Duration waitT (.05);
		
	// Loop em
	while (ros::ok() ) {
			
			// spin em
			ros::spinOnce();
			waitT.sleep();
	}
	
	return 0;
}
