#!/bin/sh

# ========================================================================
# name : files-util.sh
# description : Some commandlines to extract different path part
# ========================================================================

input="/home/vivek/work/config.ini"

# extract config.ini
file_name="${input##*/}"

# get .ini 
file_extension="${file_name##*.}"

# get config 
file="${file_name%.*}"

# print it
echo "Full input file : $input"
echo "Filename only : $file_name"
echo "File extension only: $file_extension"
echo "First part of filename only: $file"