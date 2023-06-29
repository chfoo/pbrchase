#!/bin/sh
set -e

python3 generate_html.py --sound-file-prefix "https://meme.nyc3.cdn.digitaloceanspaces.com/pbrchase/sounds/" out.html
./minify.sh out.html > out.min.html
