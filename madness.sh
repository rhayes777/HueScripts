#!/bin/bash

lights='python /Users/alexbrown/Zakk/HueScripts/light_script.py'

echo "Let the madness begin!"
$lights --on

n=1
while [ $n -lt 10 ]
do
    $lights --random
    echo "flash $n"
    let n+=1
done
