# omdb_rotten_tomato_rating

Get the Rotten Tomato rating for movies

## Usage

```sh
$ docker run --rm -e OMDB_API_KEY=$OMDB_API_KEY agustinhenze/omdb-rt-rating
usage: omdb_rotten_tomato_rating.py [-h] name [name ...]

Search movies by name and print its Rotten Tomato rating

positional arguments:
  name        Movie name you want to know the Rotten Tomato rating

optional arguments:
  -h, --help  show this help message and exit
```

```sh
$ docker run --rm -e OMDB_API_KEY=$OMDB_API_KEY agustinhenze/omdb-rt-rating batman
Batman Begins/2005 ➡ Rotten Tomatoes 84%
--------------------------------------------------------------------------------
Batman v Superman: Dawn of Justice/2016 ➡ Rotten Tomatoes 28%
--------------------------------------------------------------------------------
Batman/1989 ➡ Rotten Tomatoes 71%
--------------------------------------------------------------------------------
Batman Returns/1992 ➡ Rotten Tomatoes 80%
--------------------------------------------------------------------------------
Batman Forever/1995 ➡ Rotten Tomatoes 39%
--------------------------------------------------------------------------------
Batman & Robin/1997 ➡ Rotten Tomatoes 10%
--------------------------------------------------------------------------------
The Lego Batman Movie/2017 ➡ Rotten Tomatoes 90%
--------------------------------------------------------------------------------
Batman: The Animated Series/1992–1995 ➡ No rating info
--------------------------------------------------------------------------------
Batman: Under the Red Hood/2010 ➡ Rotten Tomatoes 100%
--------------------------------------------------------------------------------
Batman: The Dark Knight Returns, Part 1/2012 ➡ Rotten Tomatoes 100%
--------------------------------------------------------------------------------
```

You can get the omdb api key from here https://omdbapi.com/apikey.aspx

## Install via pip and usage

```sh
$ pip3 install -r requirements.txt
$ python3 omdb_rotten_tomato_rating.py blade runner
Blade Runner/1982 ➡ Rotten Tomatoes 90%
--------------------------------------------------------------------------------
Blade Runner 2049/2017 ➡ Rotten Tomatoes 87%
--------------------------------------------------------------------------------
Blade Runner: Black Out 2022/2017 ➡ No rating info
--------------------------------------------------------------------------------
Dangerous Days: Making Blade Runner/2007 ➡ No rating info
--------------------------------------------------------------------------------
Blade Runner/1997 ➡ No rating info
--------------------------------------------------------------------------------
Oscar Pistorius: Blade Runner Killer/2017 ➡ No rating info
--------------------------------------------------------------------------------
On the Edge of 'Blade Runner'/2000 ➡ No rating info
--------------------------------------------------------------------------------
Blade Runner: Deleted and Alternate Scenes/2007 ➡ No rating info
--------------------------------------------------------------------------------
Blade Runner 2049: To Be Human: - Casting Blade Runner 2049/2018 ➡ No rating info
--------------------------------------------------------------------------------
Blade Runner 60: Director's Cut/2012 ➡ No rating info
--------------------------------------------------------------------------------
```

## Howto build the docker image

```sh
$ docker build -t agustinhenze/omdb-rt-rating .
```