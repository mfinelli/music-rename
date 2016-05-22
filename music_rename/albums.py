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
                os.rename(os.path.join(directory, dirname), os.path.join(directory, sanitized_album))
                dirname = sanitized_album
        else:
            print(dirname)

        do_album_contents(
            os.path.join('.', directory), dirname, config, rename_active)

        print('')


def do_album_contents(full_dirname, directory, config, rename_active):
    for dirname in os.listdir(os.path.join(full_dirname, directory)):
        if not os.path.isdir(os.path.join(full_dirname, directory, dirname)):
            filename = os.path.splitext(dirname)[0]
            ext = os.path.splitext(dirname)[1]
            if ext in ['.flac', '.mp3', '.m4a', '.ogg']:
                sanitized_song = sanitize.sanitize(filename,
                                                   config['song_maxlen'])
                if filename != sanitized_song:
                    print(colored(dirname + ' -> ' + sanitized_song + ext,
                                  'yellow'))

                    if rename_active:
                        os.rename(dirname, sanitized_song + ext)
                else:
                    print(dirname)
            elif ext == '.md5':
                # Delete sum files since we're going to generate a new one.
                if rename_active:
                    os.remove(dirname)
            else:
                print(colored('Skipping unknown type: ' + ext, 'red'))
        else:
            sanitized_dir = sanitize.sanitize(dirname, config['extra_dir_maxlen'])

            if dirname != sanitized_dir:
                print(colored(dirname + ' -> ' + sanitized_dir, 'yellow'))

                if rename_active:
                    os.rename(dirname, sanitized_dir)
                    dirname = sanitized_dir
            else:
                print(dirname)

            do_extra_dir(
                os.path.join('.', full_dirname, directory), dirname, config, rename_active)


def do_extra_dir(full_dirname, directory, config, rename_active):
    for dirname in os.listdir(os.path.join(full_dirname, directory)):
        if os.path.isdir(os.path.join(full_dirname, directory, dirname)):
            print(colored('No support for directories this deep: ' + dirname,
                          'red'))
        else:
            filename = os.path.splitext(dirname)[0]
            ext = os.path.splitext(dirname)[1]
            sanitized_item = sanitize.sanitize(filename,
                                               config['extra_maxlen'])

            if filename != sanitized_item:
                print(colored(dirname + ' -> ' + sanitized_item + ext,
                              'yellow'))

                if rename_active:
                    os.rename(dirname, sanitized_item + ext)
            else:
                print(dirname)
