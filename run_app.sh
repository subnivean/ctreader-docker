#!/bin/bash

SCRIPT_PATH=$(dirname $(realpath -s $0))

docker run --rm \
  --privileged \
  -v $SCRIPT_PATH/data:/data \
  -v $SCRIPT_PATH/src:/app \
  allinone-py311 python app.py

