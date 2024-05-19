FROM osrf/ros:humble-desktop-full

RUN apt-get update && apt-get nano -y && rm -rf /var/lib/lists/*

COPY config/ /ros_config

RUN apt-get update \
    && apt-get install -y sudo \
    && echo &USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME \ 
    && rm -rf /var/lib/apt/lists/* 


COPY setup.sh /setup.sh
ENTRYPOINT [ "/bin/bash", "/setup.bash" ]

