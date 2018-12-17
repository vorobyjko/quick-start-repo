#!/bin/bash

ip=$1

until timeout 1 bash -c " ping -c 1 $ip"; [[ "$?" -eq "0" ]];
  do sleep 1;
done;
echo 'connected to' "$ip"