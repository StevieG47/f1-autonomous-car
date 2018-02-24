## Start car in gazebo with hector slam
```
roslaunch f1 f1-Slam.launch 
```

## Start planner (need teb local planner) 
```
roslaunch teb_local_planner_tutorials robot_carlike_in_stage.launch
```

## Convert twist messages to ackermann
```
rosrun Twist2Ack twist2ack.py 
```
