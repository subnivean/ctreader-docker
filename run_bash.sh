#!/bin/bash

SCRIPT_PATH=$(dirname $(realpath -s $0))

docker run --rm -it \
  --privileged \
  -v $SCRIPT_PATH/data:/data \
  -v $SCRIPT_PATH/src:/app \
  -v $SCRIPT_PATH/ipython:/root/.ipython \
  allinone-py311 /bin/bash --rcfile /bashrc

