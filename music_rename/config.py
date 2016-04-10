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

import configparser
import os
from termcolor import colored

CONFIG_FILENAME = '.music-rename.ini'

DEFAULT_ARTIST_MAXLEN = 32
DEFAULT_ALBUM_MAXLEN = 29
DEFAULT_EXTRA_DIR_MAXLEN = 13
DEFAULT_EXTRA_MAXLEN = 25
DEFAULT_SONG_MAXLEN = 38


def ask_user_config():
    config = read_default_configuration()

    artist_maxlen = prompt_user_config_option(
        'Enforce maximum length of artist folders', DEFAULT_ARTIST_MAXLEN,
        config.get('artist_maxlen')).strip()
    album_maxlen = prompt_user_config_option(
        'Enforce maximum length of album folders', DEFAULT_ALBUM_MAXLEN,
        config.get('album_maxlen')).strip()
    extra_dir_maxlen = prompt_user_config_option(
        'Enforce maximum length of directories inside an album folders',
        DEFAULT_EXTRA_DIR_MAXLEN, config.get('extra_dir_maxlen')).strip()
    extra_maxlen = prompt_user_config_option(
        'Enforce maximum length of file in directories inside album folders',
        DEFAULT_EXTRA_MAXLEN, config.get('extra_maxlen')).strip()
    song_maxlen = prompt_user_config_option(
        'Enforce maximum length of song filenames', DEFAULT_SONG_MAXLEN,
        config.get('song_maxlen')).strip()

    new_config = configparser.ConfigParser()
    new_config['DEFAULT'] = {}

    if artist_maxlen is not "":
        new_config['DEFAULT']['artist_maxlen'] = artist_maxlen

    if album_maxlen is not "":
        new_config['DEFAULT']['album_maxlen'] = album_maxlen

    if extra_dir_maxlen is not "":
        new_config['DEFAULT']['extra_dir_maxlen'] = extra_dir_maxlen

    if extra_maxlen is not "":
        new_config['DEFAULT']['extra_maxlen'] = extra_maxlen

    if song_maxlen is not "":
        new_config['DEFAULT']['song_maxlen'] = song_maxlen

    write_configuration_file(new_config)


def read_default_configuration():
    config = configparser.ConfigParser()
    config.read(get_config_filepath())
    return config['DEFAULT']


def get_config_filepath():
    return os.path.join(os.path.expanduser('~'), CONFIG_FILENAME)


def write_configuration_file(config):
    with open(get_config_filepath(), 'w') as config_file:
        config.write(config_file)


def prompt_user_config_option(prompt, default, current):
    print(colored(prompt, 'blue', attrs=['bold']))
    return input('(default: ' + str(default) + '; current: ' + str(current) +
                 ') -> ')
