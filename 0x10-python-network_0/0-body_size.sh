#!bin/bash
#sh script that takes url send request to that url and display the size of the body response.
curl -sI "$1" | awk '/Content-Length/ {print $2}'
