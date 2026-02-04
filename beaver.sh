#!/bin/bash

file_name=$(zenity --file-selection --title="BEAVER - Please select the log file:")

if [ -z "$file_name" ]; then
    exit 0
fi

db_name=$(zenity --entry --title="BEAVER" --text="Please enter the database name:")
        python3 /home/odoo/src/support-tools/beaver.py $file_name $db_name
        zenity --notification --text "Jobs Done"

