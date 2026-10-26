# ros2-random-exploration

A ROS 2 (Jazzy) package that makes a TurtleBot3 wander an unknown space on its own, using only a 2D LiDAR scan and odometry — no map or SLAM needed. It drives forward, watches for obstacles ahead, and when one shows up it scans the full 360° laser sweep to find the widest open gap to turn into next.

## Demo

https://github.com/user-attachments/assets/9ef3b5af-553e-4039-9b24-0cc54c12e490

## My DIY TurtleBot

<p align="center">
  <img width="70%" alt="front" src="https://github.com/user-attachments/assets/af74a811-5fc8-496f-8e4e-a2a0e28bcad0" />
  <img width="70%" alt="side" src="https://github.com/user-attachments/assets/b89b84fe-370c-4311-8541-b0b16f54ac22" />
  <img width="70%" alt="side2" src="https://github.com/user-attachments/assets/9694ad78-e866-4807-b734-111e5fe8ed54" />
  <img width="70%" alt="back" src="https://github.com/user-attachments/assets/4f439928-50c0-4767-a224-44b347462360" />
  <img width="70%" alt="above" src="https://github.com/user-attachments/assets/d60ee4f6-c0de-446b-9f55-3a549678e082" />
</p>

## Overview

The node runs a simple state loop:

- **Move forward** while checking a front window of laser rays for obstacles.
- **Find the best gap** by scanning the full 360° laser reading, grouping open rays into gaps, filtering out gaps too narrow to pass through, and picking the widest one (with some randomness in exactly which ray within it is targeted, so the path varies each run).
- **Rotate** toward that gap using a proportional controller, then go back to moving forward.

## Tech

ROS 2 Jazzy · Python (`rclpy`) · `sensor_msgs/LaserScan` · `nav_msgs/Odometry` · `geometry_msgs/TwistStamped` · TurtleBot3

## License

Apache-2.0
