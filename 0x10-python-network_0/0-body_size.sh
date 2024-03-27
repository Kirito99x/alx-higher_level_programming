#!bin/bash
#sh script that takes url send request to that url and display the size of the body response.
curl -s -w "$1" | wc -c

