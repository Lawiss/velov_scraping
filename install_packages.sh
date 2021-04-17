#!/bin/bash

arch=$(uname -a)

if [[ "$arch" == *"armv7l"* ]] 
then
    pip install --index-url=https://www.piwheels.org/simple -r requirements.txt
else
    pip install -r requirements.txt
fi
