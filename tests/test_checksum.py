import pytest
import tempfile
import shutil
import os
import music_rename
from music_rename import checksum


@pytest.fixture()
def empty(request):
    dir = tempfile.mkdtemp()

    os.mknod(os.path.join(dir, 'empty.txt'))

    def cleanup():
        shutil.rmtree(dir)

    request.addfinalizer(cleanup)
    return os.path.join(dir, 'empty.txt')


@pytest.fixture()
def not_empty(request):
    file = tempfile.mkstemp()

    print(file)
    fp = open(file[1], 'w')
    fp.write("Some text...\n")
    fp.close()

    def cleanup():
        os.remove(file[1])

    request.addfinalizer(cleanup)
    return file[1]


def test_emptyfile(empty):
    assert music_rename.checksum.md5sum_file(
        empty) == 'd41d8cd98f00b204e9800998ecf8427e'


def test_not_empty(not_empty):
    assert music_rename.checksum.md5sum_file(
        not_empty) == '4e3e88d75e5dc70c6ebb2712bcf16227'
