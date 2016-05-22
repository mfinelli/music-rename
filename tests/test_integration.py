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
    os.mknod(os.path.join(dir, 'somefile.txt'))
    os.mknod(os.path.join(dir, 'øther fíle.txt'))

    albums = ['[1999] Some album', '[1999] Ánother album', '[1999] A really long album title that needs to be truncated']
    for album in albums:
        os.mkdir(os.path.join(dir, 'Fine', album))
        os.mkdir(os.path.join(dir, 'Sömé Àccents', album))
    os.mknod(os.path.join(dir, 'Fine', 'album file.txt'))
    os.mknod(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    os.mknod(os.path.join(dir, 'Sömé Àccents', 'album file.txt'))
    os.mknod(os.path.join(dir, 'Sömé Àccents', 'ânother album file.txt'))

    prev = os.getcwd()
    os.chdir(dir)

    def cleanup():
        os.chdir(prev)
        shutil.rmtree(dir)
    request.addfinalizer(cleanup)
    return dir

def test_dry_run_artists(dir):
    assert os.path.exists(os.path.join(dir, 'Fine'))
    assert os.path.exists(os.path.join(dir, 'With Space'))
    assert os.path.exists(os.path.join(dir, 'With_Underscore'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents'))
    assert os.path.exists(os.path.join(dir, 'Some directory that is way too many characters'))
    assert os.path.exists(os.path.join(dir, 'somefile.txt'))
    assert os.path.exists(os.path.join(dir, 'øther fíle.txt'))

    music_rename.artists.get_artist_directories(music_rename.config.get_populated_configuration(), False)

    assert os.path.exists(os.path.join(dir, 'Fine'))
    assert os.path.exists(os.path.join(dir, 'With Space'))
    assert os.path.exists(os.path.join(dir, 'With_Underscore'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents'))
    assert os.path.exists(os.path.join(dir, 'Some directory that is way too many characters'))
    assert os.path.exists(os.path.join(dir, 'somefile.txt'))
    assert os.path.exists(os.path.join(dir, 'øther fíle.txt'))

def test_artists(dir):
    assert os.path.exists(os.path.join(dir, 'Fine'))
    assert os.path.exists(os.path.join(dir, 'With Space'))
    assert os.path.exists(os.path.join(dir, 'With_Underscore'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents'))
    assert os.path.exists(os.path.join(dir, 'Some directory that is way too many characters'))
    assert os.path.exists(os.path.join(dir, 'somefile.txt'))
    assert os.path.exists(os.path.join(dir, 'øther fíle.txt'))

    music_rename.artists.get_artist_directories(music_rename.config.get_populated_configuration(), True)

    assert os.path.exists(os.path.join(dir, 'Fine'))
    assert os.path.exists(os.path.join(dir, 'With Space'))
    assert os.path.exists(os.path.join(dir, 'WithUnderscore'))
    assert os.path.exists(os.path.join(dir, 'Some Accents'))
    assert os.path.exists(os.path.join(dir, 'Some directory that is way too m'))
    assert os.path.exists(os.path.join(dir, 'somefile.txt'))
    assert os.path.exists(os.path.join(dir, 'øther fíle.txt'))

def test_dry_run_albums(dir):
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', 'ânother album file.txt'))

    music_rename.artists.get_artist_directories(music_rename.config.get_populated_configuration(), False)

    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', 'ânother album file.txt'))

def test_albums(dir):
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', 'ânother album file.txt'))

    music_rename.artists.get_artist_directories(music_rename.config.get_populated_configuration(), True)

    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] A really long album ti'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Some Accents', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Some Accents', '[1999] Another album'))
    assert os.path.exists(os.path.join(dir, 'Some Accents', '[1999] A really long album ti'))
    assert os.path.exists(os.path.join(dir, 'Some Accents', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Some Accents', 'ânother album file.txt'))
