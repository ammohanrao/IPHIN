#!/bin/bash
#!/usr/bin/env python

NOW=$(date +"%m-%d-%Y")
FILE="iphin1_$NOW.txt"
python3 iphin5.py >$FILE
