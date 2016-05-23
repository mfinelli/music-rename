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
    os.mkdir(os.path.join(dir,
                          'Some directory that is way too many characters'))
    os.mknod(os.path.join(dir, 'somefile.txt'))
    os.mknod(os.path.join(dir, 'øther fíle.txt'))

    albums = ['[1999] Some album', '[1999] Ánother album',
              '[1999] A really long album title that needs to be truncated']
    for album in albums:
        os.mkdir(os.path.join(dir, 'Fine', album))
        os.mkdir(os.path.join(dir, 'Sömé Àccents', album))
    os.mknod(os.path.join(dir, 'Fine', 'album file.txt'))
    os.mknod(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    os.mknod(os.path.join(dir, 'Sömé Àccents', 'album file.txt'))
    os.mknod(os.path.join(dir, 'Sömé Àccents', 'ânother album file.txt'))

    songs = ['01 A song.flac', '02 Another song.flac', '03 Evérything.flac',
             '04 A really long song title that will shorten.flac',
             'folder.jpg', 'output.log', 'sums.md5']
    for song in songs:
        os.mknod(os.path.join(dir, 'Fine', '[1999] Some album', song))
        os.mknod(os.path.join(dir, 'Fine', '[1999] Ánother album', song))
        os.mknod(os.path.join(dir, 'Sömé Àccents', '[1999] Some album', song))
        os.mknod(os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                              song))

    extra_dirs = ['artwork', 'video', 'a long extra directory']
    for extra_dir in extra_dirs:
        os.mkdir(os.path.join(dir, 'Fine', '[1999] Some album', extra_dir))
        os.mkdir(os.path.join(dir, 'Fine', '[1999] Ánother album', extra_dir))
        os.mkdir(os.path.join(dir, 'Sömé Àccents', '[1999] Some album',
                              extra_dir))
        os.mkdir(os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                              extra_dir))

    extra_items = ['some-single.jpg', 'a-many-character-string-item.jpg']
    for extra in extra_items:
        os.mknod(os.path.join(dir, 'Fine', '[1999] Some album', 'artwork',
                              extra))
        os.mknod(os.path.join(dir, 'Fine', '[1999] Some album',
                              'a long extra directory', extra))
        os.mknod(os.path.join(dir, 'Fine', '[1999] Ánother album', 'artwork',
                              extra))
        os.mknod(os.path.join(dir, 'Fine', '[1999] Ánother album',
                              'a long extra directory', extra))
        os.mknod(os.path.join(dir, 'Sömé Àccents', '[1999] Some album',
                              'artwork', extra))
        os.mknod(os.path.join(dir, 'Sömé Àccents', '[1999] Some album',
                              'a long extra directory', extra))
        os.mknod(os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                              'artwork', extra))
        os.mknod(os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                              'a long extra directory', extra))

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
    assert os.path.exists(os.path.join(
        dir, 'Some directory that is way too many characters'))
    assert os.path.exists(os.path.join(dir, 'somefile.txt'))
    assert os.path.exists(os.path.join(dir, 'øther fíle.txt'))

    music_rename.artists.get_artist_directories(
        music_rename.config.get_populated_configuration(), False)

    assert os.path.exists(os.path.join(dir, 'Fine'))
    assert os.path.exists(os.path.join(dir, 'With Space'))
    assert os.path.exists(os.path.join(dir, 'With_Underscore'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents'))
    assert os.path.exists(os.path.join(
        dir, 'Some directory that is way too many characters'))
    assert os.path.exists(os.path.join(dir, 'somefile.txt'))
    assert os.path.exists(os.path.join(dir, 'øther fíle.txt'))


def test_artists(dir):
    assert os.path.exists(os.path.join(dir, 'Fine'))
    assert os.path.exists(os.path.join(dir, 'With Space'))
    assert os.path.exists(os.path.join(dir, 'With_Underscore'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents'))
    assert os.path.exists(os.path.join(
        dir, 'Some directory that is way too many characters'))
    assert os.path.exists(os.path.join(dir, 'somefile.txt'))
    assert os.path.exists(os.path.join(dir, 'øther fíle.txt'))

    music_rename.artists.get_artist_directories(
        music_rename.config.get_populated_configuration(), True)

    assert os.path.exists(os.path.join(dir, 'Fine'))
    assert os.path.exists(os.path.join(dir, 'With Space'))
    assert os.path.exists(os.path.join(dir, 'WithUnderscore'))
    assert os.path.exists(os.path.join(dir, 'Some Accents'))
    assert os.path.exists(os.path.join(dir,
                                       'Some directory that is way too m'))
    assert os.path.exists(os.path.join(dir, 'somefile.txt'))
    assert os.path.exists(os.path.join(dir, 'øther fíle.txt'))


def test_dry_run_albums(dir):
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album'))
    assert os.path.exists(os.path.join(
        dir, 'Fine',
        '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents',
        '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       'ânother album file.txt'))

    music_rename.artists.get_artist_directories(
        music_rename.config.get_populated_configuration(), False)

    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album'))
    assert os.path.exists(os.path.join(
        dir, 'Fine',
        '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents',
        '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       'ânother album file.txt'))


def test_albums(dir):
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album'))
    assert os.path.exists(os.path.join(
        dir, 'Fine',
        '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents',
        '[1999] A really long album title that needs to be truncated'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       'ânother album file.txt'))

    music_rename.artists.get_artist_directories(
        music_rename.config.get_populated_configuration(), True)

    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album'))
    assert os.path.exists(os.path.join(dir, 'Fine',
                                       '[1999] A really long album ti'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Fine', 'ânother album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Some album'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Another album'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] A really long album ti'))
    assert os.path.exists(os.path.join(dir, 'Some Accents', 'album file.txt'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       'ânother album file.txt'))


def test_dry_run_songs(dir):
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '01 A song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '02 Another song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'output.log'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'sums.md5'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       '01 A song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       '02 Another song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Ánother album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'output.log'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'sums.md5'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', '01 A song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', '02 Another song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'output.log'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'sums.md5'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', '01 A song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', '02 Another song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'output.log'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'sums.md5'))

    music_rename.artists.get_artist_directories(
        music_rename.config.get_populated_configuration(), False)

    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '01 A song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '02 Another song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'output.log'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'sums.md5'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       '01 A song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       '02 Another song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Ánother album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'output.log'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'sums.md5'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', '01 A song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', '02 Another song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'output.log'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'sums.md5'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', '01 A song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', '02 Another song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'output.log'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'sums.md5'))


def test_songs(dir):
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '01 A song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '02 Another song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'output.log'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'sums.md5'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       '01 A song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       '02 Another song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Ánother album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'output.log'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'sums.md5'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', '01 A song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', '02 Another song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'output.log'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'sums.md5'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', '01 A song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', '02 Another song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', '03 Evérything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                     '04 A really long song title that will shorten.flac'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'output.log'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'sums.md5'))

    music_rename.artists.get_artist_directories(
        music_rename.config.get_populated_configuration(), True)

    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '01 A song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '02 Another song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       '03 Everything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album',
                     '04 A really long song title that will.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'output.log'))
    assert not os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                           'sums.md5'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       '01 A song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       '02 Another song.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       '03 Everything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Another album',
                     '04 A really long song title that will.flac'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       'output.log'))
    assert not os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                           'sums.md5'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Some album', '01 A song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Some Accents', '[1999] Some album', '02 Another song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Some Accents', '[1999] Some album', '03 Everything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Some album',
                     '04 A really long song title that will.flac'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Some album', 'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Some album', 'output.log'))
    assert not os.path.exists(os.path.join(dir, 'Some Accents',
                                           '[1999] Some album', 'sums.md5'))
    assert os.path.exists(os.path.join(
        dir, 'Some Accents', '[1999] Another album', '01 A song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Some Accents', '[1999] Another album', '02 Another song.flac'))
    assert os.path.exists(os.path.join(
        dir, 'Some Accents', '[1999] Another album', '03 Everything.flac'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Another album',
                     '04 A really long song title that will.flac'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Another album', 'folder.jpg'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Another album', 'output.log'))
    assert not os.path.exists(os.path.join(dir, 'Some Accents',
                                           '[1999] Another album', 'sums.md5'))


def test_dry_run_extra(dir):
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'artwork'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'video'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'a long extra directory'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'artwork', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'a long extra directory',
                                       'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'artwork'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'video'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'a long extra directory'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'artwork', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Ánother album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Ánother album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'a long extra directory',
                                       'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'artwork'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'video'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', 'a long extra directory'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album', 'artwork',
                     'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', 'a long extra directory',
        'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'artwork'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'video'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', 'a long extra directory'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album', 'artwork',
                     'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', 'a long extra directory',
        'a-many-character-string-item.jpg'))

    music_rename.artists.get_artist_directories(
        music_rename.config.get_populated_configuration(), False)

    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'artwork'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'video'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'a long extra directory'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'artwork', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'a long extra directory',
                                       'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'artwork'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'video'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'a long extra directory'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'artwork', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Ánother album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Ánother album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'a long extra directory',
                                       'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'artwork'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'video'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', 'a long extra directory'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album', 'artwork',
                     'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', 'a long extra directory',
        'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'artwork'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'video'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', 'a long extra directory'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album', 'artwork',
                     'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', 'a long extra directory',
        'a-many-character-string-item.jpg'))


def test_extra(dir):
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'artwork'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'video'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'a long extra directory'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'artwork'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'a long extra directory'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'artwork', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'a long extra directory',
                                       'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'artwork'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'video'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'a long extra directory'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'artwork', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Ánother album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Ánother album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Ánother album',
                                       'a long extra directory',
                                       'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'artwork'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Some album', 'video'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', 'a long extra directory'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album', 'artwork',
                     'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Some album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Some album', 'a long extra directory',
        'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'artwork'))
    assert os.path.exists(os.path.join(dir, 'Sömé Àccents',
                                       '[1999] Ánother album', 'video'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', 'a long extra directory'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album', 'artwork',
                     'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album',
                     'a long extra directory', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Sömé Àccents', '[1999] Ánother album', 'artwork',
                     'a-many-character-string-item.jpg'))
    assert os.path.exists(os.path.join(
        dir, 'Sömé Àccents', '[1999] Ánother album', 'a long extra directory',
        'a-many-character-string-item.jpg'))

    music_rename.artists.get_artist_directories(
        music_rename.config.get_populated_configuration(), True)

    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'artwork'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'video'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'a long extra'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'artwork', 'some-single.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Some album',
                                       'a long extra', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album', 'artwork',
                     'a-many-character-string-i.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Some album', 'a long extra',
                     'a-many-character-string-i.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       'artwork'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       'video'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       'a long extra'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       'artwork', 'some-single.jpg'))
    assert os.path.exists(os.path.join(dir, 'Fine', '[1999] Another album',
                                       'a long extra', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Another album', 'artwork',
                     'a-many-character-string-i.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Fine', '[1999] Another album', 'a long extra',
                     'a-many-character-string-i.jpg'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Some album', 'artwork'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Some album', 'video'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Some album', 'a long extra'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Some album', 'artwork',
                     'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Some album', 'a long extra',
                     'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Some album', 'artwork',
                     'a-many-character-string-i.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Some album', 'a long extra',
                     'a-many-character-string-i.jpg'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Another album', 'artwork'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Another album', 'video'))
    assert os.path.exists(os.path.join(dir, 'Some Accents',
                                       '[1999] Another album', 'a long extra'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Another album', 'artwork',
                     'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Another album',
                     'a long extra', 'some-single.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Another album', 'artwork',
                     'a-many-character-string-i.jpg'))
    assert os.path.exists(
        os.path.join(dir, 'Some Accents', '[1999] Another album',
                     'a long extra', 'a-many-character-string-i.jpg'))
