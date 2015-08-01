#!/bin/bash

lights='python /Users/alexbrown/Zakk/HueScripts/light_control.py'

$lights --off

n=1
while [ $n -lt 100 ]
do
    $lights --off
    echo "off $n"
    let n+=1
done
$lights --off
