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
import argparse
import sys

from termcolor import colored
from colorama import init
init()

import music_rename
from music_rename import artists
from music_rename import config

MAIN_DESCRIPTION = """Use music-rename to organize and rename music files
    after ripping them."""

EPILOG = """music-rename:  Copyright (C) 2016 Mario Finelli.
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions. For details see the copy of the GNU
    General Public License that you should have received along with
    this program. (If not, see <http://www.gnu.org/licenses/>)"""


def main():
    parser = argparse.ArgumentParser(description=MAIN_DESCRIPTION,
                                     epilog=EPILOG)
    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version='%(prog)s ' + music_rename.__version__)
    parser.add_argument(
        '-d',
        '--directory',
        help='Work from a given directory. Otherwise operates on the ' \
                'current working directory.')
    parser.add_argument('--dry-run',
                        action='store_false',
                        dest='rename_active',
                        help='Do not actually rename/move files and folders.')
    parser.add_argument('--configure',
                        action='store_true',
                        help='Configure default values.')
    args = parser.parse_args()

    if args.configure:
        music_rename.config.ask_user_config()
        sys.exit(0)

    if args.directory is not None:
        if os.path.isdir(args.directory):
            os.chdir(args.directory)
        else:
            sys.exit(1)

    config = music_rename.config.get_populated_configuration()

    if args.rename_active:
        print(colored('Actively moving files!', 'red', attrs=['bold']))
    print("Current directory: " + os.getcwd() + "\n")

    music_rename.artists.get_artist_directories(config, args.rename_active)
