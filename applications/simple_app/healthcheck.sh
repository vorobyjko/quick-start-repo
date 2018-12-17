#!/bin/bash

ip=$1
nc -v -z -w 3 $ip 22 &> /dev/null && echo "Online" || echo "Offline"

