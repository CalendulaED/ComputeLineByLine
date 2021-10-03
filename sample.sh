#!/bin/bash

buggy_line=$(python3 iterationlist.py 2>&1)                                                                                                                    
# echo $buggy_line

for number in $buggy_line
do
    #perform the pycoconut for each buggy line
    echo $number 
done