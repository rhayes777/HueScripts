#!/bin/bash
source path_finder.py


$lights --on

n=1
while [ $n -lt 100 ]
do
    $lights --random
    echo "flash $n"
    let n+=1
done
$lights --off
