#!/bin/bash


lights='python /Users/alexbrown/Zakk/HueScripts/light_control.py'

$lights --on

#n=1
#while [ $n -lt 10 ]
#do
#    $lights --random
#    echo "flash $n"
#    let n+=1
#done
#$lights --off