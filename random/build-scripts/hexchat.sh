#!/bin/sh

cd `dirname $0`/../hexchat/ &&
sh autogen.sh &&
./configure --disable-checksum --disable-doat --disable-fishlim --enable-spell=none --enable-python=python3 CFLAGS=-march=native CXXFLAGS=-march=native &&
make clean &&
make -j2 &&
sudo make install
