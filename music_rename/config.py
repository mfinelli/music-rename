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

DEFAULT_ARTIST_MAXLEN = 32
DEFAULT_ALBUM_MEXLEN = 29
DEFAULT_EXTRA_DIR_MAXLEN = 13
DEFAULT_EXTRA_MEXLEN = 25
DEFAULT_SONG_MAXLEN = 38

def ask_user_config():
    s = input('Artist maximum length (32): ')
    print(s)
