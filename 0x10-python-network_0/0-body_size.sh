#!bin/bash
#sh script that takes url
curl -s "$1" | wc -c
