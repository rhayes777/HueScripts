#!/bin/bash

[[ $1 == on ]] && isOn=true || isOn=false

for i in `seq 3 5`;
do
	json='{"on":'$isOn'}' 
	echo $json
	curl -X PUT -d $json  http://192.168.1.65/api/db447f4cbc1d2f31aaa61c1602f297/lights/$i/state
done
