import pytest
import tempfile
import shutil
import os
import music_rename
from music_rename import artists
from music_rename import config

@pytest.fixture()
def dir(request):
    dir = tempfile.mkdtemp()

    os.mkdir(os.path.join(dir, 'Fine'))
    os.mkdir(os.path.join(dir, 'With Space'))
    os.mkdir(os.path.join(dir, 'With_Underscore'))
    os.mkdir(os.path.join(dir, 'Sömé Àccents'))
    os.mkdir(os.path.join(dir, 'Some directory that is way too many characters'))

    prev = os.getcwd()
    os.chdir(dir)

    def cleanup():
        os.chdir(prev)
        shutil.rmtree(dir)
    request.addfinalizer(cleanup)
    return dir

def test_artists(dir):
    assert os.path.exists(os.path.join(dir, 'Fine'))
    assert os.path.exists(os.path.join(dir, 'With Space'))
    assert os.path.exists(os.path.join(dir, 'With_Underscore'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents'))
    assert os.path.exists(os.path.join(dir, 'Some directory that is way too many characters'))

    music_rename.artists.get_artist_directories(music_rename.config.get_populated_configuration(), True)

    assert os.path.exists(os.path.join(dir, 'Fine'))
    assert os.path.exists(os.path.join(dir, 'With Space'))
    assert os.path.exists(os.path.join(dir, 'WithUnderscore'))
    assert os.path.exists(os.path.join(dir, 'Some Accents'))
    assert os.path.exists(os.path.join(dir, 'Some directory that is way too m'))
