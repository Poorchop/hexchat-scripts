#!/bin/sh

cd `dirname $0`/../nullfs/ &&
(rm ./nul1fs || :) &&
make nul1fs &&
sudo cp ./nul1fs /usr/local/bin/
