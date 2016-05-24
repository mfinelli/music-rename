import pytest
import tempfile
import shutil
import os
import music_rename
from music_rename import checksum


@pytest.fixture(scope="module", autouse=True)
def dir(request):
    dir = tempfile.mkdtemp()

    os.mknod(os.path.join(dir, 'empty.txt'))

    def cleanup():
        shutil.rmtree(dir)

    request.addfinalizer(cleanup)
    return dir


def test_emptyfile(dir):
    assert music_rename.checksum.md5sum_file(os.path.join(
        dir, 'empty.txt')) == 'd41d8cd98f00b204e9800998ecf8427e'
