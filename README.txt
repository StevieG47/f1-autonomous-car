## Start car in gazebo with hector slam
```
roslaunch f1 f1-Slam.launch 
```

## Start planner (need teb local planner) 
```
roslaunch teb_local_planner_tutorials robot_carlike_in_stage.launch
```

- Use 2D Nav Goal in RViz to move the car

## Read occupancy grid
```
rosrun read_map readOccMap
```
