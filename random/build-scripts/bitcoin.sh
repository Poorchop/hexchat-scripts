#!/bin/sh

cd `dirname $0`/../bitcoin/ &&
git clean -xfd &&
git reset --hard origin/master &&
git merge theuni/qt5-build &&
./autogen.sh &&
./configure --with-qt=qt5 --disable-tests &&
make -j2
