#!/bin/sh

NOW=$(date +"%m-%d-%Y")
FILE="iphin1_$NOW.txt"
python3 iphin1.py >$FILE

echo "Completed FILE 1"

NOW=$(date +"%m-%d-%Y")
FILE="iphin2_$NOW.txt"
python3 iphin2.py >$FILE

echo "Completed FILE 1"

NOW=$(date +"%m-%d-%Y")
FILE="iphin1_$NOW.txt"
FILE1="iphin1_results_$NOW.txt"
gawk -F'\t' '{printf("%s\n",$3)}' $FILE | grep -vw "\[\]" >$FILE1

NOW=$(date +"%m-%d-%Y")
FILE="iphin2_$NOW.txt"
FILE1="iphin2_results_$NOW.txt"
gawk -F'\t' '{printf("%s\n",$3)}' $FILE | grep -vw "\[\]" >$FILE1
