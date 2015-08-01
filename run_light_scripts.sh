#!/usr/bin/env bash

lights="python /Users/alexbrown/Zakk/HueScripts/light_control.py"

echo Testing... Lights off
$lights off && sleep 1

### 
function l {
    for arg     # "in $@" is implied!
    do
        echo "Running lights $arg" $
        $lights $arg
        sleep 1
    done
}


################### ENTER COMMANDS BELOW ###################

echo Start script
l madness bounce     &
sleep 10
l police strobe       &

#l red orange
#l yellow green
#l turquoise blue
echo End script

