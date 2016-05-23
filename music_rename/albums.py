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


def get_album_directories(artist_dir, config, rename_active):
    artist_dir = os.path.join('.', artist_dir)

    for album_dir in os.listdir(artist_dir):
        if not os.path.isdir(os.path.join(artist_dir, album_dir)):
            print('Skipping non-directory: ' + album_dir)
            continue

        sanitized_album = sanitize.sanitize(album_dir, config['album_maxlen'])

        if album_dir != sanitized_album:
            print(colored(album_dir + ' -> ' + sanitized_album, 'yellow'))

            if rename_active:
                os.rename(
                    os.path.join(artist_dir, album_dir), os.path.join(
                        artist_dir, sanitized_album))
                album_dir = sanitized_album
        else:
            print(album_dir)

        do_album_contents(artist_dir, album_dir, config, rename_active)

        print('')


def do_album_contents(artist_dir, album_dir, config, rename_active):
    artist_album_dir = os.path.join(artist_dir, album_dir)

    for album_item in os.listdir(artist_album_dir):
        if not os.path.isdir(os.path.join(artist_album_dir, album_item)):
            filename = os.path.splitext(album_item)[0]
            ext = os.path.splitext(album_item)[1]
            if ext in ['.flac', '.mp3', '.m4a', '.ogg']:
                sanitized_song = sanitize.sanitize(filename,
                                                   config['song_maxlen'])
                if filename != sanitized_song:
                    print(colored(album_item + ' -> ' + sanitized_song + ext,
                                  'yellow'))

                    if rename_active:
                        os.rename(
                            os.path.join(artist_album_dir, album_item),
                            os.path.join(artist_album_dir,
                                         sanitized_song + ext))
                else:
                    print(album_item)
            elif ext == '.md5':
                # Delete sum files since we're going to generate a new one.
                if rename_active:
                    os.remove(os.path.join(artist_album_dir, album_item))
            else:
                print(colored('Skipping unknown type: ' + ext, 'red'))
        else:
            sanitized_dir = sanitize.sanitize(album_item,
                                              config['extra_dir_maxlen'])

            if album_item != sanitized_dir:
                print(colored(album_item + ' -> ' + sanitized_dir, 'yellow'))

                if rename_active:
                    os.rename(album_item, sanitized_dir)
                    album_item = sanitized_dir
            else:
                print(album_item)

            do_extra_dir(artist_album_dir, album_item, config, rename_active)


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
