#!/bin/bash
file_name=${1%.*}
echo 'compiling'
gcc -c -Wall $file_name.c

gcc $file_name.o -o $file_name
echo 'running'
./$file_name
