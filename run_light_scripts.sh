#!/usr/bin/env bash

lights="python /Users/alexbrown/Zakk/HueScripts/light_control.py"

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
l madness bounce      &
sleep 5
l police strobe       &

#l red orange
#l yellow green
#l turquoise blue
echo End script

