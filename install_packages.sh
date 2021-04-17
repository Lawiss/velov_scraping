#!/bin/bash

arch=$(uname -a)

if [[ "$arch" == *"aarch64"* ]] 
then
    pip install --index-url=https://www.piwheels.org/simple -r requirements.txt
else
    pip install -r requirements.txt
fi
