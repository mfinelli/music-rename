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

def get_album_directories(directory, config, rename_active):
    for dirname in os.listdir(os.path.join('.', directory)):
        if not os.path.isdir(os.path.join('.', directory, dirname)):
            print('Skipping non-directory: ' + dirname)
            continue

        sanitized_album = sanitize.sanitize(dirname, config['album_maxlen'])

        if dirname != sanitized_album:
            print(colored(dirname + ' -> ' + sanitized_album, 'yellow'))

            if rename_active:
                os.rename(dirname, sanitized_album)
                dirname = sanitized_album
        else:
            print(dirname)

        print('')
