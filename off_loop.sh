#!/bin/bash

source path_finder.py

$lights --off

n=1
while [ $n -lt 100 ]
do
    $lights --off
    echo "off $n"
    let n+=1
done
$lights --off
