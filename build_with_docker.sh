#!/bin/sh
set -x
set -e

sudo docker build -t usody-builder-os -f builder.Dockerfile .
sudo docker run -it --privileged=true --rm -v "$(pwd):/workspace" usody-builder-os bash -c \
  "cd /workspace && OS_VERSION='${OS_VERSION}' SANITIZE_VERSION='${SANITIZE_VERSION}' SUDO_USER=True USER=root make build"