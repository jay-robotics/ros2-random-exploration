# ros2-random-exploration

A ROS 2 (Jazzy) package that makes a TurtleBot3 wander an unknown space on its own, using only a 2D LiDAR scan and odometry — no map or SLAM needed. It drives forward, watches for obstacles ahead, and when one shows up it scans the full 360° laser sweep to find the widest open gap to turn into next.

## Demo

https://github.com/user-attachments/assets/9ef3b5af-553e-4039-9b24-0cc54c12e490

## Overview

The node runs a simple state loop:

- **Move forward** while checking a front window of laser rays for obstacles.
- **Find the best gap** by scanning the full 360° laser reading, grouping open rays into gaps, filtering out gaps too narrow to pass through, and picking the widest one (with some randomness in exactly which ray within it is targeted, so the path varies each run).
- **Rotate** toward that gap using a proportional controller, then go back to moving forward.

## Tech

ROS 2 Jazzy · Python (`rclpy`) · `sensor_msgs/LaserScan` · `nav_msgs/Odometry` · `geometry_msgs/TwistStamped` · TurtleBot3

## License

Apache-2.0
