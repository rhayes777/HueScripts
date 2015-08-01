#!/usr/bin/env bash

lights="python /Users/alexbrown/Zakk/HueScripts/light_control.py"

echo Testing... Lights off
$lights off

### 
function l {
    echo "Running ONE with $2" $
    $lights $1
    sleep 1
    echo "Running TWO with $1" $
    $lights $2
    sleep 1
}

################### ENTER COMMANDS BELOW ###################
echo Running 
l red orange
l yellow green
l turquoise blue

