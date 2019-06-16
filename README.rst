Pokémon Battle Revolution Announcer Soundboard
===============================================

* To use the soundboard, visit https://chfoo.github.io/pbrchase/.
* To report a mistake, use the Issues section.

Quick Start
===========

To extact the sound files:

Either

* Grab the WAV audio files (English only) from `<http://www.serebiiforums.com/showthread.php?439401-PBR-Announcer-Voice-Tracks-EXTRACTED!!!>`_ or from `Archive.org <https://archive.org/details/PokemonBattleRevolutionAnnouncerAudio>`_.

Or extract it from the disk image:

1. Install Dolphin
2. Download and compile the brsar_unpack00 utility
3. Open the disc image
4. Right click the item and select Properties, Filesystem.
5. Navigate to Partition 1, sound, pbr_sound.bsar.
6. Extract that file.
7. Run `brsar_unpack pbr_sound.bsar`

To build the sound files:

1. Install sox.
2. Organize the sound files by langauge: ``python3 reorganize_files.py``
3. ``python3 batch_convert.py``


To build the HTML file:

1. ``pip3 install jinja``
2. ``python3 generate_html.py myoutput.html``


Credits
=======

Copyright 2015,2019 Christopher Foo. Licensed under the MIT license.

Contains content from

* https://github.com/veekun/pokedex
* https://github.com/aehlke/tag-it

which may be licensed under a different license.
