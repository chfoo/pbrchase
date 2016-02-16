Pokémon Battle Revolution Announcer Soundboard
==============================================

* To use the soundboard, visit https://chfoo.github.io/pbrchase/.
* To report a mistake, use the Issues section.

Quick Start
===========

To build the sound files:

1. Grab the WAV audio files from `<http://www.serebiiforums.com/showthread.php?439401-PBR-Announcer-Voice-Tracks-EXTRACTED!!!>`_ or from `Archive.org <https://archive.org/details/PokemonBattleRevolutionAnnouncerAudio>`_.
2. Install sox.
3. ``python3 batch_convert.py``


To build the HTML file:

1. ``pip3 install jinja``
2. If needed, edit ``generate_html.py`` for the URL prefix of the sound files.
3. ``python3 generate_html.py myoutput.html``


Credits
=======

Copyright 2015 Christopher Foo. Licensed under the MIT license.

Contains content from 

* https://github.com/veekun/pokedex
* https://github.com/aehlke/tag-it

which may be licensed under a different license.
