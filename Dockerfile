FROM ubuntu:latest

# Update the package list and install sudo and snapd
RUN apt-get update && apt-get install -y sudo snapd

# Enable and start the snapd service
RUN systemctl enable snapd && systemctl start snapd

# Install prusa-slicer using snap
RUN sudo snap install prusa-slicer
