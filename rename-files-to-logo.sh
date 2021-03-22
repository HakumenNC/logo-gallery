#!/bin/bash -vx


# # extract config.ini
# file_name="${input##*/}"
# # get .ini 
# file_extension="${file_name##*.}"
# # get config 
# file="${file_name%.*}"

# ========================================================================
# name : md-table-generator.sh
# description : Generate the .md table for each subfolders on $PATH
# ========================================================================


#### VARIABLES

# target folder path, ex : "img/devops"
# current dir : ${PWD##*/}
PATH="./img"

# output .md file
OUTPUT="./table.md"

LINE=""
NB_COLS=3
FOLDERS=0
I=0
J=0

#### MAIN

# fetch letter folders
for d in $PATH/*/ ; do

     # remove full path and trailing slash
     letterFolder="${d%?}"
     letterFolder="${letterFolder##*/}"

     echo "current letter folder : $letterFolder"

    # fetch letter's subfolders
     for e in $d* ; do

        for f in $e/* ; do
            echo $f 
            /bin/mv $f "$e/logo-1-40.png"
        done

     done

done
