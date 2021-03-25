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

# count folders
for d in $PATH/*/ ; do
    if [ "$(/bin/ls -A $d)" ]; then
        for e in $d* ; do
            FOLDERS=$((FOLDERS+1))
        done
    fi
done

# header
for c in  $(/bin/seq 1 $NB_COLS) ; do
    header="${header}logo|name|"
    cellAlign="${cellAlign}:--:|:---|"
done

echo "|$header" > $OUTPUT
echo "|$cellAlign" >> $OUTPUT

# fetch letter folders
for d in $PATH/*/ ; do

     # remove full path and trailing slash
     letterFolder="${d%?}"
     letterFolder="${letterFolder##*/}"

     # echo "current letter folder : $letterFolder"

    # if 
    if [ "$(/bin/ls -A $d)" ]; then

        # fetch letter's subfolders
        for e in $d* ; do

            # remove full path and trailing slash
            NAME="$(/bin/basename $e)"

            # apply .md table template
            ITEM="![$NAME]($e/square-1-60.png \"$NAME\")|\`$NAME\`"

            J=$((J+1))

            LINE="$LINE|$ITEM"

            if [ "$J" -eq "$NB_COLS" ]
            then
                echo "$LINE|$ITEM|"
                echo "$LINE|$ITEM|" >> $OUTPUT
                J=0
                LINE=""
            fi

            I=$((I+1))
            
            # in case in not completed last line
            if [ "$I" -eq "$FOLDERS" -a "$J" -lt "$NB_COLS" -a "$J" -gt 0 ]
            then
                while [ "$J" -lt "$NB_COLS" ]
                do
                    LINE="$LINE|...|..."
                    J=$((J+1))
                done
                echo "$LINE|"
                echo "$LINE|" >> $OUTPUT
                LINE="...|..."
            fi
        
        done

    fi

done
