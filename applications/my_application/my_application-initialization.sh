#!/usr/bin/env bash

# Stop Script on Error
set -e

# For Debugging (print env. variables into a file)
printenv > /var/log/colony-vars-"$(basename "$BASH_SOURCE" .sh)".txt


# Update packages
echo "** Updating System **"
apt-get update -y

echo "** Installing Apache **"
apt-get install apache2 apache2-utils -y
systemctl enable apache2

