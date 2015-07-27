#!/bin/bash

for i in `seq 3 5`;
do
	curl -X PUT -d "{\"on\":$1}" http://192.168.1.65/api/db447f4cbc1d2f31aaa61c1602f297/lights/$i/state
done
