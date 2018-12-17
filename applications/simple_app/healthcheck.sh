#!/bin/bash

ip=$1
nc -v -z -w 3 122.122.111.111 22 &> /dev/null && echo "Online" || echo "Offline"

