import argparse
import csv
import json
import re
import sys
import collections

from jinja2 import Environment, FileSystemLoader

TrackInfo = collections.namedtuple('TrackInfoType',
    ['slug', 'labels'])

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('output_filename', type=argparse.FileType('w'))
    arg_parser.add_argument('--sound-file-prefix', default='sounds/')
    args = arg_parser.parse_args()
    output_file = args.output_filename

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=True,
        extensions=['jinja2.ext.autoescape'],
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template('index.html')

    pokedex_map = new_pokedex_map()
    track_infos = new_track_infos()

    output_file.write(
        template.render(
            track_infos=track_infos,
            pokedex_map=pokedex_map,
            sound_file_prefix=args.sound_file_prefix,
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

        # skip header
        next(reader)

        for row in reader:
            slug = row[0]
            label = row[1] or None
            label_de = row[2] or None
            label_es = row[3] or None
            label_fr = row[4] or None
            label_it = row[5] or None

            if slug.startswith('pk'):
                pokemon_number = int(slug[2:5])
                subtrack = int(slug[6])
                label = '{} {}'.format(pokedex_map[pokemon_number].title(),
                                       pokemon_subtrack_map[subtrack])

            if label:
                track_infos.append(TrackInfo(
                    slug, {
                        'en': label,
                        'de': label_de,
                        'es': label_es,
                        'fr': label_fr,
                        'it': label_it,
                    }))
            else:
                print('Ignored', slug, file=sys.stderr)

    return track_infos


if __name__ == '__main__':
    main()
