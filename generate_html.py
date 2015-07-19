import argparse
import csv
import json
import re

from jinja2 import Environment, FileSystemLoader


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('output_filename', type=argparse.FileType('w'))
    args = arg_parser.parse_args()
    output_file = args.output_filename

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=True,
        extensions=['jinja2.ext.autoescape'],
    )
    template = env.get_template('index.html')

    pokedex_map = new_pokedex_map()
    track_infos = new_track_infos()

    output_file.write(
        template.render(
            track_infos=track_infos,
            pokedex_map=pokedex_map,
            sound_file_prefix='sounds/',
            re=re,
            int=int,
            json=json,
        ))
    output_file.close()


def new_pokedex_map():
    pokedex_map = {}

    with open('metadata/veekun_pokedex/pokemon.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                pokemon_number = int(row[0])
            except ValueError:
                pass
            else:
                name = re.sub(r'-altered|-land|-plant|-normal', '', row[1])
                pokedex_map[pokemon_number] = name

    return pokedex_map


def new_track_infos():
    track_infos = []
    pokedex_map = new_pokedex_map()
    pokemon_subtrack_map = {
        1: '˧',
        2: '˥',
        4: '˧˥',
        5: '˩',
        3: 'is sent out'
    }

    with open('metadata/tracks.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            slug = row[0]
            label = row[1] or None

            if slug.startswith('pk'):
                pokemon_number = int(slug[2:5])
                subtrack = int(slug[6])
                label = '{} {}'.format(pokedex_map[pokemon_number].title(),
                                       pokemon_subtrack_map[subtrack])

            track_infos.append((slug, label))

    return track_infos


if __name__ == '__main__':
    main()
