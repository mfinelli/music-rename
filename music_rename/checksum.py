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

import hashlib


def md5sum_file(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()
    # md5 = hashlib.md5()
    # with open(path, 'rb') as file:
    #     for chunk in iter(lambda: file.read(128 * md5.block_size), b''):
    #         md5.update(chunk)
    # return md5.hexdigest()
