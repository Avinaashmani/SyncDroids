FROM osrf/ros:humble-desktop-full

RUN apt-get update && apt-get install nano -y 

COPY setup.sh SyncDroid/setup/setup.sh
COPY src /SyncDroid/src
COPY config /SyncDroid/config
COPY README.md /SyncDroid/README.msd


RUN apt-get update \
    && apt-get install -y sudo \
    && echo &USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME 
ENTRYPOINT [ "/bin/bash", "/setup.bash" ]

