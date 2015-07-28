#!/bin/bash

lights='python /Users/alexbrown/Zakk/HueScripts/light_script.py'

echo "Let the madness begin!"

n=1
while [ $n -lt 100 ]
do
    $lights --random
    echo "flash $n"
    let n+=1
done
