#!/usr/bin/env bash

USAGE="Usage: $0 arg1 arg2 arg3 ... argN"

lights="python /Users/alexbrown/Zakk/HueScripts/light_control.py"

if [ "$#" == "0" ]; then
    echo $USAGE
    exit 1
fi

while (( "$#" )); do
    echo; echo "Running: lights $1"
    $lights $1  &
    sleep 2; echo
    shift
done

#### ENTER CHAIN OF COMMANDS AFTER CALLING chain.py IN SHELL ####
# e.g. >> ./chain.py red blue green fire police
