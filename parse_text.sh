#!/bin/bash

# Accept the URL and depth as arguments
url=$1
depth=$2

# Use wget to download the HTML of the website
wget -r -l$depth -k -E -p -nc -nd $url

# Use grep to search for all <p> tags and print their contents
grep -o '<p>.*</p>' $(find . -name "*.html") > output.txt

# Remove the downloaded HTML files
rm -rf $(find . -name "*.html") robots.txt
