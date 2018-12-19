#!/bin/bash

ip=$1

until timeout 1 bash -c "nc -vz $ip 22"; [[ "$?" -eq "0" ]];
  do sleep 1;
done;

echo "$ip is online"


