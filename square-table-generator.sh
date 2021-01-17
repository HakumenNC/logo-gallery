#!/bin/sh

# ========================================================================
# name : square-table-generator.sh
# description : Generate the .md table for each square logos in subfolders
# ========================================================================


#### VARIABLES

# target folder path, ex : "img/devops"
# current dir : ${PWD##*/}
PATH="square/database/"

# output .md file
OUTPUT="./square-table.md"

LINE=""
NB_COLS=6
FOLDERS=0
I=0
J=0

#### MAIN

# header
echo "|logo|logo|logo|logo|logo|logo|" > $OUTPUT
echo "|:--:|:--:|:--:|:--:|:--:|:--:|" >> $OUTPUT

# count folders
for d in $PATH/* ; do
    FOLDERS=$((FOLDERS+1))
done

# body
for d in $PATH/* ; do
    
    # remove full path and trailing slash
    NAME="${d##*/}"
    NAME="${NAME%.*}"


    # apply .md table template
    ITEM="![$NAME]($d \"$NAME\")"

    J=$((J+1))

    LINE="$LINE|$ITEM"

    if [ "$J" -eq "$NB_COLS" ]
    then
        #echo "$LINE|$ITEM|"
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
        #echo "$LINE|"
        echo "$LINE|" >> $OUTPUT
        LINE="...|..."
   fi
done
