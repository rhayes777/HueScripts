#!/bin/bash

lights=/Users/alexbrown/Zakk/HueScripts/light_script.py

n=1
while [ $n -lt 100 ]
do
    "$lights"
    echo "flash $n"
    let n+=1
done
