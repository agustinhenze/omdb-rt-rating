from python:3.7-alpine

add requirements.txt ./

add omdb_rotten_tomato_rating.py /usr/local/bin

run chmod +x /usr/local/bin/omdb_rotten_tomato_rating.py

run pip3 install -r requirements.txt

entrypoint ["/usr/local/bin/omdb_rotten_tomato_rating.py"]

cmd ["--help"]
