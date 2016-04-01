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


def sanitize_final_character(string):
    # These are characters that we do NOT want to allow as the final
    # character of a file or directory name.
    no_last = ['(', '.', '-', '[', ',', '&', '\'']

    # First remove all surrounding whitespace.
    string = string.strip()

    # While the last character is not allowed remove it and strip surrounding
    # whitespace again.
    while string[-1] in no_last:
        string = string[:-1].strip()

    return string
