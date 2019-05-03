#!/usr/bin/env python3
import argparse
import os
import sys
import omdb


def get_rotten_tomato_rating(movie):
    """Get the Rotten Tomato rating from a specific movie"""
    for rating in movie['ratings']:
        if 'rotten tomatoes' in rating['source'].lower():
            return rating['value']


def show_results(name):
    """Print on stdout the results obtained from omdb"""
    movies = omdb.search(name)
    if not movies:
        sys.exit(f'Movie "{name}" not found')
    for movie in omdb.search(name):
        m = omdb.imdbid(movie['imdb_id'])
        rating_str = 'No rating info'
        rating = get_rotten_tomato_rating(m)
        if rating:
            rating_str = f'Rotten Tomatoes {rating}'
        print(f'{m["title"]}/{m["year"]} ➡ {rating_str}')
        print('-' * 80)


def main():
    """Configure, parse the arguments and call show_results"""
    try:
        api_key = os.environ['OMDB_API_KEY']
    except KeyError:
        sys.exit('You must set the environment variable OMDB_API_KEY')
    omdb.set_default('apikey', api_key)
    description = 'Search movies by name and print its Rotten Tomato rating'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        'name',
        help='Movie name you want to know the Rotten Tomato rating',
        type=str,
        nargs='+',
    )
    args = parser.parse_args()
    show_results(' '.join(args.name))


if __name__ == '__main__':
    main()
