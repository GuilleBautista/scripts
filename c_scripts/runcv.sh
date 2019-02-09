#!/bin/bash
file_name=${1%.*}
echo $file_name
gcc -c -Wall $file_name.c

gcc $file_name.o -o $file_name
rm $file_name.o

./$file_name
rm $file_name
