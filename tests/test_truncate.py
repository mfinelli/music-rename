from music_rename import sanitize


def test_shorter_string():
    assert sanitize.truncate('abc', 5) == 'abc'


def test_longer_string():
    assert sanitize.truncate('abcde', 4) == 'abcd'
