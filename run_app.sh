#!/bin/bash

SCRIPT_PATH=$(dirname $(realpath -s $0))

docker run --rm \
  --privileged \
  -v $SCRIPT_PATH/data:/appdata \
  -v $SCRIPT_PATH/src:/app \
  ctreader

