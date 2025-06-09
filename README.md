# Turtle robot control

In the simulation, the turtle robot drives around the polygon, is controlled by the keyboard and does not crash into walls.

**Simulation**
```sh
ros2 run turtlesim turtle_teleop_key --ros-args -r /turtle1/cmd_vel:=/cmd_vel -p scale_linear:=0.2
```
