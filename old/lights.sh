#!/bin/bash

[[ $1 == on ]] && isOn=true || isOn=false

function sendCommand(){
	curl -X PUT -d $2 http://192.168.1.65/api/db447f4cbc1d2f31aaa61c1602f297/lights/$1/state
}

# lightNumber, bri, sat, hue
function setColour(){
	json='{"on":true,"bri":'$2',"sat",'$3',"hue":'$4'}'
	sendCommand $1 $json
}

for i in `seq 3 5`;
do
	json='{"on":'$isOn'}' 
	echo $json
	sendCommand $i $json
done

