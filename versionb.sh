#!/bin/bash
#changing date format
current_date=`date +%F`
#reads in file name using arguments
fullname=$1
#gets the base name of path with extension
filename=$(basename "$fullname")
#gets the name of file without extension
file=${fullname%.*}
#gets the type of extension
extension=${fullname##*.}
#gives the argument format as filename_date_extension
echo  > $file"_"$current_date"."$extension

