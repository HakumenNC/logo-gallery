#!/bin/sh

# ========================================================================
# name : md-table-generator.sh
# description : Generate the .md table for each subfolders on $PATH
# ========================================================================


#### VARIABLES

# target folder path, ex : "img/devops"
# current dir : ${PWD##*/}
PATH="img/devops"

# output .md file
OUTPUT="./table.md"

LINE=""
FOLDERS=0
I=0
J=0

#### MAIN

# header
echo "|logo|name|logo|name|logo|name|" > $OUTPUT
echo "|:--:|:---|:--:|:---|:--:|:---|" >> $OUTPUT

# count folders
for d in $PATH/*/ ; do
    FOLDERS=$((FOLDERS+1))
done

# body
for d in $PATH/*/ ; do
    
    # remove full path and trailing slash
    NAME="${d%?}"
    NAME="${NAME##*/}"

    # apply .md table template
    ITEM="![$NAME]($PATH/$NAME/$NAME.png \"$NAME\")|\`$NAME\`"

    J=$((J+1))

    LINE="$LINE|$ITEM"

    if [ "$J" -eq 3 ]
    then
        echo "$LINE|$ITEM|"
        echo "$LINE|$ITEM|" >> $OUTPUT
        J=0
        LINE=""
    fi

    I=$((I+1))
    
    # in case in not completed last line
    if [ "$I" -eq "$FOLDERS" -a "$J" -lt 3 -a "$J" -gt 0 ]
    then
        while [ "$J" -lt 3 ]
        do
            LINE="$LINE|...|..."
            J=$((J+1))
        done
        echo "$LINE|"
        echo "$LINE|" >> $OUTPUT
        LINE="...|..."
   fi
done