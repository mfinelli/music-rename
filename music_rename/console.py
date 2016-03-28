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
import music_rename

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
    args = parser.parse_args()

    if args.directory is not None and os.path.isdir(args.directory):
        os.chdir(args.directory)

    print("Current directory: " + os.getcwd())
