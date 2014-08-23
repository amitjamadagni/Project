#!/bin/bash

WORKINGDIR=/home/prateek/Downloads/

cd $WORKINGDIR
mkdir -p used

for file in *.txt; do
if [ $file == "*.txt" ]; then
break
fi

chmod +x $file
export DISPLAY=:0.0
/usr/bin/gnome-terminal -x bash -c "./$file;bash"
mv "$file" used
done;
