from music_rename import sanitize

def test_no_change():
    assert sanitize.sanitize('abc', 10) == 'abc'

def test_truncate():
    assert sanitize.sanitize('abcdef', 3) == 'abc'
