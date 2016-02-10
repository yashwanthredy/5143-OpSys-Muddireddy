#!/bin/bash
#changing date format yyyy/mm/dd
current_date=`date +%F`
#read file name from arguments
file=$1
#creating new file
echo "" > $current_date"_"$file
