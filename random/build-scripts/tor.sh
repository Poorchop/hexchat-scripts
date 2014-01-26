#!/bin/sh

cd `dirname $0`/../tor/tor-0.2.4.20/ &&
./configure CFLAGS='-O2 -march=native' CXXFLAGS='-O2 -march=native' &&
make clean &&
make -j2 &&
sudo make install
