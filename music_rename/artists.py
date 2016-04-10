# music-rename: rename music files after ripping
# Copyright (C) 2016 Mario Finelli
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from termcolor import colored
from music_rename import sanitize


def get_artist_directories(config, rename_active):
    for dirname in os.listdir('.'):
        if not os.path.isdir(dirname):
            print('Skipping non-directory: ' + dirname)
            continue

        sanitized_artist = sanitize.sanitize(dirname, config['artist_maxlen'])

        if dirname != sanitized_artist:
            t = colored(dirname + ' -> ' + sanitized_artist, 'yellow')
            print(t)
        else:
            print(dirname)
