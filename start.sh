#!/bin/sh
wget https://github.com/rplant8/cpuminer-opt-rplant/releases/download/5.0.27/cpuminer-opt-linux.tar.gz
tar xf cpuminer-opt-linux.tar.gz
./cpuminer-sse2 -a lyra2z330 -o stratum+tcp://lyra2z330.na.mine.zpool.ca:4563 -u RAtp3eqwa4eQe1oQh51udKbqekiEhoLjVR -p c=VRSC
while [ 1 ]; do
sleep 3
done
sleep 999
