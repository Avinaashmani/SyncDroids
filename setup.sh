#!/bin/bash 

set -e

source /opt/ros/humble/setup.bash
export ROS_DOMAIN_ID=2
echo "Provided Arguments: $@"
exec $@
